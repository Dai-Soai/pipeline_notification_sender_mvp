from __future__ import annotations

import argparse
import json
from pathlib import Path

from pipeline_notification_sender.sender import send_notifications


def main() -> None:
    parser = argparse.ArgumentParser(description="Pipeline Notification Sender MVP")

    parser.add_argument(
        "input",
        help="Path to notification_report.json",
    )

    parser.add_argument(
        "--compact",
        action="store_true",
        help="Write compact JSON instead of pretty JSON",
    )

    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Allow overwriting existing output file",
    )

    parser.add_argument(
        "-o",
        "--output",
        default="reports/delivery_report.json",
        help="Path to output delivery_report.json",
    )

    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        raise SystemExit(f"Input file not found: {input_path}")

    if output_path.exists() and not args.overwrite:
        raise SystemExit(
            f"Output file already exists: {output_path}. Use --overwrite to replace it."
        )

    output_path.parent.mkdir(parents=True, exist_ok=True)

    payload = json.loads(input_path.read_text(encoding="utf-8"))
    report = send_notifications(payload)

    if args.compact:
        content = json.dumps(report, separators=(",", ":"))
    else:
        content = json.dumps(report, indent=2)

    output_path.write_text(content + "\n", encoding="utf-8")

    print(f"Delivery report written to {output_path}")
