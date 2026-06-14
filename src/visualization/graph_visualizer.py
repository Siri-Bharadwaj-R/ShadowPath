import matplotlib.pyplot as plt
import networkx as nx


def visualize_graph(graph):

    plt.figure(figsize=(10, 7))

    pos = nx.spring_layout(
        graph,
        seed=42,
        k=2
    )

    node_colors = []

    for node in graph.nodes():

        if node == "DomainAdmins":
            node_colors.append("red")

        elif node == "ServerAdmins":
            node_colors.append("orange")

        else:
            node_colors.append("skyblue")

    nx.draw_networkx_nodes(
        graph,
        pos,
        node_color=node_colors,
        node_size=2500,
        alpha=0.9
    )

    nx.draw_networkx_edges(
        graph,
        pos,
        edge_color="gray",
        arrows=True,
        arrowsize=25,
        width=2
    )

    nx.draw_networkx_labels(
        graph,
        pos,
        font_size=10,
        font_weight="bold"
    )

    plt.title(
        "ShadowPath Attack Path Analysis",
        fontsize=16,
        fontweight="bold"
    )

    plt.axis("off")

    plt.tight_layout()

    plt.savefig(
        "attack_graph.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()