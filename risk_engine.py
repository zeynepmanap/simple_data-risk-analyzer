def calculate_risk(data):
    risk = 0

    if data["password"] == "weak":
        risk += 25
    elif data["password"] == "medium":
        risk += 10

    if data["two_factor"] == "no":
        risk += 15

    risk += int(data["open_ports"]) * 4

    if data["updated"] == "no":
        risk += 15

    if data["encrypted"] == "no":
        risk += 20

    if data["access_control"] == "no":
        risk += 10

    if data["log_monitoring"] == "no":
        risk += 10

    if risk < 40:
        level = "Low"
    elif risk < 70:
        level = "Medium"
    else:
        level = "Critical"

    return risk, level
