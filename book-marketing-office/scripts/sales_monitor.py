#!/usr/bin/env python3
"""Compare the latest sales window with the preceding window and flag changes."""

from __future__ import annotations

import argparse
import csv
from datetime import date, timedelta
from decimal import Decimal
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="CSV with date, units, revenue")
    parser.add_argument("--window", type=int, default=7, help="Days per comparison window")
    parser.add_argument("--change-threshold", type=Decimal, default=Decimal("0.25"), help="Absolute relative-change alert threshold")
    args = parser.parse_args()
    if args.window < 1:
        raise ValueError("window must be positive")
    if args.change_threshold < 0:
        raise ValueError("change-threshold must be non-negative")

    daily: dict[date, dict[str, Decimal]] = {}
    with args.input.open(encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            day = date.fromisoformat(row["date"])
            bucket = daily.setdefault(day, {"units": Decimal(0), "revenue": Decimal(0)})
            bucket["units"] += Decimal(row.get("units") or "0")
            bucket["revenue"] += Decimal(row.get("revenue") or "0")
    if not daily:
        raise ValueError("input contains no data rows")

    end = max(daily)
    current_start = end - timedelta(days=args.window - 1)
    prior_start = current_start - timedelta(days=args.window)
    prior_end = current_start - timedelta(days=1)

    def total(start: date, finish: date, field: str) -> Decimal:
        return sum((values[field] for day, values in daily.items() if start <= day <= finish), Decimal(0))

    payload: dict[str, object] = {
        "current_period": [current_start.isoformat(), end.isoformat()],
        "prior_period": [prior_start.isoformat(), prior_end.isoformat()],
        "metrics": {},
        "alerts": [],
    }
    for field in ("units", "revenue"):
        current = total(current_start, end, field)
        prior = total(prior_start, prior_end, field)
        change = None if prior == 0 else (current - prior) / prior
        payload["metrics"][field] = {"current": float(current), "prior": float(prior), "relative_change": None if change is None else float(change)}
        if change is not None and abs(change) >= args.change_threshold:
            payload["alerts"].append({"metric": field, "direction": "up" if change > 0 else "down", "relative_change": float(change)})
    print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
