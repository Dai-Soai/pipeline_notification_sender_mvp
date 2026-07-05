from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from pipeline_notification_sender.contract import (
    NotificationItem,
    validate_notification_report,
)
from pipeline_notification_sender.models import DeliveryResult
from pipeline_notification_sender.report import build_delivery_report


class NotificationSender(ABC):

    @abstractmethod
    def send(self, notification: NotificationItem) -> DeliveryResult:
        raise NotImplementedError


class FakeConsoleSender(NotificationSender):

    def send(self, notification: NotificationItem) -> DeliveryResult:
        return DeliveryResult(
            notification_id=notification.notification_id,
            channel=notification.channel,
            recipient=notification.recipient,
            status="DELIVERED",
            detail="Simulated delivery.",
        )


def send_notifications(payload: dict[str, Any]) -> dict[str, Any]:
    notifications = validate_notification_report(payload)
    sender = FakeConsoleSender()

    results = [sender.send(notification) for notification in notifications]

    return build_delivery_report(results)
