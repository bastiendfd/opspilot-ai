from pathlib import Path

import pandas as pd
import pytest

from src.synthetic.generate import generate_demo_workbooks, generate_quality_issue_workbooks


def test_generate_demo_workbooks_creates_three_readable_scenario_files(tmp_path: Path) -> None:
    generated = generate_demo_workbooks(tmp_path)

    assert set(generated) == {"actual", "budget", "forecast"}
    for scenario, workbook_path in generated.items():
        assert workbook_path.exists(), scenario
        assert workbook_path.suffix == ".xlsx"

    assert generated["actual"].name == "Actual.xlsx"
    assert generated["budget"].name == "Budget.xlsx"
    assert generated["forecast"].name == "Forecast.xlsx"


def test_generated_actual_contains_traceable_post_freeze_consulting_evidence(tmp_path: Path) -> None:
    generated = generate_demo_workbooks(tmp_path)
    actual = pd.read_excel(generated["actual"], sheet_name="Transactions")

    assert {
        "transaction_id",
        "scenario",
        "period",
        "amount",
        "currency",
        "account",
        "account_name",
        "cost_center",
        "purchase_order",
        "po_created_date",
        "forecast_freeze_date",
    }.issubset(actual.columns)
    assert set(actual["scenario"]) == {"actual"}
    assert actual["amount"].sum() == pytest.approx(2_552_320)

    consulting = actual.loc[
        (actual["account"].astype(str) == "640100")
        & (actual["cost_center"].astype(str) == "4130")
        & (pd.to_datetime(actual["po_created_date"]) > pd.to_datetime(actual["forecast_freeze_date"]))
    ]
    assert len(consulting) == 47
    assert consulting["amount"].sum() == pytest.approx(96_200)


def test_quality_issue_workbooks_contain_controlled_validation_and_mapping_anomalies(
    tmp_path: Path,
) -> None:
    generated = generate_quality_issue_workbooks(tmp_path)

    actual = pd.read_excel(generated["actual_quality_issues"])
    forecast = pd.read_excel(generated["forecast_mapping_issue"])

    assert actual["transaction_id"].duplicated().any()
    assert actual["cost_center"].isna().any()
    assert "USD" in set(actual["currency"])
    assert "UNMAPPED" in set(forecast["account"].astype(str))
