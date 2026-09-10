#!/usr/bin/env python3
"""Allocate conversion revenue across ordered marketing touches."""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from decimal import Decimal, InvalidOperation
from pathlib import Path
import sys


def weights(count: int, model: str) -> list[Decimal]:
    if model == "first":
        return [Decimal(1)] + [Decimal(0)] * (count - 1)
    if model == "last":
        return [Decimal(0)] * (count - 1) + [Decimal(1)]
    if model == "linear" or count == 1:
        return [Decimal(1) / count] * count
    if count == 2:
        return [Decimal("0.5"), Decimal("0.5")]
    middle = Decimal("0.2") / (count - 2)
    return [Decimal("0.4"), *([middle] * (count - 2)), Decimal("0.4")]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="CSV with conversion_id, revenue, channel, touch_id, timestamp")
    parser.add_argument("--model", choices=("first", "last", "linear", "position"), default="linear")
    parser.add_argument("--output", type=Path, help="Output CSV; stdout when omitted")
    args = parser.parse_args()

    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    with args.input.open(encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            grouped[row["conversion_id"]].append(row)

    output_rows = []
    for conversion_id, touches in grouped.items():
        touches.sort(key=lambda row: row.get("timestamp", ""))
        revenue_values = {row.get("revenue", "") for row in touches}
        if len(revenue_values) != 1:
            raise ValueError(f"Conversion {conversion_id!r} has inconsistent revenue values")
        try:
            revenue = Decimal(revenue_values.pop())
        except InvalidOperation as exc:
            raise ValueError(f"Conversion {conversion_id!r} has invalid revenue") from exc
        for touch, weight in zip(touches, weights(len(touches), args.model)):
            output_rows.append({
                "conversion_id": conversion_id,
                "touch_id": touch.get("touch_id", ""),
                "timestamp": touch.get("timestamp", ""),
                "channel": touch.get("channel", "unknown"),
                "model": args.model,
                "weight": f"{weight:.8f}",
                "attributed_revenue": f"{revenue * weight:.4f}",
            })

    fields = ["conversion_id", "touch_id", "timestamp", "channel", "model", "weight", "attributed_revenue"]
    if args.output:
        handle = args.output.open("w", encoding="utf-8", newline="")
    else:
        handle = sys.stdout
    try:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(output_rows)
    finally:
        if args.output:
            handle.close()


if __name__ == "__main__":
    main()
