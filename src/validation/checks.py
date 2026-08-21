"""Fail-closed validation for initial canonical records."""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

REQUIRED_COLUMNS = ("transaction_id", "scenario", "period", "amount", "currency", "account", "cost_center")


@dataclass(frozen=True)
class ValidationFinding:
    code: str
    severity: str
    message: str
    record_ids: tuple[str, ...]


def _record_ids(records: pd.DataFrame) -> tuple[str, ...]:
    if "record_id" not in records.columns:
        return ()
    return tuple(records["record_id"].astype(str).tolist())


def _is_missing(series: pd.Series) -> pd.Series:
    return series.isna() | series.astype(str).str.strip().eq("")


def validate_records(
    records: pd.DataFrame, *, allowed_accounts: set[str] | None = None
) -> list[ValidationFinding]:
    """Return blocking deterministic data-quality findings; never repair financial data."""
    findings: list[ValidationFinding] = []

    missing_columns = [column for column in REQUIRED_COLUMNS if column not in records.columns]
    if missing_columns:
        findings.append(
            ValidationFinding(
                code="missing_required_column",
                severity="blocking",
                message=f"Required columns missing: {', '.join(missing_columns)}.",
                record_ids=(),
            )
        )
        return findings

    for column in REQUIRED_COLUMNS:
        missing = records.loc[_is_missing(records[column])]
        if not missing.empty:
            findings.append(
                ValidationFinding(
                    code="missing_required_value",
                    severity="blocking",
                    message=f"Required value missing in column '{column}'.",
                    record_ids=_record_ids(missing),
                )
            )

    duplicates = records.loc[
        records["transaction_id"].astype(str).str.strip().ne("")
        & records["transaction_id"].duplicated(keep=False)
    ]
    if not duplicates.empty:
        findings.append(
            ValidationFinding(
                code="duplicate_transaction_id",
                severity="blocking",
                message="Duplicate transaction IDs detected.",
                record_ids=_record_ids(duplicates),
            )
        )

    currencies = sorted(records["currency"].dropna().astype(str).str.strip().unique())
    if len(currencies) > 1:
        findings.append(
            ValidationFinding(
                code="inconsistent_currency",
                severity="blocking",
                message=f"More than one currency found: {', '.join(currencies)}.",
                record_ids=_record_ids(records),
            )
        )

    if allowed_accounts is not None:
        normalized_allowed_accounts = {str(account).strip() for account in allowed_accounts}
        unmapped = records.loc[
            records["account"].astype(str).str.strip().ne("")
            & ~records["account"].astype(str).str.strip().isin(normalized_allowed_accounts)
        ]
        if not unmapped.empty:
            findings.append(
                ValidationFinding(
                    code="unmapped_account",
                    severity="blocking",
                    message="Accounts are not present in the supplied account mapping.",
                    record_ids=_record_ids(unmapped),
                )
            )

    return findings
