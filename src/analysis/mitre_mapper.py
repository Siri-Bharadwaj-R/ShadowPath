# src/analysis/mitre_mapper.py

MITRE_TECHNIQUES = {
    "DomainAdmins": [
        ("T1078", "Valid Accounts"),
        ("T1068", "Privilege Escalation")
    ],

    "ServerAdmins": [
        ("T1021", "Remote Services")
    ]
}


def map_mitre_techniques(path):

    techniques = []

    for node in path:

        if node in MITRE_TECHNIQUES:

            techniques.extend(
                MITRE_TECHNIQUES[node]
            )

    return techniques