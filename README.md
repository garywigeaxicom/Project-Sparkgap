# Project Sparkgap

Project Sparkgap is a public, reusable reference architecture for designing trustworthy AI systems. It exists to make high-level AI engineering knowledge easier to understand, review, adapt, and share.

The project is documentation-first. Its primary artifact is a detailed master design document covering the architecture and operating practices behind a production AI platform.

## Start Here

Read the [AI Master Design Document](DESIGN.md) for the complete specification.

The document includes:

- public design principles and project scope
- a plain-language system summary
- a minimum viable blueprint for smaller teams
- layered system architecture and technology choices
- data ingestion, governance, quality, and storage
- model selection, embeddings, prompting, and RAG
- training, fine-tuning, evaluation, and experiment tracking
- inference, scaling, caching, and API design
- safety, fairness, red-teaming, auditability, and human review
- deployment, observability, disaster recovery, and risk management
- contribution, review, versioning, and change-management guidance
- architecture diagrams, decision records, evaluation templates, and deployment profiles
- portability, cost, sustainability, accessibility, and inclusion guidance
- executable API and data contracts for a future reference implementation
- a bounded v0.1 implementation plan and production-readiness gate

## Who This Is For

This project is intended for:

- ML, data, platform, and software engineers
- technical leads and architects
- students and independent practitioners
- civic technologists and public-interest organizations
- teams evaluating how to build or govern AI systems

You do not need to adopt the entire architecture. Treat it as a set of documented patterns and trade-offs that can be simplified, replaced, or extended for a different context.

## Current Status

The repository now includes a bounded v0.1 reference implementation. It is intentionally local and dependency-light: it supports Markdown/text ingestion, deterministic lexical retrieval, a configurable OpenAI-compatible model adapter, a safe fallback model, safety checks, structured events, and the documented API. It is not production-ready and does not include production secrets, private data, multi-region infrastructure, or GPU deployment.

## Run the Reference Slice

```powershell
python -m pip install -e ".[test]"
sparkgap-ingest ingest
uvicorn sparkgap.app:app --reload
```

Then open `http://127.0.0.1:8000/docs` or call `GET /v1/health`. The default fallback model uses retrieved excerpts and requires no model credentials. Configure `SPARKGAP_MODEL_BASE_URL` and `SPARKGAP_MODEL_API_KEY` to use an OpenAI-compatible model endpoint.

## Repository Guide

- [CONTRIBUTING.md](CONTRIBUTING.md): contribution and review expectations
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md): community standards
- [SECURITY.md](SECURITY.md): security reporting and scope
- [CHANGELOG.md](CHANGELOG.md): project history
- [docs/adr/](docs/adr/): durable architecture decisions and trade-offs
- [docs/diagrams/](docs/diagrams/): Mermaid source diagrams
- [docs/evaluation/](docs/evaluation/): evaluation plan template
- [docs/model-cards/](docs/model-cards/): model documentation template
- [docs/dataset-cards/](docs/dataset-cards/): dataset documentation template
- [docs/deployment-profiles/](docs/deployment-profiles/): adaptation profiles by scale and risk
- [docs/portability.md](docs/portability.md): capability contracts and replaceable implementations
- [docs/cost-and-sustainability.md](docs/cost-and-sustainability.md): cost and sustainability worksheet
- [docs/accessibility-and-inclusion.md](docs/accessibility-and-inclusion.md): inclusion requirements
- [docs/api/](docs/api/): versioned OpenAPI contract and API guidance
- [docs/schemas/](docs/schemas/): versioned JSON data contracts
- [docs/implementation/](docs/implementation/): v0.1 scope and local-development guidance
- [docs/evaluation/fixtures/](docs/evaluation/fixtures/): public regression cases
- [docs/production-readiness-checklist.md](docs/production-readiness-checklist.md): deployment release gate
- `src/sparkgap/`: v0.1 Python package
- `tests/`: implementation and API tests
- `examples/corpus/`: public sample documents for local evaluation
- [pyproject.toml](pyproject.toml): dependencies, test configuration, and CLI entry point

## Contributing

Contributions are welcome when they improve clarity, technical rigor, safety, accessibility, or adaptability.

Before proposing a change:

1. Read [DESIGN.md](DESIGN.md), especially the public contribution and review model.
2. Explain the problem, proposed change, rationale, and relevant trade-offs.
3. Keep architectural claims precise and distinguish examples from requirements.
4. Consider safety, privacy, governance, operational cost, and accessibility.
5. Update the document's version or changelog when the change is material.

Use pull requests or an equivalent review workflow for proposed changes. Discussion and constructive critique are part of the project, especially where reasonable design alternatives exist.

## License

This project is licensed under the [Apache License 2.0](LICENSE).
