# GDPR and EU AI Act Notes

**Status:** informational product notes, not legal advice and not a claim of compliance. Obtain qualified legal/privacy review before any real-data pilot or commercial deployment.

## GDPR considerations to track

- define controller/processor roles and documented instructions;
- document purpose limitation, data minimisation and retention;
- assess lawful basis and the presence of personal data in source files;
- map data locations, cross-border transfers and subprocessors;
- implement data-subject rights processes where applicable;
- protect confidentiality, integrity and availability;
- assess DPIA need based on real processing scope and risk;
- document incident response and contractual data-processing terms.

## EU AI Act considerations to track

The intended v0 is decision-support software for industrial performance review, with human oversight and traceable evidence. Its legal classification depends on actual deployment, functionality, data, users and applicable law. Before launch, assess transparency, instructions for use, recordkeeping, risk management, human oversight, accuracy/robustness/cybersecurity and any provider/deployer obligations that apply.

## Product-relevant controls

- deterministic calculations with source lineage;
- clear distinction between facts, computed attribution and model-generated interpretation;
- user approval/correction/rejection controls;
- no autonomous critical decisions;
- provider-agnostic model boundary with documented data egress;
- audit-oriented transformation and feedback records;
- security controls for confidential business information.

## Open questions before any pilot

1. Will uploaded exports contain personal data or commercially sensitive data?
2. Where will data, logs, backups and model processing be located?
3. Which subprocessors, model providers and connectors are involved?
4. What retention/deletion and access policies are contractually required?
5. Does the intended use create obligations beyond a general-purpose decision-support tool?
