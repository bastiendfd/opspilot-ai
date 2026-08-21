"""Run deterministic analysis from a pack-local ingestion mapping."""

from __future__ import annotations

import json
from pathlib import Path

from src.analytics.service import AnalysisReport, analyze_workbooks


def _ingestion_options(source: dict[str, object]) -> dict[str, object]:
    return {
        "sheet_name": source["sheet_name"],
        "column_mapping": source["column_mapping"],
    }


def analyze_configured_pack(pack_directory: Path) -> AnalysisReport:
    """Load mapping.json from a synthetic data-fit pack and analyse its scenarios."""
    config = json.loads((pack_directory / "mapping.json").read_text(encoding="utf-8"))
    scenarios = config["scenarios"]
    return analyze_workbooks(
        actual_path=pack_directory / scenarios["actual"]["file"],
        budget_path=pack_directory / scenarios["budget"]["file"],
        forecast_path=pack_directory / scenarios["forecast"]["file"],
        actual_ingestion=_ingestion_options(scenarios["actual"]),
        budget_ingestion=_ingestion_options(scenarios["budget"]),
        forecast_ingestion=_ingestion_options(scenarios["forecast"]),
    )
