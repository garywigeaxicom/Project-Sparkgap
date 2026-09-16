# Portability and Interoperability

The reference architecture separates capabilities from products. Implementations should preserve these contracts even when components change.

| Capability | Portable contract | Example implementations |
| --- | --- | --- |
| Model serving | OpenAI-compatible or documented generation API with health and usage metadata | vLLM, TGI, hosted provider |
| Retrieval | Query, filter, rank, provenance, and deletion semantics | Qdrant, PostgreSQL extensions, managed vector service |
| Object storage | Versioned objects, lifecycle rules, encryption, and access policy | S3-compatible storage, cloud object stores |
| Evaluation | Versioned datasets, repeatable runners, metrics, and reports | Custom harness, EleutherAI harness, managed evaluation tools |
| Observability | Metrics, logs, traces, correlation IDs, and retention policy | Prometheus, OpenTelemetry, vendor platforms |
| Identity | Authentication, authorization, tenant isolation, and audit events | OAuth/OIDC, cloud IAM, enterprise identity provider |

Document any provider-specific behavior, cost, data residency, lock-in, or feature loss when replacing an implementation.
