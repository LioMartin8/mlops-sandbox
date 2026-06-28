import json

with open("server_report.json", "r") as file:
    data = json.load(file)
    print(len(data))
