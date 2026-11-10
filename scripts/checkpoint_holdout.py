#!/usr/bin/env python3
"""Run the immutable 100-question inference holdout against a trained RONIN-10M checkpoint."""
import argparse, hashlib, json, random, sys, time
from datetime import datetime, timezone
from pathlib import Path
import numpy as np
import torch
from tokenizers import Tokenizer

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
    ap.add_argument("--checkpoint", type=Path, required=True)
    ap.add_argument("--tokenizer", type=Path, required=True)
    ap.add_argument("--holdout", type=Path, required=True)
    ap.add_argument("--output-dir", type=Path, required=True)
    ap.add_argument("--expected-steps", type=int, default=5000)\n    ap.add_argument("--threads", type=int, default=2)
    ap.add_argument("--max-new-tokens", type=int, default=32)
    ap.add_argument("--max-new-bytes", type=int, default=128)
    args = ap.parse_args()
    if args.threads < 1 or not 1 <= args.max_new_tokens <= 128 or args.max_new_bytes < 1:
        raise SystemExit("invalid generation limits")

    torch.set_num_threads(args.threads)
    torch.use_deterministic_algorithms(True)
    random.seed(SEED); np.random.seed(SEED); torch.manual_seed(SEED)

    payload = torch.load(args.checkpoint, map_location="cpu", weights_only=False)
    completed_steps = int(payload.get("completed_steps", -1))
    if completed_steps != args.expected_steps:
        raise SystemExit(f"expected checkpoint at {args.expected_steps} steps, got {completed_steps}")
    config = ModelConfig(**payload["config"])
    config.validate()
    tokenizer = Tokenizer.from_file(str(args.tokenizer))
    eos_id = tokenizer.token_to_id("<|eos|>")
    if eos_id is None or tokenizer.get_vocab_size() != config.vocab_size:
        raise SystemExit("tokenizer special tokens or vocabulary do not match model config")
    tokenizer_sha = sha256(args.tokenizer)
    if payload.get("tokenizer_sha256") != tokenizer_sha:
        raise SystemExit("checkpoint tokenizer SHA-256 does not match downloaded tokenizer")

    model = RoninLM(config).cpu()
    model.load_state_dict(payload["model_state_dict"], strict=True)
    model.eval()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    checkpoint_sha = sha256(args.checkpoint)
    rows = load_holdout(args.holdout)
    results = []
    instruction = (
        "Responde en castellano. Si no sabes algo, dilo claramente. "
        "No inventes datos ni afirmes como cierto lo que no puedas justificar."
    )
    with torch.inference_mode():
        for index, row in enumerate(rows, 1):
            prompt = instruction + "\n\n" + row["question"].strip() + "\nRespuesta:"
            ids = tokenizer.encode(prompt).ids
            if not ids:
                raise ValueError(f"{row['id']}: empty prompt encoding")
            generated, generated_bytes = [], 0
            started = time.perf_counter()
            for _ in range(args.max_new_tokens):
                input_ids = torch.tensor([ids[-config.context_length:]], dtype=torch.long)
                logits, _ = model(input_ids)
                next_id = int(torch.argmax(logits[0, -1]).item())
                if next_id == eos_id:
                    break
                piece_bytes = tokenizer.decode([next_id], skip_special_tokens=True).encode("utf-8")
                if generated_bytes + len(piece_bytes) > args.max_new_bytes:
                    break
                generated.append(next_id); ids.append(next_id)
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
        "label": f"RONIN-10M-checkpoint-{completed_steps}",
        "completed_steps": completed_steps,
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
        "note": f"Checkpoint {completed_steps} comparison. Rubrics included; no automatic quality score is claimed.",
    }
    out = args.output_dir / f"checkpoint-{completed_steps}-holdout-100.json"
    out.write_text(json.dumps(diary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    manifest = {
        "checkpoint": args.checkpoint.name, "checkpoint_sha256": checkpoint_sha,
        "completed_steps": completed_steps, "parameter_count": model.parameter_count(),
        "tokenizer_sha256": tokenizer_sha, "holdout_sha256": holdout_sha,
        "holdout_count": len(results), "config": config.__dict__,
    }
    (args.output_dir / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, indent=2), flush=True)

if __name__ == "__main__":
    main()
