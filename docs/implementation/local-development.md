# Local Development Guide

Project Sparkgap does not yet include a runnable implementation. This guide defines the expected local workflow for the v0.1 reference implementation so future code can be added consistently.

## Prerequisites

- Python 3.12 or the version selected by the implementation
- Docker Desktop or an equivalent container runtime
- Git
- a model provider configured through a local environment file
- no production credentials or private data

## Local Services

The initial implementation should run with the smallest practical set of services:

- API service
- embedding and model adapter
- local vector store
- local filesystem or object-store-compatible document directory

A hosted model may be used for local development, but tests must support a deterministic fake or recorded adapter so CI does not require credentials or network access.

## Expected Workflow

1. Copy the eventual `.env.example` to a local, untracked environment file.
2. Start local dependencies with the implementation's documented command.
3. Ingest only the public sample corpus.
4. Run schema validation and unit tests.
5. Start the API and call `/v1/health`.
6. Run the v0.1 evaluation fixtures.
7. Record model, corpus, configuration, and test-report identifiers.

## Local Safety Rules

Never place credentials, personal data, customer documents, or unrestricted model outputs in the repository. Local logs must scrub request content by default. Any example provider endpoint, tenant identifier, or source URL must be clearly non-production.
