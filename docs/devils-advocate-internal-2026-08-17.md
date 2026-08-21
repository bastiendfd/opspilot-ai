# Devil’s Advocate — Internal Pre-mortem

**Date:** 2026-08-17  
**Status:** internal critical review; an additional independent subagent review has been launched separately.  
**Rule:** these are risks/hypotheses to falsify, not factual claims about customers.

## Failure thesis

OpsPilot fails because it builds a technically attractive reconciliation demo for a problem that customers either solve adequately with Excel/Power BI/SAP, cannot safely expose to a startup, or will not pay enough to solve.

## 1. “Excel + Power BI is good enough”

**Failure mode:** Controllers have established templates, understand their exceptions, and view a new tool as an additional reconciliation layer rather than a time saver.

**Early falsification test:** During interviews, ask for the last materially difficult variance investigation: elapsed time, handoffs, revisions and source-proof effort. If fewer than 5 of the first 10 people describe recurring expensive investigation/rework, stop prioritising this wedge.

**Required evidence to continue:** repeated examples where a source-traceable answer changes the speed or quality of a decision.

## 2. The customer wants planning, not investigation

**Failure mode:** The budget owner buys an FP&A/planning platform or asks for forecasting instead; the source-lineage investigation wedge has no standalone budget.

**Early falsification test:** Ask who owns the budget and whether the last reporting problem led to a tool evaluation. Do not pitch the product first.

**Required evidence to continue:** a named buyer who distinguishes reconciliation/investigation pain from planning-model pain and can articulate an outcome.

## 3. Integration/security destroys the economic case

**Failure mode:** File upload proves little because real users require SAP/SharePoint/Power BI integration, SSO, data residency, audit logs and security review before pilot. The setup cost dwarfs saved reporting hours.

**Early falsification test:** Ask what a no-production, local or sandbox pilot would require. Record exact security/integration blockers and whether a synthetic/sanitised test is accepted.

**Required evidence to continue:** a credible design-partner route that does not require building enterprise infrastructure before value is observed.

## 4. Data quality is too poor or too bespoke

**Failure mode:** Every company has custom chart-of-accounts mappings, unusual allocations, manual adjustments and period logic. Quality gates produce too many blocks; professional services dominates the model.

**Early falsification test:** Request only a description of export shape and the last reconciliation failure—never real confidential data. Measure number/type of expected mapping and semantic exceptions.

**Required evidence to continue:** a repeatable canonical minimum across several companies, with mapping effort bounded enough to support the intended economics.

## 5. “Root cause” over-promises

**Failure mode:** The system reliably shows contribution but users interpret generated language as causality. One misleading recommendation erodes finance trust.

**Early falsification test:** Put evidence and causal-language boundaries in front of controllers. Ask which statement they would approve, correct or reject and why.

**Required evidence to continue:** users value association/evidence language rather than demanding unjustified causal certainty.

## 6. Incumbents absorb the feature

**Failure mode:** SAP/Microsoft/FP&A vendors add similar AI summaries and source navigation, making a narrow feature look like a commodity.

**Early falsification test:** For each interview, identify the existing stack and ask what it cannot do in the last difficult investigation. Compare actual workflow gaps, not marketing claims.

**Required evidence to continue:** a repeated gap in cross-file validation, reconciliation, lineage and follow-through—not merely lack of a chat interface.

## 7. Long industrial sales cycles prevent learning

**Failure mode:** Targeting mid-market manufacturers leads to stakeholder-heavy procurement and long feedback loops before commercial proof.

**Early falsification test:** Determine whether a controller can evaluate a local demo without IT/procurement, and whether the stakeholder map permits a short discovery loop.

**Required evidence to continue:** a research/pilot motion that creates learning in weeks, not a promise of an enterprise deal in months.

## Recommendation

Do not add connectors, predictions, RAG, multi-tenancy or autonomous agents. The next validation asset should be an interview scorecard that quantitatively records:

1. investigation frequency and hours;
2. last concrete consequence of late/wrong analysis;
3. source-traceability requirement;
4. current stack failure;
5. pilot/security feasibility;
6. buyer and budget route;
7. willingness to test, in the interviewee’s own words.

## Kill criteria to define now

Pause or reconsider the wedge if, after 10 high-quality interviews, there is no repeated costly investigation workflow, no credible local/synthetic test route, or no buyer who distinguishes this problem from generic planning/reporting.
