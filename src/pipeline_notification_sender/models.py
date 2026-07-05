from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DeliveryResult:
    notification_id: str
    channel: str
    recipient: str
    status: str
    detail: str
