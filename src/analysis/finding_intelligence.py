from .findings import Finding


def enrich_finding(finding: Finding) -> Finding:
    """
    Enriches a finding with contextual intelligence.

    This module is responsible for adding
    business context and remediation guidance.
    """

    target = finding.path[-1]

    # -------------------------------------------------
    # Business Impact
    # -------------------------------------------------

    if target == "SP-DomainAdmins":
        finding.business_impact = (
            "Potential compromise of Domain Administration."
        )

    elif target == "ServerAdmins":
        finding.business_impact = (
            "Potential compromise of privileged server administration."
        )

    else:
        finding.business_impact = (
            "Potential privilege escalation."
        )

    # -------------------------------------------------
    # Attack Vector
    # -------------------------------------------------

    if len(finding.path) >= 4:
        finding.attack_vector = (
            "Nested Group Privilege Escalation"
        )

    else:
        finding.attack_vector = (
            "Direct Privileged Group Membership"
        )

    # -------------------------------------------------
    # Description
    # -------------------------------------------------

    finding.description = (
        "ShadowPath identified a privilege escalation path "
        "through Active Directory group relationships."
    )

    # -------------------------------------------------
    # Recommendation
    # -------------------------------------------------

    finding.recommendation = (
        "Review nested group memberships and apply the "
        "Principle of Least Privilege."
    )

    return finding