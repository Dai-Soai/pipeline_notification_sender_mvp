from pipeline_notification_sender.sender import send_notifications


def test_send_notifications_end_to_end_success():
    payload = {
        "artifact_type": "notification_report",
        "notifications": [
            {
                "notification_id": "notif-001",
                "channel": "console",
                "recipient": "ops",
                "subject": "Pipeline completed",
                "message": "Execution finished successfully.",
                "severity": "info",
            },
            {
                "notification_id": "notif-002",
                "channel": "console",
                "recipient": "dev",
                "subject": "Pipeline warning",
                "message": "Execution completed with warning.",
                "severity": "warning",
            },
        ],
    }

    report = send_notifications(payload)

    assert report["artifact_type"] == "delivery_report"
    assert report["summary"]["total"] == 2
    assert report["summary"]["delivered"] == 2
    assert report["summary"]["failed"] == 0
    assert report["deliveries"][0]["notification_id"] == "notif-001"
    assert report["deliveries"][1]["notification_id"] == "notif-002"
