import os

print(os.getcwd())

from core.graph_builder import build_graph
from core.parser import load_relationships


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


if __name__ == "__main__":
    main()