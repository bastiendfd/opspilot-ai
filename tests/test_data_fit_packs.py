import json
from pathlib import Path

from src.analytics.configured import analyze_configured_pack
from src.ingestion.loader import ingest_workbook
from src.synthetic.data_fit import generate_data_fit_packs
from src.validation.checks import validate_records


def test_five_heterogeneous_data_fit_packs_are_configurable_without_code_changes(
    tmp_path: Path,
) -> None:
    packs = generate_data_fit_packs(tmp_path)

    assert set(packs) == {"alpha", "bravo", "charlie", "delta", "echo"}
    for pack_name, pack_directory in packs.items():
        config = json.loads((pack_directory / "mapping.json").read_text(encoding="utf-8"))
        assert set(config["scenarios"]) == {"actual", "budget", "forecast"}, pack_name

        for scenario, source in config["scenarios"].items():
            records = ingest_workbook(
                pack_directory / source["file"],
                scenario=scenario,
                sheet_name=source["sheet_name"],
                column_mapping=source["column_mapping"],
            )
            assert validate_records(records) == [], f"{pack_name}/{scenario}"
            assert records["source_sheet"].iloc[0] == source["sheet_name"]


def test_configured_analysis_runs_across_all_five_data_fit_packs(tmp_path: Path) -> None:
    packs = generate_data_fit_packs(tmp_path)

    for pack_name, pack_directory in packs.items():
        report = analyze_configured_pack(pack_directory)

        assert report.blocked is False, pack_name
        assert report.insight is not None, pack_name
        assert report.insight.variance_amount == 184_320, pack_name
