import matplotlib.pyplot as plt
import networkx as nx


def visualize_graph(graph):

    plt.style.use("dark_background")

    plt.figure(figsize=(22, 14), facecolor="#0d1117")

    # Better layout
    pos = nx.kamada_kawai_layout(graph)

    scale = 2.6

    for node in pos:
        x, y = pos[node]
        pos[node] = (x * scale, y * scale)

    tier0 = {
        "DomainAdmins",
        "SP-DomainAdmins",
        "Enterprise Admins",
        "Schema Admins",
        "Administrators",
    }

    privileged = {
        "ServerAdmins",
        "ITSupport",
        "BackupOperators",
        "HelpDesk",
    }

    node_colors = []
    node_sizes = []

    for node in graph.nodes():

        if node in tier0:
            node_colors.append("#ff4d6d")
            node_sizes.append(2600)

        elif node in privileged:
            node_colors.append("#ffb347")
            node_sizes.append(2300)

        elif str(node).lower().startswith("svc"):
            node_colors.append("#00d084")
            node_sizes.append(2100)

        else:
            node_colors.append("#5dade2")
            node_sizes.append(2000)

    nx.draw_networkx_edges(
        graph,
        pos,
        edge_color="#95a5a6",
        width=1.6,
        alpha=0.55,
        arrows=True,
        arrowsize=18,
        arrowstyle="-|>",
        connectionstyle="arc3,rad=0.03",
    )

    nx.draw_networkx_nodes(
        graph,
        pos,
        node_color=node_colors,
        node_size=node_sizes,
        edgecolors="white",
        linewidths=1.6,
    )

    nx.draw_networkx_labels(
        graph,
        pos,
        font_size=9,
        font_weight="bold",
        font_color="white",
        font_family="sans-serif",
    )

    plt.title(
        "ShadowPath Active Directory Attack Graph",
        fontsize=24,
        fontweight="bold",
        color="white",
        pad=25,
    )

    plt.figtext(
        0.5,
        0.02,
        "Red = Tier-0 Assets   |   Orange = Privileged Groups   |   Green = Service Accounts   |   Blue = Standard Users / Groups",
        ha="center",
        fontsize=11,
        color="#bfc9ca",
    )

    plt.margins(0.25)

    plt.axis("off")

    plt.tight_layout()

    plt.savefig(
        "attack_graph.png",
        dpi=300,
        facecolor="#0d1117",
        bbox_inches="tight",
    )

    #plt.show()