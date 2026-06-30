HIGH_IMPACT_GROUPS = {
    "Domain Admins",
    "Enterprise Admins",
    "Schema Admins",
    "Administrators",
    "SP-DomainAdmins"
}

ELEVATED_GROUPS = {
    "ServerAdmins",
    "BackupOperators",
    "ITSupport"
}


def calculate_risk(path):
    score = 0

    # Highest privilege reached
    for node in path:
        if node in HIGH_IMPACT_GROUPS:
            score += 50

        elif node in ELEVATED_GROUPS:
            score += 20

    # Longer attack chains indicate broader privilege inheritance
    score += len(path) * 5

    # Low-privilege starting identities deserve higher attention
    if path and path[0] in {
        "intern01",
        "helpdesk01",
        "alice",
        "bob",
        "charlie",
        "svc_backup"
    }:
        score += 15

    score = min(score, 100)

    if score >= 80:
        severity = "Critical"
    elif score >= 60:
        severity = "High"
    elif score >= 40:
        severity = "Medium"
    else:
        severity = "Low"

    return score, severity