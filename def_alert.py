def load_logs():
    with open("logs.txt", "r") as file:
        lines = file.readlines()
        return lines


def filter_alert(lines):
    filtered_line = ""
    for line in lines:
        if "WARNING" in line or "ERROR" in line:
            filtered_line += line

    return filtered_line


def save_alert(alerts):
    with open("alert.txt", "w") as file:
        file.write(alerts)


logs = load_logs()
alert = filter_alert(logs)
save_alert(alert)
