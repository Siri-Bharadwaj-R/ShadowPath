from rich.panel import Panel
from rich.table import Table

from ...framework.palette import BORDER


def build_attack_intelligence(data):

    intelligence = data.graph_intelligence

    stats = intelligence.get("graph_statistics", {})

    critical_nodes = intelligence.get("critical_nodes", [])

    tier0_assets = intelligence.get("tier0_assets", [])

    table = Table.grid(expand=True)

    table.add_column(ratio=1)
    table.add_column(ratio=1)

    table.add_row(
        "[bold bright_cyan]Attack Paths[/bold bright_cyan]",
        str(stats.get("attack_paths", 0))
    )

    table.add_row(
        "[bold bright_cyan]Entry Points[/bold bright_cyan]",
        str(stats.get("unique_entry_points", 0))
    )

    table.add_row(
        "[bold bright_cyan]Targets[/bold bright_cyan]",
        str(stats.get("unique_targets", 0))
    )

    table.add_row(
        "[bold bright_cyan]Average Path Length[/bold bright_cyan]",
        str(stats.get("average_path_length", 0))
    )

    table.add_row("", "")

    table.add_row(
        "[bold yellow]Highest Risk Hub[/bold yellow]",
        critical_nodes[0]["name"] if critical_nodes else "-"
    )

    table.add_row("", "")

    if tier0_assets:

        table.add_row(
            "[bold bright_red]Tier-0 Assets[/bold bright_red]",
            ", ".join(tier0_assets)
        )

    else:

        table.add_row(
            "[bold bright_red]Tier-0 Assets[/bold bright_red]",
            "None"
        )

    table.add_row("", "")

    table.add_row(
        "[bold white]Top Critical Nodes[/bold white]",
        ""
    )

    for node in critical_nodes[:5]:

        table.add_row(
            node["name"],
            f'{node["frequency"]} paths'
        )

    return Panel(
        table,
        title="[bold bright_magenta]Attack Intelligence[/bold bright_magenta]",
        border_style=BORDER,
        expand=True,
    )