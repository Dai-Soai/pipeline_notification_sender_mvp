# Pipeline Notification Sender MVP

RADAR Service Utility #21

Version: v0.1.0

## Overview

Pipeline Notification Sender reads a notification report,
simulates notification delivery,
and produces a delivery report artifact.

This MVP does not send real Telegram, Email, or Webhook notifications.

## Overview

Pipeline Notification Sender reads a notification report,
simulates notification delivery,
and produces a delivery report artifact.

This MVP does not send real Telegram, Email, or Webhook notifications.

## Pipeline

```text
notification_report.json
        │
        ▼
validate_notification_report()
        │
        ▼
FakeConsoleSender
        │
        ▼
DeliveryResult
        │
        ▼
build_delivery_report()
        │
        ▼
delivery_report.json
```

## Project Structure

```text
src/
    contract.py
    models.py
    sender.py
    report.py
    cli.py

tests/

samples/

reports/
```

## Module Responsibilities

### contract.py

Validate notification report.

### models.py

Shared data models.

### sender.py

Notification sender abstraction and fake sender.

### report.py

Generate delivery report artifact.

### cli.py

Command-line interface.

## Installation

```bash
python -m venv .venv
source .venv/bin/activate

pip install -e .
```

## CLI Usage

```bash
pipeline-notification-sender \
    samples/notification_report.json
```

Custom output:

```bash
pipeline-notification-sender \
    samples/notification_report.json \
    -o reports/delivery_report.json \
    --overwrite
```

Compact JSON:

```bash
pipeline-notification-sender \
    samples/notification_report.json \
    -o reports/delivery_report.compact.json \
    --compact \
    --overwrite
```

## Input Artifact

notification_report.json

## Output Artifact

delivery_report.json

## Responsibility

- Validate notification report
- Simulate delivery
- Produce delivery report
- CLI execution

## Not Responsibility

- Real Telegram delivery
- Real Email delivery
- Real Webhook delivery
- Retry strategy
- Runtime integration

