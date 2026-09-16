from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass(frozen=True)
class Chunk:
    document_id: str
    chunk_id: str
    title: str
    text: str
    url: str | None = None
    sensitivity_class: str = "Public"


def document_id(path: Path, text: str) -> str:
    digest = hashlib.sha256((path.name + "\0" + text).encode("utf-8")).hexdigest()[:16]
    return f"doc_{digest}"


def chunk_text(text: str, size: int = 800, overlap: int = 100) -> list[str]:
    words = text.split()
    if not words:
        return []
    if overlap >= size:
        raise ValueError("overlap must be smaller than size")
    chunks: list[str] = []
    step = size - overlap
    for start in range(0, len(words), step):
        chunk = " ".join(words[start : start + size])
        if chunk:
            chunks.append(chunk)
        if start + size >= len(words):
            break
    return chunks


def ingest_directory(directory: Path, output_path: Path) -> list[Chunk]:
    chunks: list[Chunk] = []
    for path in sorted(directory.rglob("*.md")) + sorted(directory.rglob("*.txt")):
        text = path.read_text(encoding="utf-8")
        doc_id = document_id(path, text)
        title = next((line.lstrip("# ").strip() for line in text.splitlines() if line.strip()), path.stem)
        for index, part in enumerate(chunk_text(text)):
            chunks.append(
                Chunk(
                    document_id=doc_id,
                    chunk_id=f"{doc_id}_chunk_{index}",
                    title=title,
                    text=part,
                )
            )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps([asdict(chunk) for chunk in chunks], indent=2), encoding="utf-8")
    return chunks


def load_index(path: Path) -> list[Chunk]:
    if not path.exists():
        return []
    records = json.loads(path.read_text(encoding="utf-8"))
    return [Chunk(**record) for record in records]
