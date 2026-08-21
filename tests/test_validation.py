from pathlib import Path

from src.ingestion.loader import ingest_workbook
from src.synthetic.generate import generate_demo_workbooks
from src.validation.checks import validate_records


def test_validation_reports_duplicate_missing_dimension_and_currency_mismatch(tmp_path: Path) -> None:
    workbooks = generate_demo_workbooks(tmp_path)
    records = ingest_workbook(workbooks["actual"], scenario="actual")
    invalid = records.copy()
    invalid.loc[1, "transaction_id"] = invalid.loc[0, "transaction_id"]
    invalid.loc[2, "cost_center"] = ""
    invalid.loc[3, "currency"] = "USD"

    findings = validate_records(invalid)
    finding_codes = {finding.code for finding in findings}

    assert {"duplicate_transaction_id", "missing_required_value", "inconsistent_currency"}.issubset(
        finding_codes
    )
    assert all(finding.severity == "blocking" for finding in findings)


def test_validation_reports_unmapped_account_against_explicit_mapping() -> None:
    import pandas as pd

    records = pd.DataFrame(
        {
            "record_id": ["Forecast.xlsx:Transactions:2"],
            "transaction_id": ["FOR-PLAN-001"],
            "scenario": ["forecast"],
            "period": ["2026-06"],
            "amount": [100.0],
            "currency": ["EUR"],
            "account": ["UNMAPPED"],
            "cost_center": ["4130"],
        }
    )

    findings = validate_records(records, allowed_accounts={"640100"})

    assert any(finding.code == "unmapped_account" for finding in findings)
