import json


def load_logs():
    with open("logs.txt", "r") as file:
        return file.readlines()


def filter_alerts(lines):
    filtered_line = []
    for line in lines:
        if "WARNING" in line or "ERROR" in line:
            filtered_line.append(line)

    return filtered_line


def generate_report(alerts):
    wr = 0
    err = 0
    for alert in alerts:
        if "WARNING" in alert:
            wr = wr + 1
        if "ERROR" in alert:
            err = err + 1

    report_dic = {"total_alert": len(alerts), "warning": wr, "error": err}
    return report_dic


def save_report(report):
    with open("report.json", "w") as file:
        json.dump(report, file)


logs = load_logs()
alert = filter_alerts(logs)
reports = generate_report(alert)
save_report(reports)
