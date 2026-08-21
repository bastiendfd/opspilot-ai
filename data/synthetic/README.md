# NOVA INDUSTRIES GmbH — Synthetic Dataset Design

**Fictional company:** NOVA INDUSTRIES GmbH  
**Location:** Hamburg, Germany  
**Scale:** approximately €120m annual revenue; 450 employees  
**Data status:** fully synthetic; independent IP; no employer/client content.

## Workbook contract

Three workbooks have one `Transactions` worksheet with the canonical columns:

`transaction_id`, `scenario`, `period`, `posting_date`, `amount`, `currency`, `account`, `account_name`, `cost_center`, `business_unit`, `material`, `supplier`, `purchase_order`, `po_created_date`, `forecast_freeze_date`.

`Actual.xlsx` contains transactions. `Budget.xlsx` and `Forecast.xlsx` contain synthetic plan allocations at compatible granularity.

## Controlled ground truth

| ID | Type | Scenario | Expected system response |
|---|---|---|---|
| GT-01 | External consulting overspend | Actual | Material positive Actual-vs-Budget variance in cost centre `4130`, account `640100` |
| GT-02 | Post-freeze PO activity | Actual | Consulting transactions with `po_created_date` after `forecast_freeze_date` can be evidence-filtered |
| GT-03 | Duplicate transaction | Actual | Deterministic duplicate finding; blocks trusted analysis until reviewed |
| GT-04 | Missing cost centre | Actual | Required-dimension validation finding; blocks trusted analysis |
| GT-05 | Currency mismatch | Actual | Currency validation finding; blocks trusted analysis |
| GT-06 | Forecast mapping issue | Forecast | Invalid/unmapped account or cost centre recognised as a mapping finding |
| GT-07 | Production-volume decline | Actual | A volume signal exists as a separate operational measure; deferred from the finance core analysis |

## Demonstration sequence

1. Load the clean generated scenario data to demonstrate reconciliation, €184,320 OPEX variance and root cause.
2. Load the deliberately invalid QA workbook variant to demonstrate fail-closed quality gates.
3. Inspect source lineage and exact transaction records behind each displayed driver.

The dataset must not depend on hard-coded analysis outputs; the engine must calculate the visible values from workbook contents.
