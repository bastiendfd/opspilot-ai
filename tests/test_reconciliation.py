from pathlib import Path

import pytest

from src.ingestion.loader import ingest_workbook
from src.reconciliation.variance import reconcile_actual_vs_plan
from src.synthetic.generate import generate_demo_workbooks


def test_reconciliation_calculates_traceable_actual_vs_budget_variances(tmp_path: Path) -> None:
    workbooks = generate_demo_workbooks(tmp_path)
    actual = ingest_workbook(workbooks["actual"], scenario="actual")
    budget = ingest_workbook(workbooks["budget"], scenario="budget")

    result = reconcile_actual_vs_plan(actual, budget, plan_name="budget")

    assert result.total_actual == pytest.approx(2_552_320)
    assert result.total_plan == pytest.approx(2_368_000)
    assert result.total_variance == pytest.approx(184_320)
    assert result.variance_percent == pytest.approx(7.7838, abs=0.0001)

    consulting = result.drilldown.loc[
        (result.drilldown["account"] == "640100")
        & (result.drilldown["cost_center"] == "4130")
    ].iloc[0]
    assert consulting["actual_amount"] == pytest.approx(400_000)
    assert consulting["plan_amount"] == pytest.approx(267_960)
    assert consulting["variance_amount"] == pytest.approx(132_040)
    assert consulting["contribution_percent"] == pytest.approx(71.6363, abs=0.0001)
    assert len(consulting["actual_record_ids"]) == 48
    assert consulting["plan_record_ids"] == ["Budget.xlsx:Transactions:2"]
