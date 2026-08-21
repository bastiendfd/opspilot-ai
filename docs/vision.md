# OpsPilot AI — Vision

**Version:** 0.1  
**Date:** 2026-08-17  
**Status:** working hypothesis, not validated market fact

## North star

> European industrial companies trust OpsPilot to turn fragmented operational data into verified decisions and actions.

## Initial wedge

A controller or operational manager uploads `Actual.xlsx`, `Budget.xlsx`, and `Forecast.xlsx`. In under five minutes, OpsPilot must identify material performance deviations, show a reproducible drill-down, and let the user inspect the exact source rows before deciding what to do.

## Customer problem hypothesis

Industrial SMEs and mid-market firms repeatedly reconcile planning and actuals across ERP exports, spreadsheets, BI extracts and manually maintained files. The cost is not merely report preparation: late, incorrect or unexplained variance analysis slows management action. This hypothesis requires interview evidence.

## Product promise

**Verified performance intelligence, not a generic chatbot.**

1. Ingest tabular finance/operations exports.
2. Stop when data quality is insufficient; report the problem rather than inventing values.
3. Calculate Actual/Budget/Forecast and period comparisons deterministically.
4. Attribute important deviations through reproducible dimension drill-down.
5. Present evidence and a bounded, reviewable explanation.
6. Capture an explicit human decision: approve, correct or reject.

## Target beachhead (hypothesis)

- European manufacturing companies, approximately 50–1,000 employees
- Germany first, then France, DACH and Benelux
- initial buyer/champion: Head of Controlling or industrial controller
- adjacent stakeholders: CFO, COO, plant, procurement and transformation leaders

## What success means

### Technical

- calculation correctness is covered by automated tests;
- every displayed result has file/sheet/row and transformation lineage;
- validation failures are explicit and block unsafe downstream conclusions.

### Product

A target controller understands *what changed, why it changed, which evidence supports it, and the next action to consider* without manual reconciliation.

### Business

Real, recorded interviews demonstrate a frequent painful workflow and at least a subset of target users agrees to test a prototype. No willingness-to-pay claim is valid before such evidence exists.

## Explicit non-goals for v0

Direct SAP integration, Power BI/SharePoint connections, autonomous communications, generic RAG, multi-tenant SaaS, mobile, billing, predictive maintenance, and autonomous business decisions.

## Falsification conditions

The wedge should be reconsidered if interviews show any of the following:

- monthly variance investigation is not sufficiently frequent or costly;
- existing Excel/BI workflows already solve traceability well enough;
- access/integration cost systematically exceeds credible value;
- data quality prevents a reliable pilot at the customer segment;
- customers will not share data with a tightly governed external system even for a pilot.
