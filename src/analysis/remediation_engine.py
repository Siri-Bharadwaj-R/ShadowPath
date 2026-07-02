from collections import defaultdict


def generate_remediation_plan(attack_paths, graph_intelligence):
    """
    Generate prioritized remediation recommendations based on
    graph intelligence and attack path frequency.
    """

    node_frequency = graph_intelligence["node_frequency"]

    recommendations = []

    affected_paths = defaultdict(int)

    for path in attack_paths:

        visited = set()

        for node in path:

            if node not in visited:

                affected_paths[node] += 1
                visited.add(node)

    for node, count in affected_paths.items():

        priority = _priority(
            node,
            count,
            graph_intelligence
        )

        recommendations.append(
            {
                "node": node,
                "priority": priority,
                "affected_paths": count,
                "estimated_risk_reduction":
                    min(count * 15, 100),

                "recommendation":
                    _recommendation(node),

                "reason":
                    (
                        f"{node} appears in "
                        f"{count} attack path(s)."
                    )
            }
        )

    priority_order = {
        "Critical": 4,
        "High": 3,
        "Medium": 2,
        "Low": 1,
    }

    recommendations.sort(

        key=lambda item: (

            priority_order[item["priority"]],
            item["affected_paths"]

        ),

        reverse=True

    )

    return recommendations


# -----------------------------------------------------


def _priority(
    node,
    count,
    intelligence
):

    if node in intelligence["tier0_assets"]:
        return "Critical"

    if count >= 5:
        return "Critical"

    if count >= 3:
        return "High"

    if count >= 2:
        return "Medium"

    return "Low"


# -----------------------------------------------------


def _recommendation(node):

    return (
        f"Review memberships, delegated permissions "
        f"and administrative access associated with "
        f"{node}."
    )