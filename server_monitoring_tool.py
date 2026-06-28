import json
import os
from datetime import datetime

data_os = os.environ

nama_file = data_os.get("SERVER_FILE", "servers.json")


def load_servers(file):
    with open(file, "r") as file:
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
    warning_server_name = []
    for server in servers:
        if server["cpu"] >= 80 or server["ram"] >= 80:
            warning_server_name.append(server["nama"])

    return warning_server_name


def save_report(report):
    try:
        with open("servers_report.json", "r") as file:
            history = json.load(file)

    except FileNotFoundError:
        history = []

    total_history = len(history)

    copy_report = report.copy()
    del copy_report["timestamp"]

    if not history:
        history.append(report)

    else:
        last_history = history[-1]
        copy_history = last_history.copy()
        del copy_history["timestamp"]

        if copy_history == copy_report:
            pass

        else:
            if total_history >= 5:
                del history[0]
            history.append(report)

    with open("servers_report.json", "w") as file:
        json.dump(history, file)


def save_heartbeat(report):
    try:
        with open("heartbeat_report.json", "r") as file:
            history = json.load(file)

    except FileNotFoundError:
        history = []

    history.append(report)

    with open("heartbeat_report.json", "w") as file:
        json.dump(history, file)


now = datetime.now()
str_datetime = now.strftime("%H:%M:%S")

# exec

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

save_report(health)
save_heartbeat(health)
