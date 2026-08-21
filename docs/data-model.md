# Data Model v0

## Canonical record

| Field | Type | Required | Meaning |
|---|---|---:|---|
| `record_id` | string | Yes | Stable deterministic record identity after ingestion |
| `scenario` | enum | Yes | `actual`, `budget`, or `forecast` |
| `period` | YYYY-MM | Yes | Accounting month |
| `amount` | decimal | Yes | Signed monetary amount in record currency |
| `currency` | ISO code | Yes | Record currency; v0 expects a controlled reporting currency |
| `account` | string | Yes | GL account or mapped account group |
| `cost_center` | string | Yes | Responsible organisational unit |
| `business_unit` | string | No | Organisational dimension |
| `material` | string | No | Product/material dimension |
| `supplier` | string | No | Supplier dimension |
| `purchase_order` | string | No | PO reference |
| `posting_date` | date | No | Actual posting date |
| `forecast_freeze_date` | date | No | Cut-off used to investigate post-freeze activity |
| `source_file` | string | Yes | Original workbook name |
| `source_sheet` | string | Yes | Original worksheet name |
| `source_row` | integer | Yes | One-indexed source row |

## Evidence object

An analytical output must carry:

- `metric`: named measure;
- `formula`: executable or human-readable deterministic formula;
- `dimensions`: aggregation/drill-down dimensions;
- `source_record_ids`: linked canonical records;
- `validation_status`: pass, warning or blocked;
- `assumptions`: explicit assumptions (e.g., reporting currency);
- `generated_at` and calculation version.

## Invariants

- no duplicate `record_id` in a canonical dataset;
- no computed display value without an evidence object;
- no LLM-created value may be stored as a computed financial measure;
- missing mandatory financial values block analysis rather than being imputed.
