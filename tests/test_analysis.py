from pathlib import Path

import pytest

from src.analytics.service import analyze_workbooks
from src.synthetic.generate import generate_demo_workbooks, generate_quality_issue_workbooks


def test_analysis_produces_cited_deterministic_insight_for_clean_workbooks(tmp_path: Path) -> None:
    workbooks = generate_demo_workbooks(tmp_path)

    report = analyze_workbooks(
        actual_path=workbooks["actual"],
        budget_path=workbooks["budget"],
        forecast_path=workbooks["forecast"],
    )

    assert report.blocked is False
    assert report.findings == []
    assert report.insight is not None
    assert report.insight.variance_amount == pytest.approx(184_320)
    assert report.insight.variance_percent == pytest.approx(7.7838, abs=0.0001)
    assert report.insight.driver_account == "640100"
    assert report.insight.driver_variance_amount == pytest.approx(132_040)
    assert report.insight.cost_center == "4130"
    assert report.insight.post_freeze_amount == pytest.approx(96_200)
    assert len(report.insight.actual_record_ids) == 48
    assert report.insight.plan_record_ids == ["Budget.xlsx:Transactions:2"]
    assert report.insight.confidence_score == 98
    assert "Review unplanned consulting POs" in report.insight.recommended_action


def test_analysis_blocks_when_required_currency_is_inconsistent(tmp_path: Path) -> None:
    workbooks = generate_demo_workbooks(tmp_path)
    import pandas as pd

    actual = pd.read_excel(workbooks["actual"])
    actual.loc[0, "currency"] = "USD"
    actual.to_excel(workbooks["actual"], sheet_name="Transactions", index=False)

    report = analyze_workbooks(
        actual_path=workbooks["actual"],
        budget_path=workbooks["budget"],
        forecast_path=workbooks["forecast"],
    )

    assert report.blocked is True
    assert report.insight is None
    assert any(finding.code == "inconsistent_currency" for finding in report.findings)


def test_analysis_blocks_forecast_account_missing_from_reference_scenarios(tmp_path: Path) -> None:
    workbooks = generate_demo_workbooks(tmp_path)
    quality_workbooks = generate_quality_issue_workbooks(tmp_path)

    report = analyze_workbooks(
        actual_path=workbooks["actual"],
        budget_path=workbooks["budget"],
        forecast_path=quality_workbooks["forecast_mapping_issue"],
    )

    assert report.blocked is True
    assert report.insight is None
    assert any(finding.code == "unmapped_account" for finding in report.findings)
