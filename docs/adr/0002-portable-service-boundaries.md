# ADR 0002: Keep Provider-Specific Components Behind Portable Interfaces

- Status: Accepted
- Date: 2026-09-16

## Context

The reference stack includes specific cloud, database, serving, and observability technologies. A public design should teach useful patterns without requiring one vendor, cloud, or deployment model.

## Decision

Define stable interfaces around model serving, retrieval, object storage, identity, evaluation, and telemetry. Treat named products as replaceable implementations. Document portability constraints and capability differences whenever an example depends on a provider-specific feature.

## Trade-offs

Portable interfaces may leave advanced provider features unused or require translation layers. The benefit is a design that can be adapted to open-source, self-hosted, academic, public-sector, and commercial environments.

## Revisit When

Revisit when a capability cannot be represented without leaking provider-specific assumptions or when an interface prevents essential safety, performance, or governance controls.
