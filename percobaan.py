import json
import os
from datetime import datetime

data_os = os.environ
try:
    data_os["SERVER_FILE"]
except KeyError:
    data_os["SERVER_FILE"] = "servers.json"

nama_file = data_os["SERVER_FILE"]

# nama_file = data_os.get("SERVER_FILE", "servers.json")


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

    history.append(report)

    with open("servers_report.json", "w") as file:
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
