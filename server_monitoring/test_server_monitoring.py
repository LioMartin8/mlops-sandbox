import json

from server_monitoring_tool import count_health, load_history


def test_count_health():
    servers = [
        {"nama": "server-1", "cpu": 40, "ram": 50},
        {"nama": "server-2", "cpu": 90, "ram": 60},
    ]

    result = count_health(servers)

    expected = {"total": 2, "healthy": 1, "warning": 1}

    assert result == expected


def test_load_history():

    result = load_history()

    with open("server_report.json", "r") as file:
        data = json.load(file)

    make_list = []
    make_list.append(data[-1])
    expected = make_list

    assert result == expected
