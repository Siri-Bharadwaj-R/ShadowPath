import networkx as nx


PRIVILEGED_TARGETS = {
    "DomainAdmins"
}


def find_attack_paths(graph: nx.DiGraph):
    attack_paths = []

    for source in graph.nodes():

        for target in PRIVILEGED_TARGETS:

            if target not in graph.nodes():
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