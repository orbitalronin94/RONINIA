#!/usr/bin/env python3
"""Build a train-only RONINIA corpus: every synthetic row plus Spanish source rows.

The source MINIRONIN artifact is immutable and checksum-verified upstream. This
projection is deterministic, streaming, and deliberately excludes evaluation
rows before applying the language policy.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

EVAL_SPLITS = {"test", "tests", "eval", "evaluation", "benchmark", "benchmarks",
               "validation", "valid", "dev", "holdout"}
EVAL_PATH = re.compile(
    r"(^|/)(holdout|eval|evaluation|benchmark|benchmarks|test|tests|validation|valid|dev)(/|[-_.])",
    re.I,
)
LANGUAGE_KEYS = {
    "language", "lang", "locale", "source_language", "source_lang",
    "language_code", "lang_code", "original_language",
}
SPANISH_LANGUAGE = re.compile(
    r"^(?:es|spa|spanish|castellano|español)(?:[-_ (].*)?$", re.I
)
SPANISH_SOURCE_PATH = re.compile(
    r"(?:^|/)(?:"
    r"wikimedia-es|pleias-spanish-pd-books|common-corpus-es|"
    r"boe-legislation-es|bne-hemeroteca-ocr-es|alia-biomedical-es"
    r")(?:/|$)|"
    r"(?:^|/)accepted/(?:"
    r"csic-spanish-scientific-magazines|pharmaconer-es-train|"
    r"spaccc-(?:clinical-cases|token-annotations)-es|wikicat-esv2-train"
    r")(?:[./_-]|$)",
    re.I,
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _walk_language_values(value: Any, key: str = ""):
    if isinstance(value, dict):
        for child_key, child in value.items():
            normalized_key = str(child_key).strip().casefold().replace("-", "_")
            if normalized_key in LANGUAGE_KEYS:
                if isinstance(child, (str, int, float)):
                    yield str(child).strip()
                elif isinstance(child, list):
                    yield from (str(item).strip() for item in child if isinstance(item, (str, int, float)))
            elif isinstance(child, (dict, list)):
                yield from _walk_language_values(child, normalized_key)
    elif isinstance(value, list):
        for item in value:
            if isinstance(item, (dict, list)):
                yield from _walk_language_values(item, key)


def is_synthetic(record: dict[str, Any]) -> bool:
    value = record.get("synthetic", False)
    return value is True or str(value).strip().casefold() in {"true", "1", "yes"}


def is_evaluation(record: dict[str, Any]) -> bool:
    source_id = str(record.get("source_id", ""))
    if EVAL_PATH.search(source_id.replace("\\", "/")):
        return True
    metadata = record.get("metadata", {})
    if isinstance(metadata, dict):
        for key in ("split", "partition", "subset", "usage", "purpose", "set"):
            value = metadata.get(key)
            if isinstance(value, str) and value.strip().casefold() in EVAL_SPLITS:
                return True
    return False


def spanish_decision(record: dict[str, Any]) -> tuple[bool, str]:
    """Return (is Spanish, reason); explicit non-Spanish metadata beats path hints."""
    metadata = record.get("metadata", {})
    values = list(_walk_language_values(metadata))
    values.extend(
        str(record.get(key, "")).strip()
        for key in ("language", "lang", "locale", "source_language")
        if record.get(key) not in (None, "")
    )
    normalized = [v.casefold().replace("_", "-").strip() for v in values if v]
    if any(SPANISH_LANGUAGE.match(v) for v in normalized):
        return True, "metadata_language"
    explicit = [v for v in normalized if v not in {"", "und", "unknown", "zxx", "mul", "n/a", "none"}]
    if explicit:
        return False, "explicit_non_spanish_language"

    source_fields = " ".join(
        str(record.get(key, "")) for key in ("source_id", "source", "dataset")
    )
    if isinstance(metadata, dict):
        source_fields += " " + " ".join(
            str(metadata.get(key, "")) for key in ("file_name", "filename", "path", "source_id")
        )
    if SPANISH_SOURCE_PATH.search(source_fields.replace("\\", "/")):
        return True, "curated_spanish_source_path"
    return False, "language_unverified"


def render_text(record: dict[str, Any]) -> str:
    text = record.get("text", "")
    if isinstance(text, str) and text.strip():
        return " ".join(text.split())
    question = record.get("question") or record.get("prompt") or record.get("input")
    answer = record.get("answer") or record.get("target") or record.get("completion")
    if question is not None and answer is not None:
        return " ".join(f"Pregunta: {question}\nRespuesta: {answer}".split())
    return ""


def prepare(input_root: Path, output: Path, manifest_path: Path, source_run_id: int) -> dict[str, Any]:
    sources = sorted(
        path for path in input_root.rglob("*")
        if path.is_file() and path.name.endswith((".jsonl.gz", ".jsonl", ".ndjson.gz", ".ndjson"))
    )
    if not sources:
        raise SystemExit(f"No unified JSONL corpus files found under {input_root}")

    output.parent.mkdir(parents=True, exist_ok=True)
    counts = Counter()
    per_dataset: dict[str, Counter] = {}
    corpus_hash = hashlib.sha256()
    source_hashes = []
    total_bytes = 0

    with output.open("w", encoding="utf-8", newline="\n") as target:
        for source in sources:
            opener = gzip.open if source.name.endswith(".gz") else open
            file_counts = Counter()
            with opener(source, "rt", encoding="utf-8", errors="replace") as stream:
                for line_number, line in enumerate(stream, 1):
                    if not line.strip():
                        continue
                    try:
                        record = json.loads(line)
                    except json.JSONDecodeError:
                        counts["malformed_json_rows"] += 1
                        continue
                    if not isinstance(record, dict):
                        counts["non_object_rows"] += 1
                        continue
                    counts["records_seen"] += 1
                    if is_evaluation(record):
                        counts["evaluation_excluded"] += 1
                        file_counts["evaluation_excluded"] += 1
                        continue

                    synthetic = is_synthetic(record)
                    if synthetic:
                        include_reason = "synthetic"
                    else:
                        spanish, reason = spanish_decision(record)
                        if not spanish:
                            counts["non_synthetic_excluded"] += 1
                            counts[reason] += 1
                            file_counts[reason] += 1
                            continue
                        include_reason = reason

                    text = render_text(record)
                    if not text:
                        counts["empty_text_excluded"] += 1
                        file_counts["empty_text_excluded"] += 1
                        continue

                    payload = (text + "\n").encode("utf-8")
                    target.write(payload.decode("utf-8"))
                    corpus_hash.update(payload)
                    total_bytes += len(payload)
                    counts["records_included"] += 1
                    counts["synthetic_included" if synthetic else "spanish_source_included"] += 1
                    file_counts["records_included"] += 1
                    file_counts["synthetic_included" if synthetic else "spanish_source_included"] += 1
                    dataset = str(record.get("dataset") or Path(str(record.get("source_id", source.name))).name)
                    per_dataset.setdefault(dataset, Counter())[include_reason] += 1
                    per_dataset[dataset]["included"] += 1
            source_hashes.append({
                "path": source.name,
                "sha256": sha256_file(source),
                **dict(file_counts),
            })

    if counts["records_included"] == 0:
        raise SystemExit("No eligible synthetic or Spanish non-synthetic rows survived")
    if counts["synthetic_included"] == 0:
        raise SystemExit("No synthetic rows were included; refusing an incomplete library projection")
    if counts["spanish_source_included"] == 0:
        raise SystemExit("No verified Spanish non-synthetic rows were included; refusing an incomplete library projection")

    manifest = {
        "schema": "roninia-spanish-plus-synthetic-corpus-v1",
        "selection_policy": "include_all_synthetic_plus_non_synthetic_verified_spanish",
        "source_repository": "orbitalronin94/MINIRONIN",
        "source_run_id": source_run_id,
        "source_artifact": "minironin-unified-train-corpus",
        "source_files": source_hashes,
        "source_files_total": len(source_hashes),
        "records": dict(counts),
        "datasets": {name: dict(value) for name, value in sorted(per_dataset.items())},
        "text_records": counts["records_included"],
        "text_bytes": total_bytes,
        "corpus_sha256": corpus_hash.hexdigest(),
        "language_policy": {
            "synthetic": "included regardless of language, retaining upstream synthetic label in this manifest",
            "non_synthetic": "included only with Spanish language metadata or a curated Spanish source path",
            "unknown_language": "excluded and counted; no guess from text content",
            "evaluation": "excluded before all other selection rules",
        },
        "excluded_non_synthetic_non_spanish": counts["explicit_non_spanish_language"],
        "excluded_non_synthetic_unverified_language": counts["language_unverified"],
    }
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--source-run-id", type=int, required=True)
    args = parser.parse_args()
    manifest = prepare(args.input_root, args.output, args.manifest, args.source_run_id)
    print(json.dumps({
        "source_run_id": manifest["source_run_id"],
        "records": manifest["records"],
        "datasets_total": len(manifest["datasets"]),
        "text_bytes": manifest["text_bytes"],
        "corpus_sha256": manifest["corpus_sha256"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
