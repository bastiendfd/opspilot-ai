from pathlib import Path

from src.analytics.service import analyze_workbooks
from src.synthetic.generate import generate_demo_workbooks
from src.ui.app import available_data_fit_pack_names, build_view_model


def test_view_model_exposes_summary_action_and_lineage(tmp_path: Path) -> None:
    workbooks = generate_demo_workbooks(tmp_path)
    report = analyze_workbooks(
        actual_path=workbooks["actual"],
        budget_path=workbooks["budget"],
        forecast_path=workbooks["forecast"],
    )

    view_model = build_view_model(report)

    assert view_model["blocked"] is False
    assert view_model["headline"] == "Operating expenses are €184,320 above budget (+7.8%)."
    assert view_model["driver"] == "External consulting services: +€132,040"
    assert view_model["action"] == "Review unplanned consulting POs with Procurement."
    assert view_model["variance_display"] == "+€184,320"
    assert view_model["variance_subtitle"] == "vs Budget · +7.8%"
    assert view_model["quality_status"] == "Evidence complete"
    assert view_model["evidence_summary"] == "48 Actual rows · 1 Budget row"
    assert len(view_model["actual_record_ids"]) == 48
    assert view_model["plan_record_ids"] == ["Budget.xlsx:Transactions:2"]


def test_ui_lists_the_five_generated_data_fit_packs() -> None:
    assert available_data_fit_pack_names() == ["alpha", "bravo", "charlie", "delta", "echo"]
