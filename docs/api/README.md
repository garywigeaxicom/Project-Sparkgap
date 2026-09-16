# API Contracts

The [OpenAPI contract](openapi.yaml) defines the initial v0.1 inference surface. It is intentionally small: health reporting and grounded chat completions.

The contract is normative for the reference implementation. Any implementation that changes request fields, response fields, error codes, authentication requirements, streaming semantics, or citation behavior should update the specification and record a compatibility decision.

Before production use, add:

- complete endpoint coverage, including ingestion, feedback, administration, and model metadata
- OAuth/OIDC scopes and tenant authorization rules
- formal SSE event schemas and connection timeout behavior
- idempotency and retry semantics
- pagination, quotas, deprecation, and backward-compatibility policy
- generated contract tests in CI
