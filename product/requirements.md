# Product Requirements — MVP v0

## Job to be done

When a monthly performance package is available as Actual, Budget and Forecast Excel exports, help a controller identify and verify the most material deviations without manually reconciling the files and building drill-downs.

## Functional requirements

1. Upload three `.xlsx` workbooks with a clear scenario assignment.
2. Inspect workbook sheets, headers and types; create immutable source line references.
3. Validate required columns, periods, currencies, duplicate rows, missing values, mapping consistency and totals.
4. Prevent analytical claims when blocking validation findings exist.
5. Calculate Actual-vs-Budget, Actual-vs-Forecast, current-period-vs-prior-period and YTD comparisons.
6. Rank material deviations deterministically.
7. Drill down by cost centre, account and available dimensions; calculate contribution to parent variance.
8. Show source rows, formula and assumptions for each material finding.
9. Render a concise explanation that cites the calculated evidence and clearly labels any inference.
10. Offer a bounded recommendation plus structured Approve/Correct/Reject feedback.

## Non-functional requirements

- repeatable output for identical inputs;
- no financial imputation by an LLM;
- local/synthetic operation in v0;
- interpretable error messages;
- automated coverage for core calculation and data-quality behaviour.

## Acceptance scenario

Given controlled NOVA INDUSTRIES workbooks, the demo detects documented anomalies and allows a user to trace each visible financial claim to its source records.
