def calculate_risk(path):
    """
    Calculate risk score for an attack path.
    """

    score = 0

    if "DomainAdmins" in path:
        score += 50

    if "ServerAdmins" in path:
        score += 20

    score += len(path) * 5

    if score >= 81:
        severity = "Critical"
    elif score >= 61:
        severity = "High"
    elif score >= 31:
        severity = "Medium"
    else:
        severity = "Low"

    return score, severity