import json
import os
from datetime import datetime


def load_servers(name_file):
    with open(name_file, "r") as file:
        data = json.load(file)

    return data


def count_health(servers):
    health = 0
    warning = 0
    for server in servers:
        if server["cpu"] < 80 and server["ram"] < 80:
            health += 1
        else:
            warning += 1

    count_dic = {"total": len(servers), "healthy": health, "warning": warning}
    return count_dic


def find_heaviest_server(servers):
    heaviest = 0
    # name_server = ""
    for server in servers:
        summation = server["cpu"] + server["ram"]
        if heaviest < summation:
            heaviest = summation
            # name_server = server["nama"]

            report_server = {
                "nama": server["nama"],
                "cpu": server["cpu"],
                "ram": server["ram"],
            }

    return report_server


def get_warning_server(servers):
    warnings = []
    for server in servers:
        if server["cpu"] >= 80 or server["ram"] >= 80:
            warning_server = {
                "nama": server["nama"],
                "cpu": server["cpu"],
                "ram": server["ram"],
            }
            warnings.append(warning_server)

    return warnings


def load_history():
    try:
        with open("servers_report.json", "r") as file:
            history = json.load(file)

    except FileNotFoundError:
        print("[WARNING] servers_report.json not found.")
        print("[INFO] Starting with empty history. ")
        history = []

    except json.JSONDecodeError:
        print("[WARNING] servers_report.json is corrupted.")
        print("[INFO] Starting with emptyhis")
        history = []

    if not isinstance(history, list):
        print("[WARNING] Invalid history structure.")
        history = []

    if not "timestamp" in history:
        print("[WARNING] History of no timestamp")

    return history


def is_changed_history(report, history):

    if not history:
        return True

    last_history = history[-1]
    copy_report = report.copy()
    copy_history = last_history.copy()

    if "timestamp" in history:
        del copy_history["timestamp"]

    if "timestamp" in report:
        del copy_report["timestamp"]

    return copy_history != copy_report


def save_report(report, changed, history):
    total_history = len(history)

    if changed:
        if total_history >= 5:
            del history[0]

        history.append(report)
        with open("server_report.json", "w") as file:
            json.dump(history, file)

    else:
        pass


def save_heartbeat(report):
    try:
        with open("heartbeat_report.json", "r") as file:
            history = json.load(file)

    except FileNotFoundError:
        history = []

    history.append(report)

    with open("heartbeat_report.json", "w") as file:
        json.dump(history, file)


def generate_alert(report):
    if report["warning"] >= 2:
        warnings = report["warning_servers"]
        print(f"[ALERT] \n{len(warnings)} servers need attention")

        for warning in warnings:
            print(f"-  {warning['nama']} (CPU {warning['cpu']} | RAM {warning['ram']})")

        heaviest = report["heaviest_server"]
        print(
            f"Heaviest server:\n{heaviest['nama']} (CPU {heaviest['cpu']} | RAM {heaviest['ram']})"
        )

    else:
        print("[OK]\nALL system healthy")


def main():
    nama_file = os.environ.get("SERVER_FILE", "servers.json")
    now = datetime.now()
    str_datetime = now.strftime("%H:%M:%S")

    servers = load_servers(nama_file)
    health = count_health(servers)
    heaviest = find_heaviest_server(servers)
    warning_server = get_warning_server(servers)

    health.update(
        {
            "warning_servers": warning_server,
            "heaviest_server": heaviest,
            "timestamp": str_datetime,
        }
    )

    history = load_history()
    changed = is_changed_history(health, history)
    save_report(health, changed, history)

    save_heartbeat(health)
    generate_alert(health)


# Test function

expected = {"total": 2, "healthy": 1, "warning": 1}

servers = [
    {"nama": "server-1", "cpu": 40, "ram": 50},
    {"nama": "server-2", "cpu": 90, "ram": 60},
]

result = count_health(servers)

assert expected == result

if __name__ == "__main__":
    main()
