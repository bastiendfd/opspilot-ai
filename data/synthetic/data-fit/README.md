# Data-Fit Packs — Structural Validation Gate

**Status:** generated synthetic test corpus.  
**Location:** `data/synthetic/data-fit/`

## Purpose

These five packs test whether the current canonical model can ingest, validate and analyse structurally different tri-scenario Excel exports using only `mapping.json`, not pack-specific code.

## Packs

| Pack | Worksheet | Header style |
|---|---|---|
| `alpha` | `Transactions` | Canonical English |
| `bravo` | `GL Export` | English finance/ERP export |
| `charlie` | `Buchungen` | German finance export |
| `delta` | `Finance_Data` | Generic operational finance export |
| `echo` | `Controle_Gestion` | French controlling export |

Every pack contains Actual, Budget and Forecast workbooks plus a per-scenario mapping configuration.

## Verified result

The configured pipeline runs all five packs without a code branch per pack and returns the expected Actual-vs-Budget variance of **€184,320**. This is automated by `tests/test_data_fit_packs.py`.

## Critical limitation

The five packs deliberately vary **structure** (file names, worksheets, language and headers) but retain the same NOVA economic facts and common canonical semantics. They do not yet test:

- different fiscal calendars;
- sign conventions or credit/debit structures;
- account hierarchy changes;
- allocation/accrual logic;
- multiple currencies with conversion rules;
- different transaction grain;
- parent/child cost-center hierarchy;
- semantic ambiguity in real ERP exports.

Therefore this is evidence that mapping configuration works across header/schema variation—not evidence of broad real-world industrial data fit.

## Reproduce

```bash
C:/Users/basti/opspilot/.venv/Scripts/python.exe scripts/generate_synthetic_data.py
C:/Users/basti/opspilot/.venv/Scripts/python.exe -m pytest tests/test_data_fit_packs.py -q
```
