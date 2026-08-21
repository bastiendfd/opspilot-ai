"""Generate structurally heterogeneous, synthetic data-fit packs."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from src.synthetic.generate import COLUMNS, _actual_records, _plan_records

BASE_RECORDS = {
    "actual": _actual_records,
    "budget": lambda: _plan_records("budget", [267_960, 50_000, 1_000_000, 800_000, 250_000, 40]),
    "forecast": lambda: _plan_records("forecast", [320_000, 51_000, 1_015_000, 805_000, 208_960, 40]),
}

PACK_SPECS = {
    "alpha": {
        "sheet_name": "Transactions",
        "headers": {
            "transaction_id": "transaction_id", "scenario": "scenario", "period": "period",
            "posting_date": "posting_date", "amount": "amount", "currency": "currency",
            "account": "account", "account_name": "account_name", "cost_center": "cost_center",
            "business_unit": "business_unit", "material": "material", "supplier": "supplier",
            "purchase_order": "purchase_order", "po_created_date": "po_created_date",
            "forecast_freeze_date": "forecast_freeze_date",
        },
    },
    "bravo": {
        "sheet_name": "GL Export",
        "headers": {
            "transaction_id": "Document No", "scenario": "Scenario", "period": "Fiscal Month",
            "posting_date": "Posting Date", "amount": "Booked EUR", "currency": "Curr.",
            "account": "G/L", "account_name": "G/L Description", "cost_center": "Cost centre",
            "business_unit": "Business Unit", "material": "Material", "supplier": "Vendor",
            "purchase_order": "PO Number", "po_created_date": "PO Created",
            "forecast_freeze_date": "Forecast Freeze",
        },
    },
    "charlie": {
        "sheet_name": "Buchungen",
        "headers": {
            "transaction_id": "Belegnummer", "scenario": "Szenario", "period": "Buchungsmonat",
            "posting_date": "Buchungsdatum", "amount": "Wert EUR", "currency": "Währung",
            "account": "Sachkonto", "account_name": "Kontobezeichnung", "cost_center": "Kostenstelle",
            "business_unit": "Geschäftsbereich", "material": "Materialnummer", "supplier": "Lieferant",
            "purchase_order": "Bestellung", "po_created_date": "Bestelldatum",
            "forecast_freeze_date": "Forecast-Stichtag",
        },
    },
    "delta": {
        "sheet_name": "Finance_Data",
        "headers": {
            "transaction_id": "Ref", "scenario": "Version", "period": "YYYY_MM",
            "posting_date": "Date", "amount": "Value", "currency": "Currency Code",
            "account": "Account Code", "account_name": "Account Label", "cost_center": "Responsibility Unit",
            "business_unit": "Entity", "material": "Product", "supplier": "Supplier Name",
            "purchase_order": "Purchasing Ref", "po_created_date": "PO Raised",
            "forecast_freeze_date": "Plan Cutoff",
        },
    },
    "echo": {
        "sheet_name": "Controle_Gestion",
        "headers": {
            "transaction_id": "Pièce", "scenario": "Scénario", "period": "Période",
            "posting_date": "Date comptable", "amount": "Montant", "currency": "Devise",
            "account": "Compte GL", "account_name": "Libellé compte", "cost_center": "Centre de coût",
            "business_unit": "Unité", "material": "Article", "supplier": "Fournisseur",
            "purchase_order": "Commande", "po_created_date": "Date commande",
            "forecast_freeze_date": "Gel prévision",
        },
    },
}


def generate_data_fit_packs(output_directory: Path) -> dict[str, Path]:
    """Create five three-workbook packs and a JSON mapping per pack."""
    output_directory.mkdir(parents=True, exist_ok=True)
    generated: dict[str, Path] = {}

    for pack_name, specification in PACK_SPECS.items():
        pack_directory = output_directory / pack_name
        pack_directory.mkdir(parents=True, exist_ok=True)
        scenario_config: dict[str, dict[str, object]] = {}
        for scenario, build_records in BASE_RECORDS.items():
            source_filename = f"{pack_name}_{scenario}.xlsx"
            dataframe = pd.DataFrame(build_records(), columns=COLUMNS)
            source_headers = specification["headers"]
            dataframe = dataframe.rename(columns=source_headers)
            dataframe.to_excel(pack_directory / source_filename, sheet_name=specification["sheet_name"], index=False)
            scenario_config[scenario] = {
                "file": source_filename,
                "sheet_name": specification["sheet_name"],
                "column_mapping": source_headers,
            }
        (pack_directory / "mapping.json").write_text(
            json.dumps({"pack_name": pack_name, "scenarios": scenario_config}, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        generated[pack_name] = pack_directory

    return generated
