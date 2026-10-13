# AfyaPlus-AI-Health-Operations-System

## Overview
This integrated capstone repository delivers a hardened, production-ready version of the AfyaPlus AI Health-Operations platform. The architecture unifies our public FastAPI Triage API layer with our logistics Model Context Protocol (MCP) tooling nodes. The complete codebase aligns directly with the privacy guidelines of the Kenya Data Protection Act (KDPA) 2019, implementing strict prompt injection filters, token redaction, and automated data retention cleaning loops. Full business tracking details are documented inside `docs/build_checkpoint.md`.

## Project path
- [x] AfyaPlus Module 4 Capstone (Official Recommended Path)
- [ ] Domain / field alternative with skill checklist

## Week reuse (open these)
- **Weeks 1-5:** Standardized local data containment architecture and dictionary routing stubs.
- **Week 6:** Public endpoint routing layers managed natively via the `main_pipeline.py` file.
- **Week 7:** FinOps resource optimization analysis cataloged inside `docs/cost_analysis.md`.
- **Week 8:** Explicit model signature version pins documented inside `integration_map.json`.
- **Week 9:** Log masking infrastructure smoke checks verified via `tests/test_security_smoke.py`.
- **Week 10:** Operational health-poster data transfer policies mapped inside `fixtures/README.md`.

## Dataset
- **fixtures/:** Standardized using `fixtures/triage_messages_sample.jsonl` which contains exactly **300 synthetic patient entries**. No external production environments were scraped.

## Quick start
Execute the automated test pyramid suite locally via standard terminal frameworks:
```bash
python -m pytest -q
```

## Testing
*   **unit default:** `python -m pytest -m unit`
*   **integration:** `python -m pytest -m integration`
*   **security:** `python -m pytest tests/test_security_smoke.py`

## Demo
Launch and verify the application locally using these three terminal commands:
```bash
# 1. Start the application engine layer
python -m uvicorn main_pipeline:app --host 127.0.0.1 --port 8000

# 2. Query the system health endpoint
curl -X GET http://127.0.0

# 3. Submit a secure triage verification query
curl -X POST http://127.0.0 -H "Authorization: Bearer test_token" -H "Content-Type: application/json" -d '{"role": "clinical_officer", "symptoms": "Patient shows a high fever."}'
```

## Fallbacks declared
- [x] no Azure Key Vault (local-env plus the twin JSON)
- [x] no AWS account
- [x] local MCP stub
- [x] legal review pending on lawful_basis

## Checklist
- [x] Secrets not in git
- [x] MCP cannot dump the environment or every clinic
- [x] The brief is readable by a non-engineer
