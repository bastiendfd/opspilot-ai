from pathlib import Path

from src.analytics.service import analyze_workbooks
from src.synthetic.generate import generate_demo_workbooks, generate_quality_issue_workbooks


def test_quality_issue_workbook_blocks_end_to_end_analysis_with_all_controlled_findings(
    tmp_path: Path,
) -> None:
    clean = generate_demo_workbooks(tmp_path)
    quality = generate_quality_issue_workbooks(tmp_path)

    report = analyze_workbooks(
        actual_path=quality["actual_quality_issues"],
        budget_path=clean["budget"],
        forecast_path=clean["forecast"],
    )

    assert report.blocked is True
    assert report.insight is None
    assert {finding.code for finding in report.findings} >= {
        "duplicate_transaction_id",
        "missing_required_value",
        "inconsistent_currency",
    }
