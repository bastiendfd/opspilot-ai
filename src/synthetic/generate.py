"""Generate controlled, independent OpsPilot demo workbooks."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd


SCENARIO_FILENAMES = {
    "actual": "Actual.xlsx",
    "budget": "Budget.xlsx",
    "forecast": "Forecast.xlsx",
}

COLUMNS = [
    "transaction_id",
    "scenario",
    "period",
    "posting_date",
    "amount",
    "currency",
    "account",
    "account_name",
    "cost_center",
    "business_unit",
    "material",
    "supplier",
    "purchase_order",
    "po_created_date",
    "forecast_freeze_date",
]

FREEZE_DATE = "2026-06-15"


def _record(
    transaction_id: str,
    scenario: str,
    amount: float,
    account: str,
    account_name: str,
    cost_center: str,
    *,
    supplier: str = "",
    purchase_order: str = "",
    po_created_date: str = "",
) -> dict[str, Any]:
    return {
        "transaction_id": transaction_id,
        "scenario": scenario,
        "period": "2026-06",
        "posting_date": "2026-06-30",
        "amount": amount,
        "currency": "EUR",
        "account": account,
        "account_name": account_name,
        "cost_center": cost_center,
        "business_unit": "Industrial Systems",
        "material": "",
        "supplier": supplier,
        "purchase_order": purchase_order,
        "po_created_date": po_created_date,
        "forecast_freeze_date": FREEZE_DATE,
    }


def _actual_records() -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for index in range(47):
        amount = 2047.20 if index == 46 else 2046.80
        records.append(
            _record(
                f"ACT-CONS-{index + 1:03d}",
                "actual",
                amount,
                "640100",
                "External consulting services",
                "4130",
                supplier="NordConsult GmbH",
                purchase_order=f"PO-2026-41{index + 1:02d}",
                po_created_date="2026-06-20",
            )
        )

    records.extend(
        [
            _record(
                "ACT-CONS-048",
                "actual",
                303_800.00,
                "640100",
                "External consulting services",
                "4130",
                supplier="NordConsult GmbH",
                purchase_order="PO-2026-4001",
                po_created_date="2026-05-10",
            ),
            _record("ACT-TRAV-001", "actual", 50_670.00, "640200", "Travel and training", "4130"),
            _record("ACT-MAT-001", "actual", 1_030_000.00, "510000", "Direct materials", "3100"),
            _record("ACT-SAL-001", "actual", 810_000.00, "620000", "Production salaries", "3200"),
            _record("ACT-LOG-001", "actual", 261_610.00, "630000", "Inbound logistics", "3300"),
            _record("ACT-ADM-001", "actual", 40.00, "650000", "Administrative expenses", "3300"),
        ]
    )
    return records


def _plan_records(scenario: str, amounts: list[float]) -> list[dict[str, Any]]:
    definitions = [
        ("640100", "External consulting services", "4130"),
        ("640200", "Travel and training", "4130"),
        ("510000", "Direct materials", "3100"),
        ("620000", "Production salaries", "3200"),
        ("630000", "Inbound logistics", "3300"),
        ("650000", "Administrative expenses", "3300"),
    ]
    return [
        _record(
            f"{scenario.upper()[:3]}-PLAN-{index + 1:03d}",
            scenario,
            amount,
            account,
            account_name,
            cost_center,
        )
        for index, ((account, account_name, cost_center), amount) in enumerate(zip(definitions, amounts, strict=True))
    ]


def _write_workbook(path: Path, records: list[dict[str, Any]]) -> None:
    dataframe = pd.DataFrame(records, columns=COLUMNS)
    dataframe.to_excel(path, sheet_name="Transactions", index=False)


def generate_demo_workbooks(output_directory: Path) -> dict[str, Path]:
    """Create clean Actual, Budget and Forecast workbooks for NOVA INDUSTRIES."""
    output_directory.mkdir(parents=True, exist_ok=True)
    workbook_records = {
        "actual": _actual_records(),
        "budget": _plan_records("budget", [267_960, 50_000, 1_000_000, 800_000, 250_000, 40]),
        "forecast": _plan_records("forecast", [320_000, 51_000, 1_015_000, 805_000, 208_960, 40]),
    }
    generated: dict[str, Path] = {}
    for scenario, records in workbook_records.items():
        workbook_path = output_directory / SCENARIO_FILENAMES[scenario]
        _write_workbook(workbook_path, records)
        generated[scenario] = workbook_path
    return generated


def generate_quality_issue_workbooks(output_directory: Path) -> dict[str, Path]:
    """Create separate intentionally invalid workbooks for fail-closed QA tests."""
    clean_workbooks = generate_demo_workbooks(output_directory)

    actual = pd.read_excel(clean_workbooks["actual"])
    actual.loc[1, "transaction_id"] = actual.loc[0, "transaction_id"]
    actual.loc[2, "cost_center"] = None
    actual.loc[3, "currency"] = "USD"
    actual_path = output_directory / "Actual_quality_issues.xlsx"
    actual.to_excel(actual_path, sheet_name="Transactions", index=False)

    forecast = pd.read_excel(clean_workbooks["forecast"])
    forecast["account"] = forecast["account"].astype(str)
    forecast.loc[0, "account"] = "UNMAPPED"
    forecast_path = output_directory / "Forecast_mapping_issue.xlsx"
    forecast.to_excel(forecast_path, sheet_name="Transactions", index=False)

    return {
        "actual_quality_issues": actual_path,
        "forecast_mapping_issue": forecast_path,
    }
