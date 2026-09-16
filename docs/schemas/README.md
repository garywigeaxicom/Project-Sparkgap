# Data Contracts

The JSON Schemas in this directory turn the examples in [DESIGN.md](../../DESIGN.md) into versioned validation targets.

- `training-record.schema.json`: supervised fine-tuning records
- `user-event.schema.json`: interaction and feedback events
- `embedding-record.schema.json`: indexed knowledge chunks and provenance

Implementations should validate records before persistence or publication, reject unknown fields unless a compatibility policy allows them, and test backward- and forward-compatibility before changing a schema. A production implementation should register these schemas in its chosen registry and add deletion, retention, and access-control tests.
