import json

from pipeline_notification_sender.cli import main


def test_cli_writes_delivery_report(tmp_path, monkeypatch):
    input_path = tmp_path / "notification_report.json"
    output_path = tmp_path / "delivery_report.json"

    input_path.write_text(
        json.dumps(
            {
                "artifact_type": "notification_report",
                "notifications": [
                    {
                        "notification_id": "notif-001",
                        "channel": "console",
                        "recipient": "ops",
                        "subject": "Done",
                        "message": "Pipeline completed",
                        "severity": "info",
                    }
                ],
            }
        ),
        encoding="utf-8",
    )

    monkeypatch.setattr(
        "sys.argv",
        [
            "pipeline-notification-sender",
            str(input_path),
            "-o",
            str(output_path),
        ],
    )

    main()

    report = json.loads(output_path.read_text(encoding="utf-8"))

    assert output_path.exists()
    assert report["artifact_type"] == "delivery_report"
    assert report["summary"]["total"] == 1
    assert report["summary"]["delivered"] == 1
