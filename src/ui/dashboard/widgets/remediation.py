from rich.panel import Panel
from rich.table import Table

from ui.framework.palette import BORDER


def build_remediation(data):

    plan = data.remediation_plan

    table = Table(
        expand=True,
        show_header=True,
        header_style="bold bright_white"
    )

    table.add_column("Priority", width=10)
    table.add_column("Target", width=22)
    table.add_column("Impact", width=10)
    table.add_column("Recommendation")

    priority_colors = {
        "Critical": "bright_red",
        "High": "yellow",
        "Medium": "cyan",
        "Low": "green",
    }

    for item in plan[:5]:

        color = priority_colors.get(
            item["priority"],
            "white"
        )

        table.add_row(
            f"[{color}]{item['priority']}[/{color}]",
            item["node"],
            f"{item['affected_paths']} path(s)",
            item["recommendation"],
        )

    if not plan:

        table.add_row(
            "-",
            "No remediation actions",
            "-",
            "-"
        )

    return Panel(
        table,
        title="[bold bright_green]Top Remediation Actions[/bold bright_green]",
        border_style=BORDER,
        expand=True,
    )