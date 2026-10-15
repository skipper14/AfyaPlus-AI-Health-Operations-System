# AfyaPlus AI System Infrastructure & Module Architecture

This document details the cross-component architecture, structural data boundaries, and processing life cycles for the integrated **AfyaPlus AI Health-Operations System **.

## 1. System Topology & Module Boundaries

The architecture handles request containment at the local system boundary before passing any parameter tokens to underlying processing layers or mock endpoints.

[ Inbound HTTP Triage Client / Curl request ]
│
▼
[ FastAPI Router (main_pipeline.py) ]
│
┌─────────────────┴─────────────────┐
▼                                   ▼
[ HTTPBearer Token Guard ]           [ Pre-Model Injection Guard ]
(Role Matrix Authorization)          (400 Block Regex Scanning)
│                                   │
└─────────────────┬─────────────────┘
│  (If Cleared)
▼
[ Local Deterministic Routing Stub ]
(Triage Logic Engine: 1.4.0 Baseline)
│
┌─────────────────┴─────────────────┐
▼                                   ▼
[ Structured Response Payload ]       [ Redact-Then-Hash Logging ]
(JSON formatting returned)           (Anonymized to audit_trail.jsonl)

## 2. Integrated Module Component Re-use

The platform unifies core capabilities developed across the engineering lifecycle into a single operational pipeline:

*   **Week 6 Endpoint Layer (`main_pipeline.py`):** Exposes public, type-validated FastAPI web paths (`GET /health` and `POST /triage`) utilizing an integrated `HTTPBearer` authorization dependency.
*   **Week 7 FinOps Strategy (`docs/cost_analysis.md`):** Drives system caching rules and background logistics queue models to limit token usage overheads.
*   **Week 8 Structural Versioning (`integration_map.json`):** Locks operational execution targets to static configurations (`openai/gpt-4o-mini@2026-10-11-snapshot`) to prevent downstream runtime regressions.
*   **Week 9 Security Framework (`tests/test_security_smoke.py`):** Runs pre-execution interception checks and enforces clear identity masking rules across the processing path.
*   **Week 10 & 11 Evaluation Engines (`scripts/measure_perf.py`):** Runs local smoke checking suites to generate system metrics without requiring external database hosting environments.

---

## 3. Data Processing Lifecycles

### Step 1: Inbound Authentication & Authorization Layer
When a client sends a request to the `/triage` endpoint, the system checks the `Authorization: Bearer <token>` credentials. The internal `authorize_actor_role` module compares the user's role against the `ROLE_MATRIX` array to prevent vertical privilege escalations.

### Step 2: Pre-Execution Prompt Injection Guard
Before parsing symptoms or triggering any model inference logic, the plain-text input string is analyzed by the `pre_model_injection_guard` pattern-matching loop. If a malicious override phrasing fingerprint is matched, the transaction drops immediately with an HTTP 400 Bad Request error.

### Step 3: Local Deterministic Triage Inference
Once cleared by the input filters, the symptoms are processed by the `execute_triage_router` matrix engine. This engine compares input criteria against your 300-row synthetic fixture set (`fixtures/triage_messages_sample.jsonl`) to return a structured JSON response specifying the urgency tier, action protocols, and consistency metrics.

### Step 4: Redaction & Hashing Trail Generation
Simultaneously, the transaction context is routed to the `redact_then_hash_payload` function. This step completely strips raw Bearer keys from the metadata stream, substitutes clinical text details with an unalterable SHA-256 hash, and appends the anonymized, KDPA-compliant execution trace to the system's log files.

---

## 4. Statutory Compliance & Isolation Boundaries

*   **Non-Mixing Protocol Enforced:** Patient Protected Health Information (PHI) properties are completely isolated within healthcare triage modules, with no commercial store files or retail item data mixed into the catalog structures.
*   **Data Minimization Tracking:** The system logs only SHA-256 validation fingerprints rather than plain-text medical strings, aligning directly with the core data protection principles of the Kenya Data Protection Act (KDPA) 2019.
*   **Honest Build Checkpoints:** All live connections to paid external cloud networks or distributed database clusters are explicitly disabled. The architecture leverages local memory routing stubs to support deterministic verification runs at zero financial cost.
