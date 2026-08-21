# Validation Plan v1 — Displacement Before Build

**Status:** proposed research protocol. No outreach is authorised by this document.

## Objective

Determine whether a controller investigation workflow is expensive, frequent and insufficiently solved by the existing Excel/BI/ERP stack.

## Study design

### Sample

- 8–10 observed current-state investigations for the first gate.
- Target roles: industrial controller first; include Head of Controlling/CFO and IT/security only where a real workflow exists.
- No confidential data or employer contacts. Use verbal walkthroughs, anonymised descriptions, or synthetic examples only.

### Per-workflow scorecard

| Field | Measure |
|---|---|
| Trigger | Last real variance/investigation question |
| Frequency | Monthly/quarterly/ad hoc and exception rate |
| Current stack | ERP, Excel, Power Query, Power BI, planning tool, manual trackers |
| Manual effort | Minutes/hours and people/handoffs |
| Rework | Number/type of reconciliation or comment revisions |
| Evidence gap | What cannot be traced today? |
| Decision consequence | Delay/error impact, with direct quote/context |
| Existing adequacy | Can current tools generate a trusted answer? Why/why not? |
| Data-fit | Expected mappings, period logic, exports, quality blockers |
| Security feasibility | First mandatory constraint and expected effort |
| Buyer path | User, sponsor, budget owner, procurement/IT gates |
| Test signal | Exact words on willingness to evaluate/pay, if offered voluntarily |

## Gate 1 — Workflow displacement

Advance only if at least 3 of the first 8–10 qualified participants describe a current-stack failure that requires substantial manual reconciliation to obtain a trusted answer.

## Gate 2 — Synthetic data fit

Build five heterogeneous synthetic export packs. A non-engineer must configure each in less than four hours and repeat a refresh without code changes.

## Gate 3 — Commercial/security feasibility

For every promising workflow, obtain both a value-buyer discussion and an IT/security feasibility view. Count no workflow as traction without a named buyer, credible paid-test path and bounded integration/security requirement.

## Kill/reposition signals

Pause/reconsider the wedge if any of the following dominates:

- existing tools are adequate for most qualified users;
- mapping/integration requires bespoke implementation;
- a local/synthetic evaluation is not feasible;
- no buyer distinguishes the problem from generic planning/reporting;
- evaluation cycles routinely exceed 60 days before a repeatable run.
