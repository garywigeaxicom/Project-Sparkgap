from __future__ import annotations

import re
from dataclasses import dataclass

from .ingestion import Chunk


@dataclass(frozen=True)
class SearchResult:
    chunk: Chunk
    score: float


def _terms(text: str) -> set[str]:
    return {term for term in re.findall(r"[a-z0-9]{2,}", text.lower())}


def search(chunks: list[Chunk], query: str, limit: int = 4) -> list[SearchResult]:
    query_terms = _terms(query)
    if not query_terms:
        return []
    scored: list[SearchResult] = []
    for chunk in chunks:
        chunk_terms = _terms(chunk.text)
        overlap = query_terms & chunk_terms
        if overlap:
            score = len(overlap) / len(query_terms)
            scored.append(SearchResult(chunk=chunk, score=round(score, 4)))
    return sorted(scored, key=lambda result: (-result.score, result.chunk.chunk_id))[:limit]
