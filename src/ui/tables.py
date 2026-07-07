from rich.table import Table

from .console import console


def show_attack_paths(findings):
    table = Table(
        title="Attack Findings",
        show_lines=True
    )

    table.add_column("Entry Point", style="cyan")
    table.add_column("Target", style="yellow")
    table.add_column("Severity", style="red")
    table.add_column("Risk", justify="right")

    for finding in findings:

        table.add_row(
            finding.path[0],
            finding.path[-1],
            finding.severity,
            str(finding.score),
        )

    console.print(table)