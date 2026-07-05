import pytest

from pipeline_notification_sender.contract import validate_notification_report


def test_validate_notification_report_success():
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
            }
        ],
    }

    items = validate_notification_report(payload)

    assert len(items) == 1
    assert items[0].notification_id == "notif-001"
    assert items[0].channel == "console"


def test_validate_notification_report_rejects_wrong_artifact_type():
    payload = {
        "artifact_type": "execution_report",
        "notifications": [],
    }

    with pytest.raises(ValueError, match="artifact_type"):
        validate_notification_report(payload)


def test_validate_notification_report_rejects_missing_notifications():
    payload = {
        "artifact_type": "notification_report",
    }

    with pytest.raises(ValueError, match="notifications"):
        validate_notification_report(payload)


def test_validate_notification_report_rejects_missing_item_field():
    payload = {
        "artifact_type": "notification_report",
        "notifications": [
            {
                "notification_id": "notif-001",
                "channel": "console",
            }
        ],
    }

    with pytest.raises(ValueError, match="missing fields"):
        validate_notification_report(payload)
