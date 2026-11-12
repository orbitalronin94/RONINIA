#!/usr/bin/env python3
"""Train RONIN-10M from random initialization with periodic checkpoints and validation."""
import argparse
import hashlib
import json
import random
import sys
from pathlib import Path

# Make the src-layout package importable when invoked as `python scripts/train.py`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import numpy as np
import torch
from tokenizers import Tokenizer
from roninia.config import ModelConfig
from roninia.model import RoninLM


def sha256_file(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def evaluate(model, data, context, batches=16, batch_size=2):
    """Deterministic validation loss over fixed windows in the reserved corpus tail."""
    model.eval()
    generator = torch.Generator().manual_seed(20261110)
    upper = len(data) - context - 1
    losses = []
    with torch.no_grad():
        for _ in range(batches):
            starts = torch.randint(0, upper + 1, (batch_size,), generator=generator)
            batch = torch.stack([
                torch.from_numpy(np.asarray(
                    data[int(start):int(start) + context], dtype=np.int64
                )) for start in starts
            ])
            _, loss = model(batch, batch)
            losses.append(float(loss))
    model.train()
    return sum(losses) / len(losses)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", type=Path, required=True)
    ap.add_argument("--corpus", type=Path)
    ap.add_argument("--tokenizer", type=Path)
    ap.add_argument("--tokens", type=Path, help="Reusable uint16 token cache")
    ap.add_argument("--token-manifest", type=Path, help="Manifest for a reusable token cache")
    ap.add_argument("--output-dir", type=Path, default=Path("runs/ronin-10m"))
    ap.add_argument("--steps", type=int, default=50000)
    ap.add_argument("--batch-size", type=int, default=4)
    ap.add_argument("--threads", type=int, default=2)
    ap.add_argument("--learning-rate", type=float, default=3e-4)
    ap.add_argument("--warmup-steps", type=int, default=2000)
    ap.add_argument("--min-lr-ratio", type=float, default=0.1)
    ap.add_argument("--checkpoint-every", type=int, default=5000)
    ap.add_argument("--eval-batches", type=int, default=16)
    ap.add_argument("--resume", type=Path, help="Parent checkpoint to continue from")
    ap.add_argument("--allow-corpus-change", action="store_true", help="Explicitly continue from a parent checkpoint using a different verified corpus; tokenizer and model config must still match")
    args = ap.parse_args()
    if min(args.steps, args.batch_size, args.threads, args.checkpoint_every, args.eval_batches) <= 0 or args.warmup_steps < 0 or not 0 < args.min_lr_ratio <= 1:
        raise SystemExit("steps, batch-size, threads, checkpoint-every and eval-batches must be positive")

    torch.set_num_threads(args.threads)
    random.seed(20261110)
    torch.manual_seed(20261110)
    config = ModelConfig.load(args.config)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    token_manifest = None
    corpus_changed_from_parent = False
    generated_token_cache = args.tokens is None
    if generated_token_cache:
        if args.corpus is None or args.tokenizer is None or args.token_manifest is not None:
            raise SystemExit("provide --corpus and --tokenizer, or --tokens with --token-manifest")
        tokenizer = Tokenizer.from_file(str(args.tokenizer))
        if tokenizer.get_vocab_size() != config.vocab_size:
            raise SystemExit("tokenizer vocabulary size does not match model config")
        eos_id = tokenizer.token_to_id("<|eos|>")
        if eos_id is None:
            raise SystemExit("Tokenizer is missing <|eos|>")
        token_cache = args.output_dir / "corpus-tokens.u16"
        token_count = 0
        with token_cache.open("wb") as binary, args.corpus.open(encoding="utf-8") as corpus:
            for line in corpus:
                if line.strip():
                    ids = tokenizer.encode(line.strip()).ids
                    if ids:
                        np.asarray(ids + [eos_id], dtype=np.uint16).tofile(binary)
                        token_count += len(ids) + 1
        tokenizer_sha256 = sha256_file(args.tokenizer)
        corpus_sha256 = sha256_file(args.corpus)
    else:
        if args.corpus is not None or args.tokenizer is not None or args.token_manifest is None:
            raise SystemExit("pretokenized mode requires --tokens and --token-manifest only")
        token_cache = args.tokens
        manifest = json.loads(args.token_manifest.read_text(encoding="utf-8"))
        token_manifest = manifest
        if manifest.get("schema") != "roninia-token-cache-v1" or manifest.get("dtype") != "uint16":
            raise SystemExit("unsupported token cache manifest")
        if manifest.get("vocab_size") != config.vocab_size:
            raise SystemExit("token cache vocabulary does not match model config")
        if sha256_file(token_cache) != manifest.get("tokens_sha256"):
            raise SystemExit("token cache SHA-256 mismatch")
        token_count = manifest.get("token_count")
        if not isinstance(token_count, int) or token_count * 2 != token_cache.stat().st_size:
            raise SystemExit("token cache size/count mismatch")
        tokenizer_sha256 = manifest["tokenizer_sha256"]
        corpus_sha256 = manifest["corpus_sha256"]

    if token_count < (config.context_length + 2) * 2:
        raise SystemExit("Corpus too small for train/validation windows")
    data = np.memmap(token_cache, dtype=np.uint16, mode="r")
    if int(data.max()) >= config.vocab_size:
        raise SystemExit("Token ID outside configured vocabulary")

    # Fixed contiguous tail split: validation windows never enter optimizer batches.
    val_count = max(config.context_length + 2, token_count // 100)
    split = token_count - val_count
    train_data = data[:split]
    val_data = data[split:]
    if len(train_data) <= config.context_length + 1 or len(val_data) <= config.context_length + 1:
        raise SystemExit("Insufficient tokens after deterministic 99/1 train-validation split")

    model = RoninLM(config)
    resume_payload = None
    start_step = 0
    parent_checkpoint_sha256 = None
    if args.resume is not None:
        if not args.resume.is_file():
            raise SystemExit(f"Parent checkpoint not found: {args.resume}")
        resume_payload = torch.load(args.resume, map_location="cpu", weights_only=False)
        if resume_payload.get("config") != config.__dict__:
            raise SystemExit("Parent checkpoint model config does not match current config")
        parent_corpus_sha256 = resume_payload.get("corpus_sha256")
        corpus_changed_from_parent = parent_corpus_sha256 != corpus_sha256
        if corpus_changed_from_parent and not args.allow_corpus_change:
            raise SystemExit("Parent checkpoint corpus fingerprint does not match token cache; pass --allow-corpus-change only for an intentional, verified corpus transition")
        if corpus_changed_from_parent:
            print(json.dumps({"event":"explicit_corpus_transition","parent_corpus_sha256":parent_corpus_sha256,"new_corpus_sha256":corpus_sha256,"selection_policy":(token_manifest or {}).get("selection_policy")}),flush=True)
        if resume_payload.get("tokenizer_sha256") != tokenizer_sha256:
            raise SystemExit("Parent checkpoint tokenizer fingerprint does not match token cache")
        model.load_state_dict(resume_payload["model_state_dict"], strict=True)
        start_step = int(resume_payload.get("completed_steps", 0))
        if start_step <= 0:
            raise SystemExit("Parent checkpoint has no valid completed_steps")
        parent_checkpoint_sha256 = sha256_file(args.resume)
        print(json.dumps({
            "event": "resume_parent",
            "parent_checkpoint": str(args.resume),
            "parent_sha256": parent_checkpoint_sha256,
            "parent_completed_steps": start_step,
        }), flush=True)
    # Keep decay off biases, normalization parameters and the tied token embedding.
    decay, no_decay = [], []
    for name, parameter in model.named_parameters():
        if not parameter.requires_grad:
            continue
        if parameter.ndim < 2 or name.endswith("bias") or "norm" in name.lower() or "embedding" in name.lower() or "tok_emb" in name.lower():
            no_decay.append(parameter)
        else:
            decay.append(parameter)
    optimizer = torch.optim.AdamW(
        [
            {"params": decay, "weight_decay": 0.1},
            {"params": no_decay, "weight_decay": 0.0},
        ],
        lr=args.learning_rate, betas=(0.9, 0.95), eps=1e-8
    )

    warmup_steps = min(args.warmup_steps, max(0, args.steps - 1))
    def lr_factor(step):
        if warmup_steps and step < warmup_steps:
            return max(1e-8, float(step + 1) / warmup_steps)
        decay_steps = max(1, args.steps - warmup_steps)
        progress = min(1.0, max(0.0, (step - warmup_steps) / decay_steps))
        cosine = 0.5 * (1.0 + np.cos(np.pi * progress))
        return args.min_lr_ratio + (1.0 - args.min_lr_ratio) * float(cosine)
    scheduler = torch.optim.lr_scheduler.LambdaLR(optimizer, lr_factor)
    if resume_payload is not None:
        if "optimizer_state_dict" not in resume_payload:
            raise SystemExit("Parent checkpoint is missing optimizer state")
        optimizer.load_state_dict(resume_payload["optimizer_state_dict"])
        # Continue with a conservative fixed LR while preserving AdamW moments.
        for group in optimizer.param_groups:
            group["lr"] = args.learning_rate
            group["initial_lr"] = args.learning_rate
        scheduler = torch.optim.lr_scheduler.LambdaLR(optimizer, lambda _: 1.0)
    model.train()
    history = []
    checkpoints = []
    for local_step in range(1, args.steps + 1):
        step = start_step + local_step
        starts = torch.randint(0, len(train_data) - config.context_length - 1, (args.batch_size,))
        batch = torch.stack([
            torch.from_numpy(np.asarray(
                train_data[int(start):int(start) + config.context_length], dtype=np.int64
            )) for start in starts
        ])
        _, loss = model(batch, batch)
        optimizer.zero_grad(set_to_none=True)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        optimizer.step()
        scheduler.step()

        if step == 1 or step % 100 == 0:
            record = {"step": step, "train_loss": float(loss.detach()), "learning_rate": optimizer.param_groups[0]["lr"]}
            history.append(record)
            print(json.dumps(record), flush=True)

        if local_step % args.checkpoint_every == 0 or local_step == args.steps:
            val_loss = evaluate(
                model, val_data, config.context_length,
                batches=args.eval_batches, batch_size=args.batch_size
            )
            checkpoint = args.output_dir / f"checkpoint-{step}.pt"
            payload = {
                "model_state_dict": model.state_dict(),
                "optimizer_state_dict": optimizer.state_dict(),
                "scheduler_state_dict": scheduler.state_dict(),
                "optimizer": "AdamW", "betas": [0.9, 0.95],
                "weight_decay": 0.1, "no_decay_parameter_tensors": len(no_decay),
                "warmup_steps": warmup_steps, "min_lr_ratio": args.min_lr_ratio,
                "batch_size": args.batch_size, "peak_learning_rate": args.learning_rate,
                "config": config.__dict__,
                "parameter_count": model.parameter_count(),
                "completed_steps": step,
                "parent_checkpoint_sha256": parent_checkpoint_sha256,
                "optimizer_continued_from_parent": resume_payload is not None,
                "tokenizer_sha256": tokenizer_sha256,
                "corpus_sha256": corpus_sha256,
                "token_count": token_count,
                "train_tokens": len(train_data),
                "validation_tokens": len(val_data),
                "validation_method": "fixed contiguous final 1% of imported training corpus",
                "validation_loss": val_loss,
                "history": history,
            }
            torch.save(payload, checkpoint)
            checksum = sha256_file(checkpoint)
            with (args.output_dir / "SHA256SUMS").open("a", encoding="utf-8") as sums:
                sums.write(f"{checksum}  {checkpoint.name}\n")
            summary = {"step": step, "train_loss": float(loss.detach()), "learning_rate": optimizer.param_groups[0]["lr"],
                       "validation_loss": val_loss, "checkpoint": checkpoint.name,
                       "sha256": checksum}
            checkpoints.append(summary)
            (args.output_dir / "progress.json").write_text(
                json.dumps({"checkpoints": checkpoints}, indent=2) + "\n", encoding="utf-8"
            )
            print(json.dumps(summary), flush=True)

    if generated_token_cache:
        token_cache.unlink(missing_ok=True)
    print(json.dumps({
        "completed_steps": start_step + args.steps,
        "steps_this_run": args.steps,
        "parent_checkpoint_sha256": parent_checkpoint_sha256,
        "parameters": model.parameter_count(),
        "tokens": token_count,
        "checkpoints": checkpoints,
    }), flush=True)


if __name__ == "__main__":
    main()
