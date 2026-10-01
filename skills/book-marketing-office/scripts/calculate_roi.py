#!/usr/bin/env python3
"""Calculate campaign and total book-marketing economics from CSV data."""

from __future__ import annotations

import argparse
import csv
import json
from decimal import Decimal, InvalidOperation
from pathlib import Path


NUMERIC_FIELDS = ("spend", "revenue", "variable_cost", "conversions", "customers")


def number(row: dict[str, str], key: str) -> Decimal:
    raw = (row.get(key) or "0").strip()
    try:
        return Decimal(raw)
    except InvalidOperation as exc:
        raise ValueError(f"Invalid {key!r} value {raw!r}") from exc


def ratio(numerator: Decimal, denominator: Decimal) -> float | None:
    return None if denominator == 0 else float(numerator / denominator)


def calculate(row: dict[str, str]) -> dict[str, object]:
    values = {key: number(row, key) for key in NUMERIC_FIELDS}
    profit = values["revenue"] - values["spend"] - values["variable_cost"]
    return {
        "campaign": row.get("campaign", ""),
        **{key: float(value) for key, value in values.items()},
        "contribution_profit": float(profit),
        "roas": ratio(values["revenue"], values["spend"]),
        "cac": ratio(values["spend"], values["customers"]),
        "cost_per_conversion": ratio(values["spend"], values["conversions"]),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="CSV with campaign, spend, revenue, variable_cost, conversions, customers")
    parser.add_argument("--pretty", action="store_true", help="Indent JSON output")
    args = parser.parse_args()

    with args.input.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    results = [calculate(row) for row in rows]
    totals = {key: sum((number(row, key) for row in rows), Decimal(0)) for key in NUMERIC_FIELDS}
    total_row = {"campaign": "TOTAL", **{key: str(value) for key, value in totals.items()}}
    payload = {"campaigns": results, "total": calculate(total_row)}
    print(json.dumps(payload, ensure_ascii=False, indent=2 if args.pretty else None, sort_keys=True))


if __name__ == "__main__":
    main()
