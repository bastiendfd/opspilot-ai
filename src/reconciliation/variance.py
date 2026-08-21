"""Deterministic Actual-versus-plan reconciliation with row-level lineage."""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

DIMENSIONS = ["account", "account_name", "cost_center"]


@dataclass(frozen=True)
class ReconciliationResult:
    total_actual: float
    total_plan: float
    total_variance: float
    variance_percent: float
    drilldown: pd.DataFrame


def _aggregate(records: pd.DataFrame, amount_column: str, ids_column: str) -> pd.DataFrame:
    return (
        records.groupby(DIMENSIONS, dropna=False, as_index=False)
        .agg(**{amount_column: ("amount", "sum"), ids_column: ("record_id", list)})
    )


def _as_list(value: object) -> list[str]:
    return value if isinstance(value, list) else []


def reconcile_actual_vs_plan(
    actual: pd.DataFrame, plan: pd.DataFrame, *, plan_name: str
) -> ReconciliationResult:
    """Compare Actual to a plan scenario and retain source IDs for every driver."""
    actual_grouped = _aggregate(actual, "actual_amount", "actual_record_ids")
    plan_grouped = _aggregate(plan, "plan_amount", "plan_record_ids")
    drilldown = actual_grouped.merge(plan_grouped, on=DIMENSIONS, how="outer")
    drilldown["actual_amount"] = drilldown["actual_amount"].fillna(0.0)
    drilldown["plan_amount"] = drilldown["plan_amount"].fillna(0.0)
    drilldown["actual_record_ids"] = drilldown["actual_record_ids"].map(_as_list)
    drilldown["plan_record_ids"] = drilldown["plan_record_ids"].map(_as_list)
    drilldown["variance_amount"] = drilldown["actual_amount"] - drilldown["plan_amount"]

    total_actual = float(actual["amount"].sum())
    total_plan = float(plan["amount"].sum())
    total_variance = total_actual - total_plan
    variance_percent = (total_variance / total_plan * 100) if total_plan else 0.0
    drilldown["contribution_percent"] = (
        drilldown["variance_amount"] / total_variance * 100 if total_variance else 0.0
    )
    drilldown["plan_name"] = plan_name
    drilldown = drilldown.sort_values("variance_amount", ascending=False, ignore_index=True)

    return ReconciliationResult(
        total_actual=total_actual,
        total_plan=total_plan,
        total_variance=total_variance,
        variance_percent=variance_percent,
        drilldown=drilldown,
    )
