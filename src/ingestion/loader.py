"""Deterministic Excel ingestion for the initial OpsPilot contract."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

IDENTIFIER_COLUMNS = (
    "transaction_id",
    "account",
    "cost_center",
    "business_unit",
    "material",
    "supplier",
    "purchase_order",
)


def _normalise_identifier(value: object) -> str:
    if pd.isna(value):
        return ""
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value).strip()


def ingest_workbook(
    workbook_path: Path,
    scenario: str,
    *,
    sheet_name: str = "Transactions",
    column_mapping: dict[str, str] | None = None,
) -> pd.DataFrame:
    """Load a scenario workbook, map source headers, and attach source lineage."""
    records = pd.read_excel(workbook_path, sheet_name=sheet_name)
    if column_mapping:
        missing_source_columns = sorted(set(column_mapping.values()) - set(records.columns))
        if missing_source_columns:
            raise ValueError(f"Mapped source columns not found: {', '.join(missing_source_columns)}.")
        records = records.rename(columns={source: canonical for canonical, source in column_mapping.items()})

    for column in IDENTIFIER_COLUMNS:
        if column in records.columns:
            records[column] = records[column].map(_normalise_identifier)

    records["scenario"] = scenario
    records["source_file"] = workbook_path.name
    records["source_sheet"] = sheet_name
    records["source_row"] = records.index + 2
    records["record_id"] = records.apply(
        lambda row: f"{row['source_file']}:{row['source_sheet']}:{row['source_row']}", axis=1
    )
    return records
