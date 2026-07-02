MITRE_TECHNIQUES = {
    "T1078": {
        "name": "Valid Accounts",
        "description": "Valid Accounts used to access Active Directory."
    },
    "T1098": {
        "name": "Account Manipulation",
        "description": "Privilege inheritance through group membership."
    },
    "T1484": {
        "name": "Domain Policy Modification",
        "description": "Administrative control over Active Directory policy."
    },
    "T1068": {
        "name": "Privilege Escalation",
        "description": "Escalation through privileged administrative groups."
    },
    "T1021": {
        "name": "Remote Services",
        "description": "Lateral movement using inherited administrative access."
    },

    "T1070": {
        "name": "Indicator Removal",
        "description": "Service or administrative accounts may reduce attacker visibility."
    }
}


TIER0_GROUPS = {
    "Domain Admins",
    "Enterprise Admins",
    "Schema Admins",
    "Administrators",
    "SP-DomainAdmins",
}


ADMIN_GROUPS = {
    "ServerAdmins",
    "ITSupport",
    "BackupOperators",
    "HelpDesk",
}


SERVICE_ACCOUNT_PREFIX = "svc_"


def generate_mitre_mapping(path):

    techniques = []

    added = set()

    def add(technique):

        if technique not in added:

            techniques.append({

                "id": technique,

                "name": MITRE_TECHNIQUES[technique]["name"],

                "description": MITRE_TECHNIQUES[technique]["description"]

            })

            added.add(technique)

    # --------------------------------------------------
    # Initial Access
    # --------------------------------------------------

    add("T1078")

    # --------------------------------------------------
    # Service Account
    # --------------------------------------------------

    if path[0].startswith(SERVICE_ACCOUNT_PREFIX):

        add("T1070")

    # --------------------------------------------------
    # Nested Groups / Account Manipulation
    # --------------------------------------------------

    admin_groups = [

        node

        for node in path

        if node in ADMIN_GROUPS

    ]

    if len(admin_groups) >= 2:

        add("T1098")

    # --------------------------------------------------
    # Privilege Escalation
    # --------------------------------------------------

    if any(

        node in TIER0_GROUPS

        for node in path

    ):

        add("T1068")

    # --------------------------------------------------
    # Domain Policy / Tier-0
    # --------------------------------------------------

    if any(

        node == "SP-DomainAdmins"

        or node == "Domain Admins"

        for node in path

    ):

        add("T1484")

    # --------------------------------------------------
    # Lateral Movement
    # --------------------------------------------------

    if len(admin_groups) >= 2:

        add("T1021")

    return techniques