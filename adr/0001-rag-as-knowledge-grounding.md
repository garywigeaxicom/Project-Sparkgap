# ADR 0001: Use Retrieval-Augmented Generation for Knowledge Grounding

- Status: Accepted
- Date: 2026-09-16

## Context

A general-purpose language model may have stale, incomplete, or unsupported knowledge. The reference architecture needs a way to incorporate domain documents while preserving source traceability and allowing knowledge updates without retraining the base model.

## Decision

Use retrieval-augmented generation (RAG) as the default knowledge-grounding pattern. Retrieve authorized, relevant sources at request time, include source metadata in the model context, and expose citations or provenance where the product experience allows it.

## Trade-offs

RAG improves updateability and provenance but introduces retrieval quality, authorization, latency, indexing, and prompt-injection risks. Fine-tuning remains appropriate for behavior and task adaptation, not as the primary mechanism for frequently changing factual knowledge.

## Revisit When

Revisit this decision if retrieval quality cannot meet the target task requirements, if a workload has no stable external knowledge source, or if a smaller task-specific model provides better quality, cost, and safety with equivalent traceability.
