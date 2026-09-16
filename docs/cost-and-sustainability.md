# Cost and Sustainability Worksheet

Use this worksheet when adapting the architecture. Actual costs depend on region, utilization, model size, traffic, retention, and provider pricing.

| Cost area | Assumptions | Estimate | Measurement source |
| --- | --- | --- | --- |
| Inference compute | Requests, tokens, model size, accelerator hours |  |  |
| Training compute | Runs, hardware, duration, interruption rate |  |  |
| Storage | Documents, artifacts, backups, retention |  |  |
| Network and egress | Regions, users, retrieval traffic |  |  |
| Operations | Monitoring, support, incident response |  |  |
| Human review | Volume, review time, specialist rate |  |  |

Record both average and peak usage. Report cost per successful task, not only cost per token, and include the cost of failed, blocked, reviewed, or retried requests.

Sustainability considerations should include accelerator utilization, model size, retraining frequency, storage retention, regional energy mix where known, and whether a smaller model or cached result can meet the same requirement.
