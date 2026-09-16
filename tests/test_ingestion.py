from pathlib import Path

from sparkgap.ingestion import chunk_text, ingest_directory


def test_chunking_is_deterministic() -> None:
    text = "one two three four five six seven eight"
    assert chunk_text(text, size=4, overlap=1) == [
        "one two three four",
        "four five six seven",
        "seven eight",
    ]


def test_ingest_writes_stable_index(tmp_path: Path) -> None:
    source = tmp_path / "corpus"
    source.mkdir()
    (source / "doc.md").write_text("# Title\n\nA public document.", encoding="utf-8")
    first = ingest_directory(source, tmp_path / "one.json")
    second = ingest_directory(source, tmp_path / "two.json")
    assert first == second
    assert first[0].document_id.startswith("doc_")
