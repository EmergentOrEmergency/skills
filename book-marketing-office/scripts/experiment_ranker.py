#!/usr/bin/env python3
"""Rank proposed marketing experiments with an explicit impact-confidence-ease-risk score."""

from __future__ import annotations

import argparse
import csv
from decimal import Decimal
from pathlib import Path
import sys


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="CSV with experiment_id, impact, confidence, ease, risk, cost")
    parser.add_argument("--output", type=Path, help="Output CSV; stdout when omitted")
    args = parser.parse_args()

    rows = []
    with args.input.open(encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            impact = Decimal(row["impact"])
            confidence = Decimal(row["confidence"])
            ease = Decimal(row["ease"])
            risk = Decimal(row.get("risk") or "0")
            cost = Decimal(row.get("cost") or "0")
            if any(value < 0 or value > 10 for value in (impact, confidence, ease, risk)):
                raise ValueError("impact, confidence, ease, and risk must be within 0..10")
            if cost < 0:
                raise ValueError("cost must be non-negative")
            score = impact * (confidence / 10) * ease / (Decimal(1) + risk / 10) / (Decimal(1) + cost)
            row["priority_score"] = f"{score:.6f}"
            rows.append(row)
    rows.sort(key=lambda row: Decimal(row["priority_score"]), reverse=True)

    fields = list(rows[0]) if rows else ["experiment_id", "impact", "confidence", "ease", "risk", "cost", "priority_score"]
    handle = args.output.open("w", encoding="utf-8", newline="") if args.output else sys.stdout
    try:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    finally:
        if args.output:
            handle.close()


if __name__ == "__main__":
    main()
