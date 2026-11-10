#!/usr/bin/env python3
"""Train RONIN-10M from random initialization with periodic checkpoints and validation."""
import argparse
import hashlib
import json
import random
from pathlib import Path

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
    ap.add_argument("--corpus", type=Path, required=True)
    ap.add_argument("--tokenizer", type=Path, required=True)
    ap.add_argument("--output-dir", type=Path, default=Path("runs/ronin-10m"))
    ap.add_argument("--steps", type=int, default=50000)
    ap.add_argument("--batch-size", type=int, default=2)
    ap.add_argument("--threads", type=int, default=2)
    ap.add_argument("--learning-rate", type=float, default=3e-4)
    ap.add_argument("--checkpoint-every", type=int, default=5000)
    ap.add_argument("--eval-batches", type=int, default=16)
    args = ap.parse_args()
    if min(args.steps, args.batch_size, args.threads, args.checkpoint_every, args.eval_batches) <= 0:
        raise SystemExit("steps, batch-size, threads, checkpoint-every and eval-batches must be positive")

    torch.set_num_threads(args.threads)
    random.seed(20261110)
    torch.manual_seed(20261110)
    config = ModelConfig.load(args.config)
    tokenizer = Tokenizer.from_file(str(args.tokenizer))
    eos_id = tokenizer.token_to_id("<|eos|>")
    if eos_id is None:
        raise SystemExit("Tokenizer is missing <|eos|>")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    token_cache = args.output_dir / "corpus-tokens.u16"
    token_count = 0
    with token_cache.open("wb") as binary, args.corpus.open(encoding="utf-8") as corpus:
        for line in corpus:
            if line.strip():
                ids = tokenizer.encode(line.strip()).ids
                if ids:
                    np.asarray(ids + [eos_id], dtype=np.uint16).tofile(binary)
                    token_count += len(ids) + 1

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
    optimizer = torch.optim.AdamW(
        model.parameters(), lr=args.learning_rate, betas=(0.9, 0.95), weight_decay=0.1
    )
    model.train()
    history = []
    checkpoints = []
    for step in range(1, args.steps + 1):
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

        if step == 1 or step % 100 == 0:
            record = {"step": step, "train_loss": float(loss.detach())}
            history.append(record)
            print(json.dumps(record), flush=True)

        if step % args.checkpoint_every == 0 or step == args.steps:
            val_loss = evaluate(
                model, val_data, config.context_length,
                batches=args.eval_batches, batch_size=args.batch_size
            )
            checkpoint = args.output_dir / f"checkpoint-{step}.pt"
            payload = {
                "model_state_dict": model.state_dict(),
                "optimizer_state_dict": optimizer.state_dict(),
                "config": config.__dict__,
                "parameter_count": model.parameter_count(),
                "completed_steps": step,
                "tokenizer_sha256": sha256_file(args.tokenizer),
                "corpus_sha256": sha256_file(args.corpus),
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
            summary = {"step": step, "train_loss": float(loss.detach()),
                       "validation_loss": val_loss, "checkpoint": checkpoint.name,
                       "sha256": checksum}
            checkpoints.append(summary)
            (args.output_dir / "progress.json").write_text(
                json.dumps({"checkpoints": checkpoints}, indent=2) + "\n", encoding="utf-8"
            )
            print(json.dumps(summary), flush=True)

    token_cache.unlink(missing_ok=True)
    print(json.dumps({
        "completed_steps": args.steps,
        "parameters": model.parameter_count(),
        "tokens": token_count,
        "checkpoints": checkpoints,
    }), flush=True)


if __name__ == "__main__":
    main()
