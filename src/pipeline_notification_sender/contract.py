from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class NotificationItem:
    notification_id: str
    channel: str
    recipient: str
    subject: str
    message: str
    severity: str


REQUIRED_ITEM_FIELDS = {
    "notification_id",
    "channel",
    "recipient",
    "subject",
    "message",
    "severity",
}


def validate_notification_report(payload: dict[str, Any]) -> list[NotificationItem]:
    if not isinstance(payload, dict):
        raise ValueError("notification_report must be a JSON object")

    if payload.get("artifact_type") != "notification_report":
        raise ValueError("artifact_type must be notification_report")

    notifications = payload.get("notifications")
    if not isinstance(notifications, list):
        raise ValueError("notifications must be a list")

    result: list[NotificationItem] = []

    for index, item in enumerate(notifications):
        if not isinstance(item, dict):
            raise ValueError(f"notification item at index {index} must be an object")

        missing = REQUIRED_ITEM_FIELDS - set(item.keys())
        if missing:
            raise ValueError(
                f"notification item at index {index} missing fields: {sorted(missing)}"
            )

        result.append(
            NotificationItem(
                notification_id=str(item["notification_id"]),
                channel=str(item["channel"]),
                recipient=str(item["recipient"]),
                subject=str(item["subject"]),
                message=str(item["message"]),
                severity=str(item["severity"]),
            )
        )

    return result
