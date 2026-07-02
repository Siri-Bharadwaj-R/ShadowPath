from collections import Counter
from typing import List


HIGH_PRIVILEGE_GROUPS = {
    "Domain Admins",
    "SP-DomainAdmins",
    "Enterprise Admins",
    "Administrators",
    "ServerAdmins",
}


def analyze_attack_path(path: List[str], all_paths: List[List[str]]) -> dict:
    """
    Performs intelligence analysis on a single attack path.

    Returns:
        {
            blast_radius,
            attack_complexity,
            choke_points,
            lateral_movement,
            privilege_concentration,
            intelligence_summary
        }
    """

    blast_radius = len(path)

    choke_points = _find_choke_points(path, all_paths)

    attack_complexity = _calculate_complexity(path)

    privilege_concentration = _calculate_privilege_concentration(path)

    lateral_movement = _calculate_lateral_movement(path)

    intelligence_summary = _generate_summary(
        blast_radius,
        attack_complexity,
        choke_points,
        lateral_movement,
        privilege_concentration,
    )

    return {
        "blast_radius": blast_radius,
        "attack_complexity": attack_complexity,
        "choke_points": choke_points,
        "lateral_movement": lateral_movement,
        "privilege_concentration": privilege_concentration,
        "intelligence_summary": intelligence_summary,
    }


def _find_choke_points(
    current_path: List[str],
    all_paths: List[List[str]],
) -> List[str]:

    counter = Counter()

    for path in all_paths:
        counter.update(path)

    choke_points = []

    for node in current_path:

        if counter[node] >= 2:
            choke_points.append(node)

    return choke_points


def _calculate_complexity(path: List[str]) -> str:

    length = len(path)

    if length <= 2:
        return "Very Low"

    if length == 3:
        return "Low"

    if length == 4:
        return "Moderate"

    if length == 5:
        return "High"

    return "Very High"


def _calculate_privilege_concentration(path: List[str]) -> str:

    privileged = sum(
        1
        for node in path
        if node in HIGH_PRIVILEGE_GROUPS
    )

    if privileged >= 3:
        return "Very High"

    if privileged == 2:
        return "High"

    if privileged == 1:
        return "Moderate"

    return "Low"


def _calculate_lateral_movement(path: List[str]) -> str:

    if len(path) >= 5:
        return "High"

    if len(path) >= 3:
        return "Moderate"

    return "Low"


def _generate_summary(
    blast_radius: int,
    complexity: str,
    choke_points: List[str],
    lateral: str,
    privilege: str,
) -> str:

    summary = []

    summary.append(
        f"This attack path affects {blast_radius} directory objects."
    )

    summary.append(
        f"Attack complexity is assessed as {complexity.lower()}."
    )

    summary.append(
        f"Lateral movement potential is {lateral.lower()}."
    )

    summary.append(
        f"Privilege concentration is {privilege.lower()}."
    )

    if choke_points:

        summary.append(
            "Critical choke point(s): "
            + ", ".join(choke_points)
            + "."
        )

    else:

        summary.append(
            "No significant choke points detected."
        )

    return " ".join(summary)