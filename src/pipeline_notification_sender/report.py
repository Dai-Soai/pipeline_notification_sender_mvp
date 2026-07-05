from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from pipeline_notification_sender.models import DeliveryResult


def build_delivery_report(results: list[DeliveryResult]) -> dict[str, Any]:
    return {
        "artifact_type": "delivery_report",
        "version": "0.1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "summary": {
            "total": len(results),
            "delivered": sum(1 for item in results if item.status == "DELIVERED"),
            "failed": sum(1 for item in results if item.status == "FAILED"),
        },
        "deliveries": [
            {
                "notification_id": item.notification_id,
                "channel": item.channel,
                "recipient": item.recipient,
                "status": item.status,
                "detail": item.detail,
            }
            for item in results
        ],
    }
