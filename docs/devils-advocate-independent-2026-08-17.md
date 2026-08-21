# Devil’s Advocate — Independent Review

**Date:** 2026-08-17  
**Method:** independent hostile review of the repository, current prototype and official public sources.  
**Verdict:** **the thesis is not commercially validated.**

## Core conclusion

OpsPilot demonstrates disciplined deterministic handling of one controlled three-workbook case. It does **not** yet establish that the target workflow is frequent, costly, unsolved by incumbent tools, feasible to deploy, or sufficiently valuable to purchase.

The only proposition worth testing next is narrower than the marketing thesis:

> A repeatable, low-friction controller investigation loop produces a more trusted answer than the current Excel/BI/ERP process without needing an integration project.

**Collection limitation:** the targeted SAP planning page returned `Access Denied` in this environment, so this review makes no new SAP capability claim from that page.[1]

## Main attacks on the thesis

| Challenge | Why OpsPilot could fail | Falsification test |
|---|---|---|
| Incumbent substitution | A buyer may view the product as a partial feature of SAP, Microsoft or FP&A tooling. Vena itself positions around financial/operational planning and close with connected data and AI.[5] | Observe 8–10 real current-state investigations. Reposition/pause if fewer than 3 users say their current stack cannot reach a trusted answer without substantial manual reconciliation. |
| Excel / Power BI is adequate | Power Query is already intended to filter, combine and transform data from supported sources; Power BI Copilot supports generative analysis and reporting.[2][3] | Measure incremental time-to-trusted-answer, handoffs and rework on a recent investigation. Stop if median improvement is below 30 minutes or the user prefers the existing template. |
| Data-fit economics | File-first may simply move the cost into mappings, calendar/alignment logic, hierarchy changes, currencies and ownership disputes. Auditable output does not make a bad mapping correct. | Run five heterogeneous synthetic export packs. Measure mapping time, blocked-run rate and repeatability. Do not advance if a pack needs bespoke code, more than one business-day mapping, or fails two consecutive refreshes. |
| Security/procurement | Finance workbooks may include sensitive/personal information; applicable EU privacy obligations must be analysed for real processing.[4] The local prototype defers identity, encryption, logging, retention and tenant isolation. | Give five IT/security stakeholders a one-page architecture/data-flow pack. Quantify the first blocking requirement and remediation cost rather than treating it as a later technical detail. |
| Weak willingness to pay | Capacity saved may not become cash saving; the buyer may expect ERP/BI owners to solve the issue without a new subscription. | Require an explicit budget owner and a credible paid-test path before counting a workflow as traction. |
| Long industrial cycles | Controller, CFO, IT/data, operations and procurement may all be required; several closes may be needed to establish trust. | Measure time from first conversation to workflow access, security response, first run, repeat run and commercial decision. Treat more than 60 days to a repeatable synthetic/sanitised evaluation as an adverse segment signal. |
| Weak differentiation | The current UI is tailored to the NOVA consulting scenario. Its owner, action and confidence are deterministic product assumptions, not yet proven reusable across investigations. | Test repeated situations where post-freeze spend, cost-centre ownership and cross-functional evidence handoff fail in the current stack. If prospects cannot name such a decision, the wedge is weak. |

## Three required changes to the validation plan

### 1. Replace broad interviews with a displacement protocol

Phase 1 needs **8–10 observed current-state investigations**, not only opinion interviews. For each, record systems used, manual minutes, handoffs, revision loops, source-traceability gap and whether Excel/BI/SAP already answered the question sufficiently.

**Exit condition:** do not build beyond the demonstrator if the incumbent workflow is adequate for most qualified users.

### 2. Add a data-fit/onboarding gate before any real-data pilot

Create five deliberately heterogeneous but synthetic export packs. A non-engineer must configure each in **under four hours** and repeat the next refresh without code changes.

**Exit condition:** no bespoke code, bounded mapping effort, and repeatable refresh.

### 3. Validate value buyer and security feasibility in parallel

Each promising controller workflow requires both:

1. a Head of Controlling/CFO discussion about value and paid-test path; and
2. an IT/security feasibility discussion about deployment/data requirements.

**Exit condition:** named buyer, plausible paid test, and no unbounded security/integration blocker.

## Recommendation

Do **not** add direct connectors, forecasting, RAG, multi-tenancy or autonomous agents yet. The next assets should be an interview scorecard and five varied synthetic packs designed to disprove the current wedge quickly.

## Sources

[1] https://www.sap.com/products/data-cloud/cloud-analytics/features/planning.html
[2] https://learn.microsoft.com/en-us/power-query
[3] https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-introduction
[4] https://commission.europa.eu/law/law-topic/data-protection/data-protection-eu_en
[5] https://www.venasolutions.com/platform
