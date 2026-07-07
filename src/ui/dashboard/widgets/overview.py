from rich.columns import Columns

from ...framework.metric_card import MetricCard


def build_overview(data):

    cards = [

        MetricCard(
            title="Domain",
            value=data.domain,
            subtitle="Active Directory"
        ).render(),

        MetricCard(
            title="Users",
            value=str(data.users)
        ).render(),

        MetricCard(
            title="Groups",
            value=str(data.groups)
        ).render(),

        MetricCard(
            title="Relationships",
            value=str(data.relationships)
        ).render(),

        MetricCard(
            title="Graph Nodes",
            value=str(data.graph_nodes)
        ).render(),

        MetricCard(
            title="Graph Edges",
            value=str(data.graph_edges)
        ).render(),

    ]

    return Columns(
        cards,
        equal=True,
        expand=True,
    )