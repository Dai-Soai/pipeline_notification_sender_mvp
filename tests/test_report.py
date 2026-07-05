from pipeline_notification_sender.models import DeliveryResult
from pipeline_notification_sender.report import build_delivery_report


def test_build_delivery_report_success():
    results = [
        DeliveryResult(
            notification_id="notif-001",
            channel="console",
            recipient="ops",
            status="DELIVERED",
            detail="Simulated delivery.",
        )
    ]

    report = build_delivery_report(results)

    assert report["artifact_type"] == "delivery_report"
    assert report["version"] == "0.1.0"
    assert report["summary"]["total"] == 1
    assert report["summary"]["delivered"] == 1
    assert report["summary"]["failed"] == 0
    assert report["deliveries"][0]["notification_id"] == "notif-001"


def test_build_delivery_report_counts_failed_items():
    results = [
        DeliveryResult(
            notification_id="notif-001",
            channel="console",
            recipient="ops",
            status="DELIVERED",
            detail="Simulated delivery.",
        ),
        DeliveryResult(
            notification_id="notif-002",
            channel="console",
            recipient="ops",
            status="FAILED",
            detail="Simulated failure.",
        ),
    ]

    report = build_delivery_report(results)

    assert report["summary"]["total"] == 2
    assert report["summary"]["delivered"] == 1
    assert report["summary"]["failed"] == 1
