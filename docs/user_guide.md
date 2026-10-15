# AfyaPlus AI Operational Field Manual

### Core Test Verification Command
To run the automated verification suites across all layers, run this command in your workspace terminal:
```bash
python -m pytest -q
```

### Interfacing with Application Endpoints
To verify endpoint functionality, start the platform application layer locally and use curl to test transaction routing:

```bash
# 1. Health Verification Check
curl -X GET http://127.0.0

# 2. Patient Triage Processing Call (Secure Path)
curl -X POST http://127.0.0 \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.validtoken" \
  -H "Content-Type: application/json" \
  -d '{"role": "clinical_officer", "symptoms": "Patient presents with a high fever and low blood pressure."}'
```
