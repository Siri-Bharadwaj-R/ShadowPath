import networkx as nx

from core.models import Relationship


def build_graph(relationships: list[Relationship]) -> nx.DiGraph:
    """
    Build a directed graph from relationships.
    """

    graph = nx.DiGraph()

    for relationship in relationships:
        graph.add_edge(
            relationship.source,
            relationship.target
        )

    return graph