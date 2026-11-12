import gzip
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from prepare_spanish_synthetic_corpus import is_evaluation, is_synthetic, spanish_decision, prepare


def row(**kwargs):
    base = {"source_id": "data/elsewhere/file.jsonl", "dataset": "file.jsonl",
            "synthetic": False, "text": "Texto de prueba suficientemente largo."}
    base.update(kwargs)
    return base


def test_synthetic_included_regardless_of_language():
    ok, reason = spanish_decision(row(metadata={"language": "en"}))
    assert not ok and reason == "explicit_non_spanish_language"
    assert is_synthetic(row(synthetic=True, metadata={"language": "en"}))


def test_explicit_spanish_metadata_is_accepted():
    assert spanish_decision(row(metadata={"language": "es-ES"}))[0]


def test_curated_spanish_path_is_fallback_for_unknown_metadata():
    record = row(source_id="data/inherited/common-corpus-es/shard.jsonl.gz",
                 metadata={"language": "und"})
    assert spanish_decision(record) == (True, "curated_spanish_source_path")


def test_explicit_non_spanish_overrides_spanish_path():
    record = row(source_id="data/inherited/common-corpus-es/shard.jsonl.gz",
                 metadata={"language": "en"})
    assert spanish_decision(record) == (False, "explicit_non_spanish_language")


def test_unknown_non_synthetic_is_excluded():
    assert spanish_decision(row(metadata={})) == (False, "language_unverified")


def test_evaluation_rows_are_excluded():
    assert is_evaluation(row(source_id="data/benchmarks/train.jsonl"))
    assert is_evaluation(row(metadata={"split": "validation"}))


def test_streaming_projection_keeps_synthetic_and_spanish_only(tmp_path: Path):
    source = tmp_path / "source"
    source.mkdir()
    rows = [
        row(source_id="data/synth/generated.jsonl", dataset="synthetic.jsonl",
            synthetic=True, metadata={"language": "en"}, text="Synthetic content kept."),
        row(source_id="data/curated/accepted/pharmaconer-es-train.jsonl",
            dataset="pharmaconer-es-train.jsonl", metadata={}, text="Contenido español admitido."),
        row(source_id="data/elsewhere/english.jsonl", dataset="english.jsonl",
            metadata={"language": "en"}, text="English content must be excluded."),
        row(source_id="data/benchmarks/test.jsonl", dataset="test.jsonl",
            synthetic=True, metadata={}, text="Evaluation synthetic excluded."),
    ]
    with gzip.open(source / "train.jsonl.gz", "wt", encoding="utf-8") as stream:
        for item in rows:
            stream.write(json.dumps(item, ensure_ascii=False) + "\n")
    output = tmp_path / "train.txt"
    manifest_path = tmp_path / "manifest.json"
    manifest = prepare(source, output, manifest_path, 123)
    lines = output.read_text(encoding="utf-8").splitlines()
    assert lines == ["Synthetic content kept.", "Contenido español admitido."]
    assert manifest["records"]["synthetic_included"] == 1
    assert manifest["records"]["spanish_source_included"] == 1
    assert manifest["records"]["evaluation_excluded"] == 1
    assert manifest["records"]["explicit_non_spanish_language"] == 1



def test_translation_uses_target_language_not_source_language():
    target_spanish = row(metadata={"source_language": "en", "target_language": "es"})
    target_english = row(metadata={"source_language": "es", "target_language": "en"})
    assert spanish_decision(target_spanish) == (True, "metadata_target_language")
    assert spanish_decision(target_english) == (False, "explicit_non_spanish_language")
