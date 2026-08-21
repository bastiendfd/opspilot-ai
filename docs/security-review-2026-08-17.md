# Security Review — Local MVP Slice

**Date:** 2026-08-17  
**Status:** engineering review, not a penetration test, certification or legal assessment.

## Scope

Reviewed the local synthetic-data code path: Excel upload → temporary local file → deterministic parsing/validation → in-memory report → Streamlit presentation.

## Controls observed

| Control | Status | Notes |
|---|---|---|
| Synthetic/authorised-data boundary | Documented | No employer/customer data used in project artefacts. |
| No external model/network calls in analytical core | Verified static scan | No high-risk network/API/secret/execution patterns found in `src/`. |
| File extension allowlist | Implemented | UI accepts `.xlsx` only. This is a usability control, not content-type security. |
| Upload size bound | Implemented | 20 MB per workbook in UI. |
| Temporary upload handling | Implemented | User uploads are stored in a `TemporaryDirectory` for analysis. |
| No autonomous action | Implemented | UI feedback is session-local; it does not email, write to an ERP or invoke tools. |
| Source lineage | Implemented | Record IDs retain source file/sheet/row; useful for auditability. |
| Deterministic validation before insights | Implemented | Duplicate/missing/currency/mapping findings block analysis. |

## Findings and unresolved risks

### S-01 — No authentication or authorisation

**Severity:** high for any shared or deployed use; acceptable only for a local synthetic demonstrator.  
**Action:** do not expose beyond localhost or use real data until identity, access control and tenant isolation are designed.

### S-02 — Workbook parsing attack surface

**Severity:** medium/high for real data.  
**Status:** only `.xlsx` extension and size are constrained. The implementation does not yet inspect ZIP contents, reject encrypted workbooks, enforce sheet/row/column limits, scan malformed archive ratios or maintain a hostile-file corpus.  
**Action:** add secure parser limits, adversarial workbook tests and an upload quarantine approach before any real-data pilot.

### S-03 — Excel formulas and external links

**Severity:** medium.  
**Status:** Pandas/openpyxl read stored values but this behaviour needs explicit test coverage and documented policy.  
**Action:** establish formula/link/macro policy and test that uploaded content cannot trigger execution or data egress.

### S-04 — Feedback is not durable or auditable

**Severity:** medium for product integrity; low for local demo security.  
**Action:** before a pilot, persist feedback in an append-only audit model with identity, timestamp and record/evidence references.

### S-05 — No encryption, retention, backup or provider boundary implementation

**Severity:** high for a real-data service.  
**Action:** defer real-data/cloud deployment until threat model, encryption/key management, retention/deletion, logging and subprocessor/model-egress design are reviewed.

### S-06 — No dependency/SBOM/security scan

**Severity:** medium.  
**Action:** add dependency auditing and lock files before a pilot or release.

## Security decision

The demonstrator must remain **localhost + synthetic data only**. It must not be marketed as secure for enterprise data or exposed on a network. The documented architecture and scope boundaries remain appropriate for this stage.
