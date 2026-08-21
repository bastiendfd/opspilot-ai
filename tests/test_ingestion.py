from pathlib import Path

from src.ingestion.loader import ingest_workbook
from src.synthetic.generate import generate_demo_workbooks


def test_ingest_workbook_normalizes_dimensions_and_attaches_source_lineage(tmp_path: Path) -> None:
    workbooks = generate_demo_workbooks(tmp_path)

    records = ingest_workbook(workbooks["actual"], scenario="actual")

    assert len(records) == 53
    assert records.loc[0, "account"] == "640100"
    assert records.loc[0, "cost_center"] == "4130"
    assert records.loc[0, "source_file"] == "Actual.xlsx"
    assert records.loc[0, "source_sheet"] == "Transactions"
    assert records.loc[0, "source_row"] == 2
    assert records.loc[0, "record_id"] == "Actual.xlsx:Transactions:2"


def test_ingest_workbook_maps_heterogeneous_headers_and_sheet_name(tmp_path: Path) -> None:
    import pandas as pd

    source_path = tmp_path / "Plant_A_Actual.xlsx"
    pd.DataFrame(
        {
            "Document No": ["A-1001"],
            "Fiscal Month": ["2026-06"],
            "Booked EUR": [1250.50],
            "Curr.": ["EUR"],
            "G/L": ["640100"],
            "Cost centre": ["CC-4130"],
        }
    ).to_excel(source_path, sheet_name="GL Export", index=False)

    records = ingest_workbook(
        source_path,
        scenario="actual",
        sheet_name="GL Export",
        column_mapping={
            "transaction_id": "Document No",
            "period": "Fiscal Month",
            "amount": "Booked EUR",
            "currency": "Curr.",
            "account": "G/L",
            "cost_center": "Cost centre",
        },
    )

    assert records.loc[0, "transaction_id"] == "A-1001"
    assert records.loc[0, "account"] == "640100"
    assert records.loc[0, "cost_center"] == "CC-4130"
    assert records.loc[0, "amount"] == 1250.50
    assert records.loc[0, "source_sheet"] == "GL Export"
    assert records.loc[0, "record_id"] == "Plant_A_Actual.xlsx:GL Export:2"
