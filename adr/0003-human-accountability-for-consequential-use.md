# ADR 0003: Preserve Human Accountability for Consequential Use

- Status: Accepted
- Date: 2026-09-16

## Context

AI outputs can influence decisions about people, access, safety, finances, employment, education, or essential services. Automation can obscure responsibility when affected people cannot understand, challenge, or correct an outcome.

## Decision

The architecture must identify a human accountable party for consequential workflows, provide escalation and override paths, log relevant evidence, and prohibit fully autonomous high-stakes decisions unless a future governance review explicitly establishes acceptable safeguards.

## Trade-offs

Human review adds time, cost, and operational workload. It is retained where the impact of an incorrect or unreviewable decision outweighs the benefit of full automation.

## Revisit When

Revisit only with documented evidence about error rates, recourse, affected communities, monitoring, and the legal and ethical context of the specific use case.
