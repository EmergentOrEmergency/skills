#!/usr/bin/env python3
"""Generate an import-ready content calendar from a JSON slot configuration."""

from __future__ import annotations

import argparse
import csv
from datetime import date, datetime, timedelta
import json
from pathlib import Path
import sys


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("config", type=Path, help="JSON with start_date, timezone, count, slots, pillars, objective")
    parser.add_argument("--output", type=Path, help="Output CSV; stdout when omitted")
    args = parser.parse_args()
    config = json.loads(args.config.read_text(encoding="utf-8"))
    start = date.fromisoformat(config["start_date"])
    slots = config["slots"]
    pillars = config.get("pillars") or [""]
    count = int(config["count"])
    if not slots or count < 1:
        raise ValueError("slots must be non-empty and count must be positive")
    if any(int(slot["weekday"]) not in range(7) for slot in slots):
        raise ValueError("slot weekday must be an integer from 0 (Monday) to 6 (Sunday)")

    rows = []
    day = start
    while len(rows) < count:
        for slot in slots:
            if len(rows) >= count:
                break
            if day.weekday() != int(slot["weekday"]):
                continue
            index = len(rows)
            scheduled = datetime.fromisoformat(f"{day.isoformat()}T{slot['time']}")
            rows.append({
                "content_id": f"CNT-{index + 1:04d}",
                "datetime": scheduled.isoformat(timespec="minutes"),
                "timezone": config["timezone"],
                "channel": slot["channel"],
                "pillar": pillars[index % len(pillars)],
                "objective": config.get("objective", ""),
                "audience": config.get("audience", ""),
                "hook": "",
                "body_or_script": "",
                "creative_brief": "",
                "cta": "",
                "destination": "",
                "utm": "",
                "experiment_id": config.get("experiment_id", ""),
                "approval_state": "draft",
                "external_status": "not_submitted",
                "external_id": "",
            })
        day += timedelta(days=1)

    fields = list(rows[0])
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
