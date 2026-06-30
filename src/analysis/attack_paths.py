import networkx as nx

from analysis.high_value_targets import HIGH_VALUE_TARGETS
from analysis.entry_points import LOW_PRIVILEGE_IDENTITIES


def find_attack_paths(graph: nx.DiGraph):
    attack_paths = []

    for source in LOW_PRIVILEGE_IDENTITIES:

        if source not in graph:
            continue

        for target in HIGH_VALUE_TARGETS:

            if source == target:
                continue

            if target not in graph:
                continue

            if not nx.has_path(graph, source, target):
                continue

            paths = nx.all_simple_paths(
                graph,
                source=source,
                target=target
            )

            for path in paths:
                if len(path) > 1:
                    attack_paths.append(path)

    return attack_paths