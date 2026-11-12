#!/usr/bin/env python3
"""Tokenize a prepared train-only corpus once and emit a hash-bound uint16 cache."""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from tokenizers import Tokenizer


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--corpus", type=Path, required=True)
    ap.add_argument("--tokenizer", type=Path, required=True)
    ap.add_argument("--corpus-manifest", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--manifest", type=Path, required=True)
    args = ap.parse_args()

    corpus_info = json.loads(args.corpus_manifest.read_text(encoding="utf-8"))
    corpus_sha = sha256(args.corpus)
    if corpus_sha != corpus_info.get("corpus_sha256"):
        raise SystemExit("prepared corpus SHA-256 does not match its manifest")
    tokenizer_sha = sha256(args.tokenizer)
    tokenizer = Tokenizer.from_file(str(args.tokenizer))
    vocab_size = tokenizer.get_vocab_size()
    if vocab_size > 65536:
        raise SystemExit("uint16 token cache cannot represent this vocabulary")
    eos_id = tokenizer.token_to_id("<|eos|>")
    if eos_id is None:
        raise SystemExit("tokenizer is missing <|eos|>")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    token_count = 0
    with args.output.open("wb") as binary, args.corpus.open(encoding="utf-8") as source:
        for line_number, line in enumerate(source, 1):
            line = line.strip()
            if not line:
                continue
            ids = tokenizer.encode(line).ids
            if ids:
                np.asarray(ids + [eos_id], dtype=np.uint16).tofile(binary)
                token_count += len(ids) + 1
            if line_number % 100000 == 0:
                print(json.dumps({"lines": line_number, "tokens": token_count}), flush=True)

    if token_count == 0:
        raise SystemExit("tokenization produced no tokens")
    result = {
        "schema": "roninia-token-cache-v1",
        "dtype": "uint16",
        "token_count": token_count,
        "vocab_size": vocab_size,
        "tokens_bytes": args.output.stat().st_size,
        "tokens_sha256": sha256(args.output),
        "corpus_sha256": corpus_sha,
        "corpus_bytes": args.corpus.stat().st_size,
        "source_run_id": corpus_info["source_run_id"],
        "corpus_manifest_sha256": sha256(args.corpus_manifest),
        "tokenizer_sha256": tokenizer_sha,
        "tokenizer_vocab_size": vocab_size,
        "evaluation_records_excluded": corpus_info["evaluation_records_excluded"],
        "selection_policy": corpus_info.get("selection_policy"),
        "records_total": corpus_info.get("records_total"),
        "synthetic_records_included": corpus_info.get("synthetic_records_included"),
        "spanish_source_records_included": corpus_info.get("spanish_source_records_included"),
        "excluded_non_synthetic_non_spanish": corpus_info.get("excluded_non_synthetic_non_spanish"),
        "excluded_non_synthetic_unverified_language": corpus_info.get("excluded_non_synthetic_unverified_language"),
    }
    args.manifest.parent.mkdir(parents=True, exist_ok=True)
    args.manifest.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2), flush=True)


if __name__ == "__main__":
    main()
