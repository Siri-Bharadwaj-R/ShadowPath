from collections import Counter

from analysis.high_value_targets import HIGH_VALUE_TARGETS


def generate_graph_intelligence(graph, attack_paths):
    """
    Generate intelligence about the Active Directory attack graph.

    Returns a dictionary containing graph-wide intelligence that can
    later be consumed by the Dashboard, PDF, Business Impact Engine,
    Remediation Engine and MITRE Engine.
    """

    node_frequency = Counter()

    entry_points = set()

    targets = set()

    path_lengths = []

    for path in attack_paths:

        path_lengths.append(len(path))

        if path:
            entry_points.add(path[0])
            targets.add(path[-1])

        node_frequency.update(path)

    average_length = (
        round(sum(path_lengths) / len(path_lengths), 2)
        if path_lengths
        else 0
    )

    tier0_assets = []

    for node in graph.nodes:

        if node in HIGH_VALUE_TARGETS:
            tier0_assets.append(node)

    critical_nodes = []

    for node, frequency in node_frequency.items():

        if frequency > 1:

            critical_nodes.append(
                {
                    "name": node,
                    "frequency": frequency,
                }
            )

    critical_nodes.sort(
        key=lambda item: item["frequency"],
        reverse=True,
    )

    graph_statistics = {
        "attack_paths": len(attack_paths),
        "unique_entry_points": len(entry_points),
        "unique_targets": len(targets),
        "average_path_length": average_length,
        "graph_nodes": graph.number_of_nodes(),
        "graph_edges": graph.number_of_edges(),
    }

    return {
        "graph_statistics": graph_statistics,
        "critical_nodes": critical_nodes,
        "tier0_assets": tier0_assets,
        "node_frequency": dict(node_frequency),
    }