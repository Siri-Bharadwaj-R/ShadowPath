from core.graph_builder import build_graph
from core.parser import load_relationships
from analysis.attack_paths import find_attack_paths


def main():
    relationships = load_relationships(
        "../data/sample_domain.json"
    )

    print("Loaded Relationships:\n")

    for relationship in relationships:
        print(
            f"{relationship.source} -> {relationship.target}"
        )

    graph = build_graph(relationships)

    print("\nNodes:")
    print(list(graph.nodes()))

    print("\nEdges:")
    print(list(graph.edges()))

    attack_paths = find_attack_paths(graph)

    print("\nAttack Paths:")

    for path in attack_paths:
        print(" -> ".join(path))


if __name__ == "__main__":
    main()