# Product Principles

## 1. Traceability over generation
Every material value, variance, attribution and recommendation must point to its data lineage: source file, sheet, row or source record, applied transformation, formula and assumptions.

## 2. Determinism before AI
Validation, reconciliation, aggregation, ranking and drill-down use deterministic code. The language model receives only structured computed evidence; it never supplies a financial value, a calculation, or a source record.

## 3. Fail closed on unreliable data
Missing mandatory fields, inconsistent schema, duplicate records, currency ambiguity, unbalanced totals or incomplete periods must produce a visible validation finding. The system does not silently repair or fill financial data.

## 4. Explain the evidence, not the imagination
“Cause” is only used where the data supports an attributable decomposition. Otherwise the product uses clearly labelled language such as *possible explanation* or *investigation question*.

## 5. Humans retain decision rights
Outputs are decision support. Users can approve, correct or reject an analysis/action. No automatic operational, financial, procurement, personnel or communication action is performed.

## 6. A narrow workflow wins
Prioritise the recurring Actual/Budget/Forecast investigation loop over broad connectors, dashboards or agent theatrics.

## 7. Sensitive-by-default data handling
Minimise source data, enforce explicit provider boundaries, redact unsafe content from prompts, use least privilege, avoid secrets in code, and retain audit records.

## 8. Measure outcome, not usage
A feature deserves priority only if it reduces time-to-trustworthy-answer, improves action follow-through, or creates measurable economic value.

## 9. European industrial usability
Build for German, French and English users; expect spreadsheet-first workflows; document data residency and compliance implications rather than claiming legal compliance.

## 10. Evidence can overturn the thesis
Customer interviews and pilot behaviour take precedence over founder intuition, demos and competitor narratives.
