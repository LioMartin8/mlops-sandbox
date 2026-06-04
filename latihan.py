def load_servers():
    servers = [
        {"nama": "server-1", "cpu": 20, "ram": 30},
        {"nama": "server-2", "cpu": 90, "ram": 20},
        {"nama": "server-3", "cpu": 10, "ram": 95},
        {"nama": "server-4", "cpu": 40, "ram": 50},
        {"nama": "server-5", "cpu": 99, "ram": 99},
    ]
    return servers


def find_heaviest_server(servers):
    heaviest = 0
    cpu = 0
    ram = 0
    nama = ""
    for server in servers:
        jumlah = server["cpu"] + server["ram"]
        if jumlah >= heaviest:
            heaviest = jumlah
            cpu = server["cpu"]
            ram = server["ram"]
            nama = server["nama"]

    report_server = {"nama": nama, "cpu": cpu, "ram": ram}
    return report_server


load = load_servers()
coba = find_heaviest_server(load)
print(coba)
