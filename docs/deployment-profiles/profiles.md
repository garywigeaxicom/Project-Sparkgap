# Deployment Profiles

These profiles show how the reference architecture can scale without requiring every component in every environment.

## Learning or Local Profile

- one model endpoint or hosted model API
- lightweight document store and retrieval index
- batch ingestion
- basic request logging with sensitive data controls
- manual evaluation and human review

Use this profile for education, prototypes, and low-risk experiments. Do not use it for consequential decisions without adding appropriate governance and oversight.

## Small Production Profile

- redundant API and orchestration services
- managed relational and object storage
- vector search with backups
- model and prompt versioning
- automated evaluation gates
- structured logs, metrics, alerts, and an incident procedure
- explicit data classification and access control

## Large or High-Risk Profile

- isolated trust zones and tenant-aware authorization
- redundant model serving and regional recovery
- controlled data and model registries
- continuous safety, fairness, drift, and cost monitoring
- formal human-review queues and appeal paths
- documented threat model, audit retention, and recovery exercises

Choose the smallest profile that satisfies the use case's risk, availability, privacy, and scale requirements.
