#!/usr/bin/env python3
"""Create the deterministic step-0 RONIN-10M checkpoint and run the fixed inference holdout."""
import argparse
import hashlib
import json
import random
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import torch
from tokenizers import Tokenizer

import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from roninia.config import ModelConfig
from roninia.model import RoninLM

SEED = 20261110


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_holdout(path: Path):
    rows, seen = [], set()
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        row = json.loads(line)
        for key in ("id", "domain", "question", "rubric"):
            if not row.get(key):
                raise ValueError(f"{path}:{n}: missing {key}")
        if row["id"] in seen:
            raise ValueError(f"duplicate holdout id: {row['id']}")
        if row.get("split") != "inference_only":
            raise ValueError(f"{row['id']}: not marked inference_only")
        seen.add(row["id"])
        rows.append(row)
    if len(rows) != 100:
        raise ValueError(f"expected exactly 100 holdout questions, got {len(rows)}")
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", type=Path, default=ROOT / "configs/ronin-10m.json")
    ap.add_argument("--tokenizer", type=Path, required=True)
    ap.add_argument("--holdout", type=Path, required=True)
    ap.add_argument("--output-dir", type=Path, default=ROOT / "runs/baseline-step-0")
    ap.add_argument("--threads", type=int, default=2)
    ap.add_argument("--max-new-tokens", type=int, default=32)
    ap.add_argument("--max-new-bytes", type=int, default=128)
    args = ap.parse_args()

    if args.threads < 1 or not 1 <= args.max_new_tokens <= 128 or args.max_new_bytes < 1:
        raise SystemExit("invalid generation limits")
    torch.set_num_threads(args.threads)
    torch.use_deterministic_algorithms(True)
    random.seed(SEED)
    np.random.seed(SEED)
    torch.manual_seed(SEED)

    config = ModelConfig.load(args.config)
    tokenizer = Tokenizer.from_file(str(args.tokenizer))
    eos_id = tokenizer.token_to_id("<|eos|>")
    if eos_id is None:
        raise SystemExit("tokenizer is missing <|eos|>")
    if tokenizer.get_vocab_size() != config.vocab_size:
        raise SystemExit("tokenizer vocabulary size does not match model config")

    model = RoninLM(config).cpu()
    model.eval()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    checkpoint_path = args.output_dir / "checkpoint-step-0.pt"
    tokenizer_sha = sha256(args.tokenizer)
    payload = {
        "model_state_dict": model.state_dict(),
        "config": config.__dict__,
        "parameter_count": model.parameter_count(),
        "completed_steps": 0,
        "seed": SEED,
        "initialization": "RoninLM._init_weights; torch.manual_seed(20261110)",
        "tokenizer_sha256": tokenizer_sha,
        "checkpoint_kind": "untrained-initialization",
    }
    torch.save(payload, checkpoint_path)
    checkpoint_sha = sha256(checkpoint_path)

    rows = load_holdout(args.holdout)
    results = []
    instruction = (
        "Responde en castellano. Si no sabes algo, dilo claramente. "
        "No inventes datos ni afirmes como cierto lo que no puedas justificar."
    )
    with torch.inference_mode():
        for index, row in enumerate(rows, 1):
            prompt = instruction + "\\n\\n" + row["question"].strip() + "\\nRespuesta:"
            ids = tokenizer.encode(prompt).ids
            if not ids:
                raise ValueError(f"{row['id']}: empty prompt encoding")
            generated = []
            generated_bytes = 0
            started = time.perf_counter()
            for _ in range(args.max_new_tokens):
                context_ids = ids[-config.context_length:]
                input_ids = torch.tensor([context_ids], dtype=torch.long)
                logits, _ = model(input_ids)
                next_id = int(torch.argmax(logits[0, -1]).item())
                if next_id == eos_id:
                    break
                piece = tokenizer.id_to_token(next_id) or ""
                piece_bytes = tokenizer.decode([next_id], skip_special_tokens=True).encode("utf-8")
                if generated_bytes + len(piece_bytes) > args.max_new_bytes:
                    break
                generated.append(next_id)
                ids.append(next_id)
                generated_bytes += len(piece_bytes)
            answer = tokenizer.decode(generated, skip_special_tokens=True).strip()
            elapsed = time.perf_counter() - started
            results.append({
                "id": row["id"], "domain": row["domain"],
                "question": row["question"], "rubric": row["rubric"],
                "answer": answer, "generated_token_ids": generated,
                "elapsed_seconds": round(elapsed, 6),
            })
            print(json.dumps({"completed": index, "total": len(rows),
                              "id": row["id"], "elapsed_seconds": round(elapsed, 3)}), flush=True)

    holdout_sha = sha256(args.holdout)
    diary = {
        "schema_version": 1,
        "benchmark": "MINIRONIN inference holdout v1 (100 inference-only questions)",
        "label": "RONIN-10M-step-0-baseline",
        "completed_steps": 0,
        "seed": SEED,
        "parameter_count": model.parameter_count(),
        "config": config.__dict__,
        "checkpoint_sha256": checkpoint_sha,
        "tokenizer_sha256": tokenizer_sha,
        "holdout_sha256": holdout_sha,
        "holdout_count": len(results),
        "generation": {
            "instruction": instruction, "max_new_tokens": args.max_new_tokens,
            "max_new_bytes": args.max_new_bytes, "threads": args.threads,
            "kv_cache": False, "decoding": "greedy_argmax",
        },
        "rag": {"enabled": False},
        "created_at": datetime.now(timezone.utc).isoformat(),
        "results": results,
        "note": "Step-0 reference only. Rubrics are included for later scoring; this workflow does not claim an automatic quality score.",
    }
    out = args.output_dir / "baseline-holdout-100.json"
    out.write_text(json.dumps(diary, ensure_ascii=False, indent=2) + "\\n", encoding="utf-8")
    manifest = {
        "checkpoint": checkpoint_path.name, "checkpoint_sha256": checkpoint_sha,
        "tokenizer_sha256": tokenizer_sha, "holdout_sha256": holdout_sha,
        "holdout_count": len(results), "completed_steps": 0, "seed": SEED,
    }
    (args.output_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\\n", encoding="utf-8"
    )
    print(json.dumps(manifest, indent=2), flush=True)


if __name__ == "__main__":
    main()
