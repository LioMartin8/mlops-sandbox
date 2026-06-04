import json
from datetime import datetime


def load_servers():
    with open("servers.json", "r") as file:
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
    with open("servers_report.json", "r") as file:
        history = json.load(file)

    history.append(report)

    with open("servers_report.json", "w") as file:
        json.dump(history, file)


now = datetime.now()
str_datetime = now.strftime("%H:%M:%S")

# exec

servers = load_servers()
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
