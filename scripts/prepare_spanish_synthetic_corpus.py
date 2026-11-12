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
PREFERRED_TEXT_FIELDS = (
    "domain", "skill", "difficulty", "language", "prompt", "instruction",
    "question", "input", "problem", "response", "answer", "completion",
    "output", "solution", "explanation", "reasoning", "assumptions",
    "verification", "text", "content",
)
IGNORED_TEXT_FIELDS = {
    "id", "uid", "domain_id", "family_id", "scenario_id", "split", "status",
    "license", "source", "metadata", "tags", "synthetic", "source_id", "dataset",
}
EVAL_PATH = re.compile(
    r"(^|/)(holdout|eval|evaluation|benchmark|benchmarks|test|tests|validation|valid|dev)(/|[-_.])",
    re.I,
)
PAIR_LANGUAGE_KEYS = {"language_pair", "lang_pair", "translation_pair", "pair"}
TARGET_LANGUAGE_KEYS = {
    "target_language", "target_lang", "tgt_lang", "translation_language",
    "output_language", "text_language", "target_locale",
} | PAIR_LANGUAGE_KEYS
LANGUAGE_KEYS = TARGET_LANGUAGE_KEYS | {
    "language", "lang", "locale", "source_language", "source_lang",
    "language_code", "lang_code", "original_language",
}
SPANISH_LANGUAGE = re.compile(
    r"^(?:es|spa|spanish|castellano|español)(?:[-_ (].*)?$", re.I
)
SYNTHETIC_SOURCE_PATH = re.compile(
    r"(?:^|/)(?:generated-curricula|generated-basic-curricula|generated-math-es|"
    r"behavioral-datasets|engineering-lessons-v1|cosmopedia(?:-[^/]*)?|drosophila|minironin-(?:behavior|engineering|identity|performance-engineering|abstention|abstain|aristocrat|casuist|scientist|oracle|error404|lexicon)[^/]*)(?:/|[-_.]|$)",
    re.I,
)
SPANISH_SOURCE_PATH = re.compile(
    r"(?:^|/)(?:"
    r"wikimedia-es|pleias-spanish-pd-books|common-corpus-es|literature-es|ronin-authored-papers|papers|"
    r"boe-legislation-es|bne-hemeroteca-ocr-es|alia-biomedical-es"
    r")(?:/|$)|"
    r"(?:^|/)accepted/(?:"
    r"csic-spanish-scientific-magazines|pharmaconer-es-train|"
    r"spaccc-(?:clinical-cases|token-annotations)-es|wikicat-esv2-train|slr-bench-spanish-v1-all-train|alia-es-cultural-heritage-train|minerva-scientific-es-train"
    r")(?:[./_-]|$)",
    re.I,
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _walk_language_values(value: Any):
    if isinstance(value, dict):
        for child_key, child in value.items():
            normalized_key = str(child_key).strip().casefold().replace("-", "_")
            if normalized_key in LANGUAGE_KEYS:
                if isinstance(child, (str, int, float)):
                    yield normalized_key, str(child).strip()
                elif isinstance(child, list):
                    yield from ((normalized_key, str(item).strip()) for item in child if isinstance(item, (str, int, float)))
            elif isinstance(child, (dict, list)):
                yield from _walk_language_values(child)
    elif isinstance(value, list):
        for item in value:
            if isinstance(item, (dict, list)):
                yield from _walk_language_values(item)

def is_synthetic(record: dict[str, Any]) -> bool:
    value = record.get("synthetic", False)
    if value is True or str(value).strip().casefold() in {"true", "1", "yes"}:
        return True
    source_fields = " ".join(str(record.get(key, "")) for key in ("source_id", "source", "dataset"))
    metadata = record.get("metadata", {})
    if isinstance(metadata, dict):
        source_fields += " " + " ".join(str(metadata.get(key, "")) for key in ("file_name", "filename", "path"))
    return bool(SYNTHETIC_SOURCE_PATH.search(source_fields.replace("\\\\", "/")) )


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
    """Classify the language of the text, preferring target/output language for translations."""
    metadata = record.get("metadata", {})
    pairs = list(_walk_language_values(metadata))
    for key in ("target_language", "target_lang", "tgt_lang", "translation_language",
                "output_language", "text_language", "target_locale", "language_pair", "lang_pair",
                "translation_pair", "pair", "language", "lang", "locale", "language_code",
                "lang_code", "original_language", "source_language", "source_lang"):
        value = record.get(key)
        if value not in (None, ""):
            pairs.append((key, str(value).strip()))

    primary_values = [value for key, value in pairs if key not in TARGET_LANGUAGE_KEYS
                      and key not in {"source_language", "source_lang"}]
    source_values = [value for key, value in pairs if key in {"source_language", "source_lang"}]

    def pair_target(value: str) -> str:
        parts = re.findall(r"[a-zA-ZÀ-ÿ]+", value)
        return parts[-1] if len(parts) >= 2 else value

    target_values = [pair_target(value) if key in PAIR_LANGUAGE_KEYS else value
                     for key, value in pairs if key in TARGET_LANGUAGE_KEYS]

    def classify(values: list[str], reason: str) -> tuple[bool, str] | None:
        normalized = [v.casefold().replace("_", "-").strip() for v in values if v]
        if any(SPANISH_LANGUAGE.match(v) for v in normalized):
            return True, reason
        explicit = [v for v in normalized if v not in {"", "und", "unknown", "zxx", "mul", "n/a", "none"}]
        if explicit:
            return False, "explicit_non_spanish_language"
        return None

    if target_values:
        result = classify(target_values, "metadata_target_language")
        if result is not None:
            return result
    if primary_values:
        result = classify(primary_values, "metadata_language")
        if result is not None:
            return result
    if source_values:
        result = classify(source_values, "metadata_source_language")
        if result is not None:
            return result

    source_fields = " ".join(str(record.get(key, "")) for key in ("source_id", "source", "dataset"))
    if isinstance(metadata, dict):
        source_fields += " " + " ".join(
            str(metadata.get(key, "")) for key in ("file_name", "filename", "path", "source_id")
        )
    if SPANISH_SOURCE_PATH.search(source_fields.replace("\\", "/")):
        return True, "curated_spanish_source_path"
    return False, "language_unverified"

def _leaf_text(value: Any) -> list[str]:
    if isinstance(value, str):
        return [value.strip()] if value.strip() else []
    if isinstance(value, list):
        return [part for item in value for part in _leaf_text(item)]
    if isinstance(value, dict):
        found: list[str] = []
        for key in PREFERRED_TEXT_FIELDS:
            if key in value:
                found.extend(_leaf_text(value[key]))
        if found:
            return found
        for key, child in value.items():
            if str(key).casefold() not in IGNORED_TEXT_FIELDS:
                found.extend(_leaf_text(child))
        return found
    return []


def render_text(record: dict[str, Any]) -> str:
    text = record.get("text", "")
    if isinstance(text, str) and text.strip():
        return " ".join(text.split())
    parts: list[str] = []
    for key in PREFERRED_TEXT_FIELDS:
        if key in record:
            parts.extend(_leaf_text(record[key]))
    if not parts:
        for key, value in record.items():
            if str(key).casefold() not in IGNORED_TEXT_FIELDS:
                parts.extend(_leaf_text(value))
    unique = list(dict.fromkeys(part for part in parts if part))
    return " ".join(" ".join(unique).split())

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
    per_source: dict[str, dict[str, Any]] = {}
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
                    relative_source = source.relative_to(input_root).as_posix()
                    if not record.get("source_id"):
                        record["source_id"] = relative_source
                    if not record.get("dataset"):
                        parent_name = source.parent.name
                        record["dataset"] = source.parent.parent.name if parent_name in {"parts", "shards"} else parent_name
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
                    source_id = str(record.get("source_id") or source.name)
                    per_dataset.setdefault(dataset, Counter())[include_reason] += 1
                    per_dataset[dataset]["included"] += 1
                    source_entry = per_source.setdefault(source_id, {
                        "dataset": dataset,
                        "records_included": 0,
                        "synthetic_included": 0,
                        "spanish_source_included": 0,
                    })
                    source_entry["records_included"] += 1
                    source_entry["synthetic_included" if synthetic else "spanish_source_included"] += 1
            source_hashes.append({
                "path": source.relative_to(input_root).as_posix(),
                "sha256": sha256_file(source),
                **dict(file_counts),
            })

    if counts["records_included"] == 0:
        raise SystemExit("No eligible synthetic or Spanish non-synthetic rows survived")
    if counts["synthetic_included"] == 0:
        raise SystemExit("No synthetic rows were included; refusing an incomplete library projection")
    if counts["spanish_source_included"] == 0:
        raise SystemExit("No verified Spanish non-synthetic rows were included; refusing an incomplete library projection")

    external_manifest_path = input_root / "external-sources.json"
    external_sources = json.loads(external_manifest_path.read_text(encoding="utf-8")) if external_manifest_path.exists() else {"sources": []}
    dataset_notes = {}
    if any("drosophila" in source_id.casefold() for source_id in per_source):
        dataset_notes["drosophila-50k"] = "50,000 procedural synthetic train_candidate rows across 10 domains and 50 task families; not gold, not holdout, and parameterized variants are not 50,000 independent capabilities."

    manifest = {
        "schema": "roninia-spanish-plus-synthetic-corpus-v2",
        "selection_policy_version": 2,
        "selection_policy": "all_synthetic_plus_verified_spanish_non_synthetic_target_language_precedence",
        "source_repository": "orbitalronin94/MINIRONIN",
        "source_run_id": source_run_id,
        "source_artifact": "minironin-unified-train-corpus",
        "source_files": source_hashes,
        "source_files_total": len(source_hashes),
        "external_sources": external_sources.get("sources", []),
        "dataset_notes": dataset_notes,
        "records": dict(counts),
        "datasets": {name: dict(value) for name, value in sorted(per_dataset.items())},
        "sources": {name: value for name, value in sorted(per_source.items())},
        "text_records": counts["records_included"],
        "records_total": counts["records_included"],
        "synthetic_records_included": counts["synthetic_included"],
        "spanish_source_records_included": counts["spanish_source_included"],
        "evaluation_records_excluded": counts["evaluation_excluded"],
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
