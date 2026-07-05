from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass

from pipeline_notification_sender.contract import NotificationItem


@dataclass(frozen=True)
class DeliveryResult:
    notification_id: str
    channel: str
    recipient: str
    status: str
    detail: str


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
