#!/usr/bin/env python3
"""CPU-friendly streaming training entry point. Always initializes a new model."""
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", type=Path, required=True)
    ap.add_argument("--corpus", type=Path, required=True)
    ap.add_argument("--tokenizer", type=Path, required=True)
    ap.add_argument("--output-dir", type=Path, default=Path("runs/ronin-10m"))
    ap.add_argument("--steps", type=int, default=1000)
    ap.add_argument("--batch-size", type=int, default=2)
    ap.add_argument("--threads", type=int, default=2)
    ap.add_argument("--learning-rate", type=float, default=3e-4)
    args = ap.parse_args()
    if min(args.steps, args.batch_size, args.threads) <= 0:
        raise SystemExit("steps, batch-size and threads must be positive")

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
    # uint16 covers the complete 16,384-token vocabulary; encode line-by-line.
    with token_cache.open("wb") as binary, args.corpus.open(encoding="utf-8") as corpus:
        for line in corpus:
            if line.strip():
                ids = tokenizer.encode(line.strip()).ids
                if ids:
                    np.asarray(ids + [eos_id], dtype=np.uint16).tofile(binary)
                    token_count += len(ids) + 1

    if token_count < config.context_length + 2:
        raise SystemExit("Corpus too small for one context window")
    data = np.memmap(token_cache, dtype=np.uint16, mode="r")
    if int(data.max()) >= config.vocab_size:
        raise SystemExit("Token ID outside configured vocabulary")

    model = RoninLM(config)
    optimizer = torch.optim.AdamW(
        model.parameters(), lr=args.learning_rate, betas=(0.9, 0.95), weight_decay=0.1
    )
    model.train()
    history = []
    for step in range(1, args.steps + 1):
        starts = torch.randint(0, len(data) - config.context_length - 1, (args.batch_size,))
        batch = torch.stack([
            torch.from_numpy(
                np.asarray(data[int(start):int(start) + config.context_length], dtype=np.int64)
            )
            for start in starts
        ])
        _, loss = model(batch, batch)
        optimizer.zero_grad(set_to_none=True)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        optimizer.step()
        if step == 1 or step % 100 == 0 or step == args.steps:
            history.append({"step": step, "loss": float(loss.detach())})
            print(json.dumps(history[-1]), flush=True)

    checkpoint = args.output_dir / f"checkpoint-{args.steps}.pt"
    torch.save({
        "model_state_dict": model.state_dict(),
        "config": config.__dict__,
        "parameter_count": model.parameter_count(),
        "completed_steps": args.steps,
        "tokenizer_sha256": sha256_file(args.tokenizer),
        "corpus_sha256": sha256_file(args.corpus),
        "token_count": token_count,
        "history": history,
    }, checkpoint)
    checksum = sha256_file(checkpoint)
    (args.output_dir / "SHA256SUMS").write_text(
        f"{checksum}  {checkpoint.name}" + chr(10), encoding="utf-8"
    )
    token_cache.unlink(missing_ok=True)
    print(json.dumps({
        "checkpoint": str(checkpoint),
        "sha256": checksum,
        "parameters": model.parameter_count(),
        "tokens": token_count,
    }))


if __name__ == "__main__":
    main()
