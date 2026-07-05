from pipeline_notification_sender.contract import NotificationItem
from pipeline_notification_sender.sender import FakeConsoleSender


def test_fake_console_sender_returns_delivery_result():

    sender = FakeConsoleSender()

    notification = NotificationItem(
        notification_id="notif-001",
        channel="console",
        recipient="ops",
        subject="Done",
        message="Pipeline completed",
        severity="info",
    )

    result = sender.send(notification)

    assert result.notification_id == "notif-001"
    assert result.status == "DELIVERED"
    assert result.channel == "console"
