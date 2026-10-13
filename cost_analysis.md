# AfyaPlus FinOps Cost Management Forecast

### System Transaction Cost Models
Our token tracking model estimates costs for text triage routing processing across baseline workloads (100,000 monthly transactions) up to a 10x surge scenario (1,000,000 monthly transactions), based on fixed `gpt-4o-mini` snapshot rates verified on 2026-10-11.

| Workload Volume Scenario | Token Processing Cost | Dedicated System Infra Floor | Total FinOps Allocated Target |
| :--- | :--- | :--- | :--- |
| **Baseline (100k requests)** | \$17.90 | \$520.00 | **\$5.3790 per 1k requests** |
| **Surge Scale (1M requests)** | \$179.01 | \$800.00 | **\$0.9790 per 1k requests** |

### Core Optimization Levers
1. **Public FAQ In-Memory TTL Cache:** Intercepts common general informational queries at the edge, achieving a 62.5% hit rate and lowering token spend across baseline operations.
2. **Offline Batch Logistics Queue:** Groups background supply chain requests into periodic batch updates, minimizing chat connection costs.
