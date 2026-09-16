# Production Readiness Checklist

This checklist is a gate for a real deployment. A completed design document alone is not evidence that these controls exist.

## Scope and Governance

- [ ] Intended use, prohibited use, affected people, and accountable owners are documented.
- [ ] Legal, privacy, security, and domain reviews are complete for the target context.
- [ ] Human review, appeal, override, and incident escalation paths are operational.
- [ ] Model card, dataset cards, risk register, and evaluation report are published or access-controlled appropriately.

## Data and Privacy

- [ ] Data sources are licensed, authorized, classified, and tracked by provenance.
- [ ] Schema validation, retention, deletion, correction, and access-control tests pass.
- [ ] Tenant isolation and authorization filtering are tested with adversarial cases.
- [ ] PII handling, redaction, encryption, backup, and recovery controls are verified.

## Model and Evaluation

- [ ] Model and prompt versions are immutable and reproducible.
- [ ] Quality, groundedness, safety, fairness, robustness, latency, and cost gates pass.
- [ ] Evaluation covers relevant languages, populations, domains, and known failure modes.
- [ ] Independent human review has examined high-risk behavior and limitations.

## Operations and Security

- [ ] Authentication, authorization, rate limiting, secrets management, and audit logging are tested.
- [ ] Dependency, container, infrastructure, and supply-chain scans pass or have documented exceptions.
- [ ] Alerts, dashboards, on-call ownership, incident runbooks, and rollback procedures are exercised.
- [ ] Backup, disaster recovery, regional failover, and data restoration are tested.
- [ ] Load, abuse, prompt-injection, data-exfiltration, and denial-of-service tests are complete.

## Release Decision

- [ ] All exceptions have an owner, expiry date, risk acceptance, and mitigation plan.
- [ ] The release decision is recorded with model, code, data, configuration, and evaluation identifiers.
- [ ] Post-release monitoring and a scheduled re-evaluation date are defined.
