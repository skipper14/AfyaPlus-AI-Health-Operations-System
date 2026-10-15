# AfyaPlus AI Operational Field Manual

This user guide provides instructions for verifying system status, executing the testing pyramid, interacting with triage endpoints, and generating performance footprints on the **AfyaPlus AI Platform**.

---

## 1. Quick Start Health Check
Query the public health path `GET http://127.0.0` to confirm successful system initialization and loaded model versions.

---

## 2. Executing the Testing Pyramid
Run test suites using `pytest` commands to validate security boundaries, unit configurations, integration data fixtures, and infrastructure security smoke suites.

---

## 3. Interfacing with Triage Endpoints
Send structured JSON payloads to the `/triage` path with role context metadata and symptom strings to test authorized clinical requests or observe injection guard interceptions for malicious prompt overrides.

---

## 4. Generating Local Performance Footprints
Execute the performance profiler utility (`scripts/measure_perf.py`) to measure processing speeds, record latency metrics, and update system telemetry configurations.
