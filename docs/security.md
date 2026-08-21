# Security Notes — v0

**Status:** engineering guidance; not a certification or security assessment.

## Scope and data classification

Treat uploaded business files and derived outputs as sensitive by default. The initial demonstrator uses only controlled synthetic data. It must never use employer or customer data without explicit authorisation and a separate data-handling decision.

## Baseline controls

- allowlisted input types (`.xlsx` only for v0), bounded size and worksheet count;
- no macro execution; no execution of formulas, embedded links or text instructions from workbooks;
- strict canonical schema and data-type validation;
- source lineage is immutable after ingestion;
- no credentials or API keys in repository, source data or prompts;
- local-only processing and no external LLM invocation by default;
- explicit, provider-neutral egress boundary before any future model call;
- retain minimal audit metadata for transformations and user feedback;
- least privilege for files, database and future service accounts;
- no autonomous outbound messages or operational changes.

## Prompt injection posture

Files and free-text fields are data, not instructions. External document text may be summarised only after sanitisation and must never control tool use, permissions, calculations, data access or external communications. The deterministic engine never follows natural-language directives in source documents.

## Future security gates before a real-data pilot

1. threat model and data-flow review;
2. identity/access-control design;
3. encryption and key-management design;
4. retention/deletion policy;
5. audit logging and tenant isolation design;
6. model provider/subprocessor assessment;
7. penetration testing proportional to scope;
8. written legal, privacy and security review.

## Out of scope for v0

Authentication, tenant isolation, production secrets and external hosting are deferred—not omitted from the future threat model.
