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
    assert manifest["schema"] == "roninia-spanish-plus-synthetic-corpus-v2"
    assert manifest["selection_policy_version"] == 2
    assert manifest["records"]["synthetic_included"] == 1
    assert manifest["records"]["spanish_source_included"] == 1
    assert manifest["records"]["evaluation_excluded"] == 1
    assert manifest["sources"]["data/synth/generated.jsonl"]["synthetic_included"] == 1
    assert manifest["sources"]["data/curated/accepted/pharmaconer-es-train.jsonl"]["spanish_source_included"] == 1
    assert manifest["records"]["explicit_non_spanish_language"] == 1



def test_translation_uses_target_language_not_source_language():
    target_spanish = row(metadata={"source_language": "en", "target_language": "es"})
    target_english = row(metadata={"source_language": "es", "target_language": "en"})
    assert spanish_decision(target_spanish) == (True, "metadata_target_language")
    assert spanish_decision(target_english) == (False, "explicit_non_spanish_language")


def test_admitted_spanish_literature_and_papers_paths_are_included():
    literature = row(source_id="data/inherited/heretic-corpus/literature-es/train.txt", metadata={})
    papers = row(source_id="data/inherited/heretic-corpus/ronin-authored-papers/article.md", metadata={})
    assert spanish_decision(literature) == (True, "curated_spanish_source_path")
    assert spanish_decision(papers) == (True, "curated_spanish_source_path")


def test_known_synthetic_source_paths_are_kept_even_without_row_flag():
    cosmopedia = row(source_id="data/inherited/heretic-corpus/cosmopedia-v0.1/train.jsonl", synthetic=False)
    drosophila = row(source_id="data/drosophila/parts/01_matematicas_5000.jsonl", synthetic=False)
    assert is_synthetic(cosmopedia)
    assert is_synthetic(drosophila)


def test_translation_uses_target_language_not_source_language():
    target_spanish = row(metadata={"source_language": "en", "target_language": "es"})
    target_english = row(metadata={"source_language": "es", "target_language": "en"})
    assert spanish_decision(target_spanish) == (True, "metadata_target_language")
    assert spanish_decision(target_english) == (False, "explicit_non_spanish_language")


def test_translation_language_pair_uses_target_side():
    assert spanish_decision(row(metadata={"language_pair": "en-es", "source_language": "en"})) == (True, "metadata_target_language")
    assert spanish_decision(row(metadata={"language_pair": "es-en", "source_language": "es"})) == (False, "explicit_non_spanish_language")


def test_engineering_lessons_source_is_synthetic():
    record = row(source_id="data/curated/engineering-lessons-v1/train.jsonl", synthetic=False)
    assert is_synthetic(record)


def test_structured_drosophila_candidate_is_rendered_and_classified_synthetic():
    from prepare_spanish_synthetic_corpus import render_text
    record = {
        "id": "01301", "domain": "matemáticas", "skill": "aritmética",
        "difficulty": "introductory", "prompt": "Calcula 2 + 2.",
        "answer": "4", "status": "train_candidate", "synthetic": False,
        "source_id": "drosophila/parts/01_matematicas_5000.jsonl",
    }
    assert is_synthetic(record)
    rendered = render_text(record)
    assert "Calcula 2 + 2." in rendered and "4" in rendered
    assert "01301" not in rendered and "train_candidate" not in rendered


def test_external_synthetic_source_and_candidate_caveat_are_recorded(tmp_path: Path):
    source = tmp_path / "source"
    (source / "drosophila" / "parts").mkdir(parents=True)
    (source / "external-sources.json").write_text(json.dumps({"sources": [{"repository": "orbitalronin94/HERETIC-RONIN", "commit": "pinned"}]}), encoding="utf-8")
    with gzip.open(source / "train.jsonl.gz", "wt", encoding="utf-8") as stream:
        stream.write(json.dumps(row(source_id="data/curated/accepted/pharmaconer-es-train.jsonl", metadata={}, text="Contenido castellano admitido."), ensure_ascii=False) + "\n")
    drosophila = source / "drosophila" / "parts" / "01_matematicas_5000.jsonl"
    drosophila.write_text(json.dumps({"id": "01301", "domain": "matemáticas", "prompt": "Calcula 2 + 2.", "answer": "4", "status": "train_candidate"}) + "\n", encoding="utf-8")
    manifest = prepare(source, tmp_path / "train.txt", tmp_path / "manifest.json", 123)
    assert manifest["records"]["synthetic_included"] == 1
    assert manifest["external_sources"][0]["repository"] == "orbitalronin94/HERETIC-RONIN"
    assert "not gold" in manifest["dataset_notes"]["drosophila-50k"]
    assert manifest["sources"]["drosophila/parts/01_matematicas_5000.jsonl"]["dataset"] == "drosophila"
