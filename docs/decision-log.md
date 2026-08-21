# Decision Log

| Date | Decision | Why | Alternatives considered | Risks | Reversible? |
|---|---|---|---|---|---|
| 2026-08-17 | Start with three uploaded Excel files, not SAP/Power BI/SharePoint integrations. | Lowest integration complexity; permits synthetic demo and customer discovery around the workflow. | Direct SAP, semantic-model, SharePoint connectors. | File uploads may not reflect production integration friction. | Yes |
| 2026-08-17 | Make deterministic validation and lineage prerequisites for explanation. | Financial-performance conclusions require reproducibility and trust. | LLM-led analysis with post-hoc citations. | Slower initial development; more data modelling work. | No in principle; implementation is reversible. |
| 2026-08-17 | Use a Python file-first analytical core; defer database, Docker and multi-tenancy. | Keeps MVP cheap, local and testable. | Database-first SaaS architecture; React frontend. | Later migration required if a pilot needs persistence. | Yes |
| 2026-08-17 | Treat the temporary name “OpsPilot AI” as provisional. | Naming is not current validation risk. | Branding process now. | Future rename cost. | Yes |
| 2026-08-17 | Use only synthetic/public/explicitly authorised data. | Preserve independent IP and respect V.I.E/employer confidentiality constraints. | Using employer examples/processes. | Synthetic data may miss real-world quirks. | No |
| 2026-08-17 | Add validation gates before extending the product scope. | Independent Devil’s Advocate review found incumbent adequacy, data-fit, security and buyer path unproven. | Continue feature build; direct integration pilot. | Slower visible feature progress; may disprove current wedge. | Yes |

## Template

| Date | Decision | Why | Alternatives considered | Risks | Reversible? |
|---|---|---|---|---|---|
| YYYY-MM-DD |  |  |  |  | Yes / No |
