"""Minimal local Streamlit demonstrator for verified performance analysis."""

from __future__ import annotations

import tempfile
from pathlib import Path
from typing import Any

import streamlit as st

from src.analytics.configured import analyze_configured_pack
from src.analytics.service import AnalysisReport, analyze_workbooks

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SAMPLE_DIRECTORY = PROJECT_ROOT / "data" / "synthetic"
MAX_UPLOAD_BYTES = 20 * 1024 * 1024

OPS_CSS = """
<style>
:root { color-scheme: dark; }
.stApp { background: #0a0b0d; color: #eef0f4; }
[data-testid="stSidebar"] { background: #101114; border-right: 1px solid rgba(255,255,255,.07); }
[data-testid="stSidebar"] > div:first-child { padding-top: 1.4rem; }
.block-container { max-width: 1280px; padding: 1.5rem 2.5rem 3.5rem; }
h1, h2, h3, p, div, button { font-feature-settings: "cv01", "ss03"; }
h1 { letter-spacing: -.045em; font-weight: 590; }
.ops-topbar { display:flex; justify-content:space-between; align-items:center; padding: .2rem 0 1.35rem; border-bottom:1px solid rgba(255,255,255,.07); margin-bottom:1.5rem; }
.ops-brand { display:flex; align-items:center; gap:.65rem; font-size:15px; font-weight:590; letter-spacing:-.02em; }
.ops-mark { width:24px; height:24px; border-radius:7px; display:grid; place-items:center; color:#e8eaff; background:#5e6ad2; font-size:13px; }
.ops-meta { color:#9298a4; font-size:12px; }
.ops-chip { display:inline-flex; align-items:center; gap:7px; color:#cbd1db; font-size:12px; padding:5px 10px; border:1px solid rgba(255,255,255,.1); border-radius:999px; background:rgba(255,255,255,.025); }
.ops-dot { width:7px; height:7px; border-radius:50%; background:#26a269; box-shadow:0 0 0 3px rgba(38,162,105,.12); }
.ops-eyebrow { color:#9298a4; font-size:11px; font-family:ui-monospace, SFMono-Regular, Menlo, monospace; letter-spacing:.08em; text-transform:uppercase; margin-bottom:.45rem; }
.ops-summary { font-size:21px; line-height:1.25; letter-spacing:-.03em; max-width:720px; margin:0 0 1.35rem; color:#f4f5f7; }
.ops-card { min-height:146px; padding:18px 19px; border:1px solid rgba(255,255,255,.08); border-radius:12px; background:rgba(255,255,255,.025); }
.ops-card-primary { background:linear-gradient(135deg, rgba(94,106,210,.2), rgba(255,255,255,.025)); border-color:rgba(113,112,255,.35); }
.ops-card-label { color:#959ba6; font-size:11px; letter-spacing:.065em; text-transform:uppercase; margin-bottom:13px; }
.ops-card-value { color:#f7f8f8; font-size:29px; font-weight:590; letter-spacing:-.05em; line-height:1; margin-bottom:9px; }
.ops-card-detail { color:#b6bdc8; font-size:13px; line-height:1.45; }
.ops-status { color:#67d295; font-size:13px; font-weight:590; margin-bottom:8px; }
.ops-section-title { font-size:13px; color:#f1f3f6; font-weight:590; margin:1.85rem 0 .7rem; letter-spacing:-.01em; }
.ops-action { padding:18px 19px; border:1px solid rgba(255,255,255,.08); border-radius:12px; background:#111216; }
.ops-action-title { color:#9399a4; font-size:11px; text-transform:uppercase; letter-spacing:.065em; margin-bottom:8px; }
.ops-action-copy { color:#f3f4f6; font-size:16px; line-height:1.4; letter-spacing:-.015em; }
.ops-action-owner { color:#aeb5c1; font-size:13px; margin-top:12px; }
.ops-note { margin-top:10px; color:#8f96a1; font-size:12px; line-height:1.5; }
[data-testid="stMetric"] { background:rgba(255,255,255,.025); border:1px solid rgba(255,255,255,.08); border-radius:10px; padding:15px; }
[data-testid="stMetricLabel"] { color:#969ca7; font-size:12px; }
[data-testid="stMetricValue"] { color:#f3f4f6; font-size:22px; letter-spacing:-.04em; }
.stButton > button { border-radius:7px; border:1px solid rgba(255,255,255,.1); background:rgba(255,255,255,.04); color:#e8ebf0; font-weight:510; }
.stButton > button[kind="primary"] { background:#5e6ad2; border-color:#7170ff; color:#fff; }
.stButton > button:hover { border-color:rgba(130,143,255,.65); color:#fff; }
.stSelectbox label, .stFileUploader label, .stRadio label, .stTextArea label { color:#b9c0ca !important; font-size:12px !important; }
[data-testid="stExpander"] { border:1px solid rgba(255,255,255,.08); border-radius:10px; background:rgba(255,255,255,.015); }
.stCodeBlock { border-radius:8px; }
@media (max-width: 800px) { .block-container { padding:1rem 1rem 2rem; } .ops-topbar { align-items:flex-start; gap:12px; flex-direction:column; } .ops-summary { font-size:19px; } }
</style>
"""


def inject_ops_styles() -> None:
    """Apply the local Monitor visual system."""
    st.markdown(OPS_CSS, unsafe_allow_html=True)


def available_data_fit_pack_names() -> list[str]:
    """Return generated local packs suitable for a configured demo."""
    data_fit_directory = SAMPLE_DIRECTORY / "data-fit"
    if not data_fit_directory.exists():
        return []
    return sorted(
        directory.name
        for directory in data_fit_directory.iterdir()
        if directory.is_dir() and (directory / "mapping.json").is_file()
    )


def _format_euro(amount: float) -> str:
    return f"€{amount:,.0f}"


def build_view_model(report: AnalysisReport) -> dict[str, Any]:
    """Transform a deterministic report into presentation-only data."""
    if report.blocked:
        return {
            "blocked": True,
            "findings": [
                {"code": finding.code, "message": finding.message, "record_ids": list(finding.record_ids)}
                for finding in report.findings
            ],
        }

    assert report.insight is not None
    insight = report.insight
    return {
        "blocked": False,
        "headline": (
            f"Operating expenses are {_format_euro(insight.variance_amount)} above budget "
            f"(+{insight.variance_percent:.1f}%)."
        ),
        "variance_display": f"+{_format_euro(insight.variance_amount)}",
        "variance_subtitle": f"vs Budget · +{insight.variance_percent:.1f}%",
        "quality_status": "Evidence complete",
        "evidence_summary": (
            f"{len(insight.actual_record_ids)} Actual rows · "
            f"{len(insight.plan_record_ids)} Budget row"
        ),
        "driver": f"{insight.driver_account_name}: +{_format_euro(insight.driver_variance_amount)}",
        "cost_center": (
            f"Cost Center {insight.cost_center}: "
            f"{insight.cost_center_contribution_percent:.1f}% of variance"
        ),
        "post_freeze": _format_euro(insight.post_freeze_amount),
        "action": insight.recommended_action,
        "owner": insight.owner,
        "confidence_score": insight.confidence_score,
        "confidence_basis": insight.confidence_basis,
        "actual_record_ids": insight.actual_record_ids,
        "plan_record_ids": insight.plan_record_ids,
    }


def _save_upload(upload: Any, destination: Path) -> Path:
    if Path(upload.name).suffix.lower() != ".xlsx":
        raise ValueError("Only .xlsx workbooks are accepted in v0.")
    payload = upload.getvalue()
    if len(payload) > MAX_UPLOAD_BYTES:
        raise ValueError("Workbook exceeds the 20 MB v0 upload limit.")
    destination.write_bytes(payload)
    return destination


def _render_report(report: AnalysisReport) -> None:
    view_model = build_view_model(report)
    if view_model["blocked"]:
        st.error("Analysis blocked — resolve the quality findings before reviewing performance.")
        st.caption("OpsPilot intentionally does not generate a financial conclusion from unreliable inputs.")
        for finding in view_model["findings"]:
            with st.expander(f"{finding['code']} · {finding['message']}"):
                st.code("\n".join(finding["record_ids"]) or "No source rows available.")
        return

    st.markdown('<div class="ops-eyebrow">Monthly performance review · June 2026</div>', unsafe_allow_html=True)
    st.markdown(f'<p class="ops-summary">{view_model["headline"]}</p>', unsafe_allow_html=True)

    variance_column, driver_column, evidence_column = st.columns([1.15, 1, 1])
    with variance_column:
        st.markdown(
            f'''<div class="ops-card ops-card-primary">
                <div class="ops-card-label">Operating expenses</div>
                <div class="ops-card-value">{view_model["variance_display"]}</div>
                <div class="ops-card-detail">{view_model["variance_subtitle"]}</div>
            </div>''',
            unsafe_allow_html=True,
        )
    with driver_column:
        st.markdown(
            f'''<div class="ops-card">
                <div class="ops-card-label">Main driver</div>
                <div class="ops-card-value">+€132k</div>
                <div class="ops-card-detail">{view_model["driver"]}<br>{view_model["cost_center"]}</div>
            </div>''',
            unsafe_allow_html=True,
        )
    with evidence_column:
        st.markdown(
            f'''<div class="ops-card">
                <div class="ops-card-label">Data confidence</div>
                <div class="ops-status">● {view_model["quality_status"]}</div>
                <div class="ops-card-detail">{view_model["evidence_summary"]}<br>{view_model["confidence_score"]}/100 evidence confidence</div>
            </div>''',
            unsafe_allow_html=True,
        )

    st.markdown('<div class="ops-section-title">Recommended investigation</div>', unsafe_allow_html=True)
    st.markdown(
        f'''<div class="ops-action">
            <div class="ops-action-title">Next human-owned action</div>
            <div class="ops-action-copy">{view_model["action"]}</div>
            <div class="ops-action-owner">Suggested owner · {view_model["owner"]}</div>
            <div class="ops-note">{view_model["confidence_basis"]}</div>
        </div>''',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="ops-section-title">Evidence & review</div>', unsafe_allow_html=True)
    evidence_tab, lineage_tab, review_tab = st.tabs(["Evidence", "Source lineage", "Human review"])
    with evidence_tab:
        st.metric("Post-forecast-freeze PO activity", view_model["post_freeze"], "47 transactions")
        st.caption("Timing supports an investigation question; it does not prove causality.")
    with lineage_tab:
        st.caption(view_model["evidence_summary"])
        actual_tab, budget_tab = st.tabs(["Actual source rows", "Budget source rows"])
        with actual_tab:
            st.code("\n".join(view_model["actual_record_ids"]), language=None)
        with budget_tab:
            st.code("\n".join(view_model["plan_record_ids"]), language=None)
    with review_tab:
        st.caption("Feedback is stored only in this local browser session. It does not execute an action.")
        with st.form("human-review", clear_on_submit=True):
            decision = st.radio("Decision", ["Approve", "Correct", "Reject"], horizontal=True)
            comment = st.text_area("Comment — required for Correct or Reject")
            submitted = st.form_submit_button("Record local feedback", type="primary")
        if submitted:
            if decision in {"Correct", "Reject"} and not comment.strip():
                st.warning("Add a comment when correcting or rejecting an insight.")
            else:
                st.session_state["feedback"] = {"decision": decision, "comment": comment.strip()}
                st.success(f"Recorded locally: {decision}. No business action was executed.")
        if feedback := st.session_state.get("feedback"):
            st.caption(f"Latest local review · {feedback['decision']}")


def main() -> None:
    st.set_page_config(page_title="OpsPilot AI", page_icon="◈", layout="wide")
    inject_ops_styles()
    st.markdown(
        '''<div class="ops-topbar">
            <div><div class="ops-brand"><span class="ops-mark">◈</span>OpsPilot <span class="ops-meta">Industrial performance monitor</span></div></div>
            <div class="ops-chip"><span class="ops-dot"></span>Local synthetic workspace</div>
        </div>''',
        unsafe_allow_html=True,
    )
    st.caption("Deterministic calculations first. Evidence stays attached. No business action is executed.")

    with st.sidebar:
        st.header("Input")
        use_sample = st.button("Analyse NOVA synthetic demo")
        data_fit_pack_names = available_data_fit_pack_names()
        selected_data_fit_pack = st.selectbox(
            "Configured data-fit pack", options=[""] + data_fit_pack_names, format_func=lambda item: item or "Select a pack"
        )
        analyse_data_fit_pack = st.button(
            "Analyse configured pack", disabled=not selected_data_fit_pack
        )
        st.caption("Or upload one .xlsx workbook for each scenario. Limit: 20 MB per file.")
        actual_upload = st.file_uploader("Actual.xlsx", type=["xlsx"], key="actual")
        budget_upload = st.file_uploader("Budget.xlsx", type=["xlsx"], key="budget")
        forecast_upload = st.file_uploader("Forecast.xlsx", type=["xlsx"], key="forecast")
        analyse_uploads = st.button("Validate and analyse uploads")

    report: AnalysisReport | None = None
    if use_sample:
        report = analyze_workbooks(
            actual_path=SAMPLE_DIRECTORY / "Actual.xlsx",
            budget_path=SAMPLE_DIRECTORY / "Budget.xlsx",
            forecast_path=SAMPLE_DIRECTORY / "Forecast.xlsx",
        )
    elif analyse_data_fit_pack:
        report = analyze_configured_pack(SAMPLE_DIRECTORY / "data-fit" / selected_data_fit_pack)
    elif analyse_uploads:
        if not all((actual_upload, budget_upload, forecast_upload)):
            st.error("Provide Actual, Budget and Forecast workbooks.")
        else:
            try:
                with tempfile.TemporaryDirectory(prefix="opspilot-") as temp_directory:
                    temp_path = Path(temp_directory)
                    report = analyze_workbooks(
                        actual_path=_save_upload(actual_upload, temp_path / "Actual.xlsx"),
                        budget_path=_save_upload(budget_upload, temp_path / "Budget.xlsx"),
                        forecast_path=_save_upload(forecast_upload, temp_path / "Forecast.xlsx"),
                    )
            except (ValueError, OSError) as error:
                st.error(f"Could not process upload: {error}")

    if report is not None:
        st.session_state["report"] = report
    if "report" in st.session_state:
        _render_report(st.session_state["report"])
    else:
        st.info("Start with the NOVA synthetic demo or upload three workbooks.")


if __name__ == "__main__":
    main()
