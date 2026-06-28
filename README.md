# Server Monitoring Tool

Simple server monitoring tool built with Python and automated using systemd timer.

## Overview

This project monitors server conditions and generates reports automatically.

The tool:

* Reads server data from JSON
* Counts healthy and warning servers
* Detects the heaviest server load
* Stores change reports
* Stores heartbeat logs
* Runs automatically using systemd timer

---

## Features

### Health Monitoring

Checks CPU and RAM usage.

Rule:

* Healthy → CPU < 80 and RAM < 80
* Warning → CPU >= 80 or RAM >= 80

### Change Detection

Stores reports only when server status changes.

File:

```text
servers_report.json
```

### Heartbeat Logging

Stores every execution to confirm the monitor is alive.

File:

```text
heartbeat_report.json
```

### Automation

Runs automatically every 1 hour using:

```text
systemd
systemd timer
```

---

## Project Structure

```text
project/
│
├── server_monitoring_tool.py
├── servers.json
├── servers_report.json
├── heartbeat_report.json
├── server-monitor.service
└── server-monitor.timer
```

---

## Run Manually

```bash
python server_monitoring_tool.py
```

---

## Run Automatically

Reload systemd:

```bash
systemctl --user daemon-reload
```

Start timer:

```bash
systemctl --user start server-monitor.timer
```

Check timer:

```bash
systemctl --user list-timers
```

---

## Example Output

Heartbeat:

```json
[
{
"healthy": 1,
"warning": 3,
"timestamp": "11:02:20"
}
]
```

---

## What I Learned

* Python file handling
* JSON report generation
* Systemd service
* Systemd timer
* Monitoring concepts
* Debugging automation workflows

---

Built as a learning project.
Still learning and improving.

