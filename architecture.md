# AfyaPlus AI System Infrastructure Architecture Diagram

### System Module Boundaries

[Client App] --> [FastAPI Layer (main_pipeline.py)]
|                                 |
[Security Guard 400]           [Auth Verification]
|                                 |
[Triage Router (Stub)]         [Redact & Hash Engine]
|                                 |
[Pinned Model Reference]       [Local audit_trail.jsonl]

### Execution Lifecycles
1. Inbound requests must supply a valid Authorization Bearer credential to pass HTTP validation barriers.
2. The payload is inspected by the pre-model guard to identify injection patterns before touching downstream logic.
3. Once cleared, the text is routed to the deterministic triage matrix, while system logs are automatically redacted and hashed to safeguard user identity.
