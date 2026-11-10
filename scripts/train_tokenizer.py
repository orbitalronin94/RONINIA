#!/usr/bin/env python3
"""Train the fixed RONINIA byte-level BPE tokenizer with visible streaming progress."""
import argparse
import hashlib
import json
import time
from pathlib import Path

from tokenizers import Tokenizer, models, pre_tokenizers, decoders, trainers


def iter_corpus(path: Path, report_every_bytes: int):
    total = path.stat().st_size
    consumed = 0
    records = 0
    last_report = 0
    started = time.monotonic()
    print(f"Tokenizer input: {total:,} bytes ({total / (1024**3):.2f} GiB)", flush=True)
    with path.open("r", encoding="utf-8", errors="replace", buffering=8 * 1024 * 1024) as stream:
        for line in stream:
            records += 1
            consumed += len(line.encode("utf-8"))
            if consumed - last_report >= report_every_bytes:
                elapsed = max(time.monotonic() - started, 0.001)
                rate = consumed / elapsed / (1024**2)
                print(
                    f"Tokenizer ingest: {consumed:,}/{total:,} bytes "
                    f"({100 * consumed / max(total, 1):.1f}%), "
                    f"{records:,} records, {rate:.1f} MiB/s",
                    flush=True,
                )
                last_report = consumed
            yield line
    elapsed = max(time.monotonic() - started, 0.001)
    print(
        f"Tokenizer ingest complete: {consumed:,} bytes, {records:,} records "
        f"in {elapsed / 60:.1f} min. Building BPE merges now...",
        flush=True,
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, type=Path)
    ap.add_argument("--output", required=True, type=Path)
    ap.add_argument("--corpus-manifest", required=True, type=Path)
    ap.add_argument("--vocab-size", type=int, default=16384)
    ap.add_argument("--progress-every-mib", type=int, default=128)
    a = ap.parse_args()
    if a.vocab_size != 16384:
        raise SystemExit("RONIN-10M fixes vocab_size=16384")
    if not a.input.is_file() or a.input.stat().st_size == 0:
        raise SystemExit(f"Missing or empty corpus: {a.input}")
    if not a.corpus_manifest.is_file():
        raise SystemExit(f"Missing corpus manifest: {a.corpus_manifest}")
    if a.progress_every_mib < 1:
        raise SystemExit("--progress-every-mib must be >= 1")

    corpus_manifest = json.loads(a.corpus_manifest.read_text(encoding="utf-8"))
    corpus_sha256 = corpus_manifest.get("corpus_sha256")
    if not corpus_sha256 or a.input.stat().st_size != corpus_manifest.get("text_bytes"):
        raise SystemExit("Corpus file does not match its preparation manifest")

    a.output.mkdir(parents=True, exist_ok=True)
    tok = Tokenizer(models.BPE(unk_token="<|unk|>"))
    tok.pre_tokenizer = pre_tokenizers.ByteLevel(add_prefix_space=False)
    tok.decoder = decoders.ByteLevel()
    trainer = trainers.BpeTrainer(
        vocab_size=16384,
        min_frequency=2,
        special_tokens=["<|unk|>", "<|bos|>", "<|eos|>", "<|pad|>"],
        initial_alphabet=pre_tokenizers.ByteLevel.alphabet(),
        show_progress=True,
    )

    started = time.monotonic()
    tok.train_from_iterator(
        iter_corpus(a.input, a.progress_every_mib * 1024 * 1024),
        trainer=trainer,
    )
    print(f"BPE training completed in {(time.monotonic() - started) / 60:.1f} min", flush=True)

    if tok.get_vocab_size() != 16384:
        raise RuntimeError(f"Expected 16384 tokens, got {tok.get_vocab_size()}")
    dest = a.output / "tokenizer.json"
    tok.save(str(dest))
    digest = hashlib.sha256(dest.read_bytes()).hexdigest()
    manifest = {
        "schema": "roninia-bytelevel-bpe-v1",
        "vocab_size": tok.get_vocab_size(),
        "special_tokens": {
            s: tok.token_to_id(s) for s in ("<|unk|>", "<|bos|>", "<|eos|>", "<|pad|>")
        },
        "tokenizer_sha256": digest,
        "corpus_sha256": corpus_sha256,
        "corpus_bytes": a.input.stat().st_size,
        "source_corpus_run_id": corpus_manifest["source_run_id"],
        "records_total": corpus_manifest["records_total"],
    }
    (a.output / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(manifest, indent=2), flush=True)


if __name__ == "__main__":
    main()
