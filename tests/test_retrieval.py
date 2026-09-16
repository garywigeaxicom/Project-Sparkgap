from sparkgap.ingestion import Chunk
from sparkgap.retrieval import search


def test_retrieval_ranks_matching_chunks() -> None:
    chunks = [
        Chunk("doc_a", "chunk_a", "Policy", "Human review is required for high-impact decisions."),
        Chunk("doc_b", "chunk_b", "Other", "The system uses public architecture documents."),
    ]
    results = search(chunks, "high-impact human review")
    assert results[0].chunk.chunk_id == "chunk_a"
    assert results[0].score > 0
