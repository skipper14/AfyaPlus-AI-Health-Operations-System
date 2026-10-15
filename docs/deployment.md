# AfyaPlus AI System Deployment Specification

This document details the environment requirements, configuration settings, and deployment steps for the **AfyaPlus AI Health-Operations System**.

---

## 1. Environment Requirements & Pinned Dependencies

The system runs entirely using native **Python 3.10+** standard libraries. No external production cloud dependencies are required to spin up or execute the service mesh.

### Core Software Mapping
*   **Web Server Engine:** FastAPI managed via Uvicorn ASGI processes.
*   **Testing Harness Framework:** Pytest 7.0+ featuring explicit marker partitions.
*   **Data Serialization Engine:** Standard JSON/JSONL processing blocks.

---

## 2. Infrastructure Declarations & Fallback Status

To maintain deterministic evaluation across local lab environments, the system utilizes configuration fallbacks:

*   **No Live Azure Key Vault:** Secret variables interface directly via local system context. Cryptographic configurations are referenced as configuration stubs within `secret_refs.yaml`.
*   **No Live AWS KMS:** Storage encryption logic is simulated locally using metadata configurations within `kms_twin.json`.
*   **No Live LLM/GPU Provider Access:** Inference models are replaced by local rule-based routing engines in `main_pipeline.py`, avoiding API cost overheads.
*   **Cloud Console Routing:** *Note: Live cloud resource creation steps are flagged as config-only ("not executed live" in standard lab environments).*

---

## 3. Step-by-Step Deployment Guide

Follow these steps to instantiate the environment and boot up the platform:

```bash
# Step 1: Clone the unified repository path and navigate to workspace
git clone https://github.com
cd AfyaPlus-AI-Health-Operations-System

# Step 2: Establish a local virtual environment runtime
python3 -m venv venv
source venv/bin/activate

# Step 3: Upgrade pip and mount testing packages
python3 -m pip install --upgrade pip
python3 -m pip install pytest fastapi uvicorn httpx

# Step 4: Provision the required security token context
export JWT_SECRET="benki_yetu_secure_capstone_token_hash_2026"

# Step 5: Boot up the web service routing architecture
python3 -m uvicorn main_pipeline:app --host 127.0.0.1 --port 8000 --reload
```

---

## 4. Production Hardening Checklist

*   **Non-Root Execution Context:** Ensure the container layer drop privileges to a restricted system user after initialization.
*   **Sealed Environment Quarantine:** Verify that `.gitignore` completely blocks operational `.env` variables or secret files from entering version histories.
*   **Resource Caps Mapping:** Bind execution processes to strict hardware constraints (`1 CPU` and `512 MiB` RAM limits) within orchestration layers to prevent system exhaustion attacks.
