#!/usr/bin/env python3
"""Compare CPU training throughput across controlled RONIN-10M configurations."""
import argparse, hashlib, json, random, time
from dataclasses import replace
from pathlib import Path

import numpy as np
import torch
from tokenizers import Tokenizer
from roninia.config import ModelConfig
from roninia.model import RoninLM

CONFIGS = [
    {"name": "baseline_fp32_b4_ctx512_t2", "batch_size": 4, "context": 512, "threads": 2, "bf16": False},
    {"name": "fp32_b2_ctx512_t2", "batch_size": 2, "context": 512, "threads": 2, "bf16": False},
    {"name": "fp32_b4_ctx256_t2", "batch_size": 4, "context": 256, "threads": 2, "bf16": False},
    {"name": "fp32_b4_ctx512_t1", "batch_size": 4, "context": 512, "threads": 1, "bf16": False},
    {"name": "bf16_b4_ctx512_t2", "batch_size": 4, "context": 512, "threads": 2, "bf16": True},
]

def sha256(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for chunk in iter(lambda: f.read(8 * 1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", type=Path, required=True)
    ap.add_argument("--corpus", type=Path, required=True)
    ap.add_argument("--tokenizer", type=Path, required=True)
    ap.add_argument("--steps", type=int, default=200)
    ap.add_argument("--warmup-steps", type=int, default=20)
    ap.add_argument("--output-dir", type=Path, default=Path("benchmark-results"))
    args = ap.parse_args()
    if args.steps < 2 or not 0 <= args.warmup_steps < args.steps:
        raise SystemExit("Require steps >= 2 and 0 <= warmup-steps < steps")

    torch.set_num_threads(2)
    tokenizer = Tokenizer.from_file(str(args.tokenizer))
    eos_id = tokenizer.token_to_id("<|eos|>")
    if eos_id is None:
        raise SystemExit("Tokenizer is missing <|eos|>")
    token_cache = args.output_dir / "corpus-tokens.u16"
    args.output_dir.mkdir(parents=True, exist_ok=True)
    count = 0
    with token_cache.open("wb") as out, args.corpus.open(encoding="utf-8") as source:
        for line in source:
            if line.strip():
                ids = tokenizer.encode(line.strip()).ids
                if ids:
                    np.asarray(ids + [eos_id], dtype=np.uint16).tofile(out)
                    count += len(ids) + 1
    data = np.memmap(token_cache, dtype=np.uint16, mode="r")
    base = ModelConfig.load(args.config)
    results = []

    for index, spec in enumerate(CONFIGS):
        result = {"name": spec["name"], **spec, "steps": args.steps,
                  "warmup_steps": args.warmup_steps, "status": "ok"}
        try:
            context = spec["context"]
            if context > base.context_length:
                raise ValueError("benchmark context exceeds model config")
            cfg = replace(base, context_length=context)
            torch.set_num_threads(spec["threads"])
            random.seed(20261110)
            torch.manual_seed(20261110)
            np.random.seed(20261110)
            model = RoninLM(cfg)
            optimizer = torch.optim.AdamW(model.parameters(), lr=3e-4, betas=(0.9, 0.95), weight_decay=0.1)
            model.train()
            upper = len(data) - context - 1
            if upper <= 0:
                raise ValueError("not enough tokenized corpus for selected context")
            measured_times, losses = [], []
            started_all = time.perf_counter()
            for step in range(args.steps):
                starts = torch.randint(0, upper, (spec["batch_size"],))
                batch = torch.stack([
                    torch.from_numpy(np.asarray(data[int(s):int(s)+context], dtype=np.int64))
                    for s in starts
                ])
                optimizer.zero_grad(set_to_none=True)
                with torch.autocast(device_type="cpu", dtype=torch.bfloat16, enabled=spec["bf16"]):
                    _, loss = model(batch, batch)
                loss.backward()
                torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
                optimizer.step()
                if step >= args.warmup_steps:
                    measured_times.append(time.perf_counter())
                    losses.append(float(loss.detach()))
            total_seconds = time.perf_counter() - started_all
            measured_seconds = measured_times[-1] - (started_all + 0) if False else None
            # Use an independent timed pass boundary: total includes warmup, while
            # measured throughput is conservatively derived from total / all steps.
            result.update({
                "total_seconds": round(total_seconds, 3),
                "seconds_per_step": round(total_seconds / args.steps, 5),
                "steps_per_second": round(args.steps / total_seconds, 4),
                "tokens_per_second": round(args.steps * spec["batch_size"] * context / total_seconds, 2),
                "final_loss": round(losses[-1], 6) if losses else None,
                "parameter_count": model.parameter_count(),
                "dtype": "bf16-autocast" if spec["bf16"] else "fp32",
            })
            del model, optimizer
        except Exception as exc:
            result.update({"status": "error", "error": f"{type(exc).__name__}: {exc}"})
        results.append(result)
        print(json.dumps(result), flush=True)

    payload = {
        "schema": "roninia-speed-benchmark-v1",
        "steps_per_configuration": args.steps,
        "warmup_steps_included_in_200": args.warmup_steps,
        "corpus_sha256": sha256(args.corpus),
        "tokenizer_sha256": sha256(args.tokenizer),
        "token_count": int(count),
        "results": results,
    }
    (args.output_dir / "benchmark.json").write_text(json.dumps(payload, indent=2) + "\n")
    lines = ["# RONIN-10M CPU speed benchmark", "",
             f"- Steps per configuration: {args.steps} (including {args.warmup_steps} warmup steps)",
             f"- Corpus SHA-256: {payload['corpus_sha256']}",
             f"- Tokenizer SHA-256: {payload['tokenizer_sha256']}", "",
             "| Configuration | Status | s/step | steps/s | tokens/s | final loss |",
             "|---|---:|---:|---:|---:|---:|"]
    for r in results:
        lines.append(f"| {r['name']} | {r['status']} | {r.get('seconds_per_step','—')} | {r.get('steps_per_second','—')} | {r.get('tokens_per_second','—')} | {r.get('final_loss','—')} |")
    (args.output_dir / "benchmark.md").write_text("\n".join(lines) + "\n")
    token_cache.unlink(missing_ok=True)
    if not any(r["status"] == "ok" for r in results):
        raise SystemExit("All benchmark configurations failed")

if __name__ == "__main__":
    main()
