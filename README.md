# OpsPilot AI

> **Evidence-first industrial performance intelligence**
>
> A local Python MVP that turns three synthetic finance workbooks into a reproducible variance investigation — with deterministic quality gates, source-row lineage and human-reviewed next steps.

![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)
![Tests](https://img.shields.io/badge/tests-pytest-0A9EDC)
![Data](https://img.shields.io/badge/data-synthetic_only-2E8B57)
![Status](https://img.shields.io/badge/status-pre--validation_MVP-5E6AD2)

## Why this exists

Industrial performance reporting often spans ERP exports, spreadsheets, BI outputs and manual management commentary. The first OpsPilot wedge is deliberately narrow:

```text
Actual.xlsx + Budget.xlsx + Forecast.xlsx
→ validate data quality
→ reconcile values deterministically
→ rank material variances
→ retain source file / sheet / row lineage
→ produce a human-reviewed investigation prompt
```

The goal is **not** another generic chatbot. It is to test whether controllers need a faster, more traceable way to investigate recurring performance deviations.

## Demo result

The included fictional company, **NOVA INDUSTRIES GmbH**, produces this tested scenario:

| Signal | Deterministic result |
|---|---:|
| Actual vs Budget operating-expense variance | **+€184,320** |
| Main driver | External consulting: **+€132,040** |
| Cost-centre driver | `4130` |
| Post-forecast-freeze evidence | **€96,200** across 47 transactions |
| Source lineage | 48 Actual records + 1 Budget record |

The post-freeze timing is presented as **evidence for an investigation**, not proof of causality.

## Product principles

1. **Traceability > generation** — material outputs link back to file, sheet, row, formula and assumptions.
2. **Determinism before AI** — validation and calculations are Python/Pandas logic; language generation is not the source of truth.
3. **Fail closed** — duplicates, missing required values, inconsistent currency and unmapped accounts block analysis.
4. **Human decision rights** — suggested actions can be approved, corrected or rejected; nothing is executed automatically.
5. **Independent, safe data only** — all bundled data is synthetic and fictional.

## Run locally

> The MVP is local-only. Do not use employer, customer, supplier or otherwise confidential files.

```bash
git clone https://github.com/bastiendfd/opspilot-ai.git
cd opspilot-ai

python -m venv .venv
# Windows Git Bash
.venv/Scripts/python.exe -m pip install -r requirements-dev.txt
.venv/Scripts/python.exe -m pytest -q
.venv/Scripts/python.exe scripts/generate_synthetic_data.py
.venv/Scripts/python.exe -m streamlit run src/ui/app.py
```

Then open the local address shown by Streamlit, usually `http://127.0.0.1:8501`.

## Included demo paths

- **NOVA demo** — canonical Actual/Budget/Forecast Excel files.
- **Data-quality variants** — controlled duplicates, missing cost centre, currency mismatch and unmapped account cases.
- **Five data-fit packs** — English, German and French headers/worksheets mapped into the same canonical model without pack-specific code.

## Repository map

```text
src/                 deterministic product modules
tests/               behavioural and quality-gate tests
data/synthetic/      fictional workbooks and ground truth
docs/                architecture, security and decision records
research/            public market notes and validation protocol
product/             requirements, workflows and backlog
scripts/             reproducible synthetic-data generation
```

## Current limitations

This is not production software and not a claim of legal/compliance readiness. It intentionally excludes:

- real customer or employer data;
- SAP, Power BI and SharePoint connectors;
- authentication, multi-tenancy and hosted deployment;
- autonomous financial, operational or procurement actions;
- external LLM calls by default.

See [SECURITY.md](SECURITY.md), [docs/security-review-2026-08-17.md](docs/security-review-2026-08-17.md) and [docs/architecture.md](docs/architecture.md).

## Validation before expansion

The next proof is customer/workflow evidence, not more features. The project includes a no-outreach workflow-displacement protocol and explicitly does **not** contact anyone or use confidential data.

## License

No license has been selected yet. All rights reserved unless and until a license is added.
