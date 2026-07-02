from rich.console import Group
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from ui.framework.palette import BORDER


class AttackCard:

    def __init__(self, finding):
        self.finding = finding

    def render(self):

        severity_colors = {
            "Critical": "bright_red",
            "High": "yellow",
            "Medium": "cyan",
            "Low": "green",
        }

        severity_color = severity_colors.get(
            self.finding.severity,
            "white"
        )

        info = Table.grid(
            expand=True
        )

        info.add_column(ratio=1)
        info.add_column(ratio=1)

        info.add_row(
            f"[bold]Severity[/bold]  [{severity_color}]{self.finding.severity.upper()}[/{severity_color}]",
            f"[bold]Score[/bold]  [bright_green]{self.finding.score}[/bright_green]",
        )

        info.add_row(
            f"[bold]Entry[/bold]  [bright_cyan]{self.finding.path[0]}[/bright_cyan]",
            f"[bold]Target[/bold]  [bright_magenta]{self.finding.path[-1]}[/bright_magenta]",
        )

        attack_path = Text()
        attack_path.append(
            "Attack Path\n",
            style="bold white"
        )

        attack_path.append(
            " → ".join(self.finding.path),
            style="white"
        )

        body = Group(
            info,
            Text(),
            attack_path,
        )

        return Panel(
            body,
            title=f"[bold bright_cyan]{self.finding.id}[/bold bright_cyan]",
            border_style=BORDER,
            padding=(1, 2),
            expand=True,
        )


def build_attack_cards(data):
    """
    Builds the highest-priority attack findings.
    """

    findings = data.findings

    if not findings:
        return Panel(
            "[green]No privilege escalation paths were identified.[/green]",
            title="[bold]Top Privilege Escalation Paths[/bold]",
            border_style=BORDER,
            expand=True,
        )

    cards = [
        AttackCard(finding).render()
        for finding in findings[:3]
    ]

    if len(findings) > 3:

        remaining = len(findings) - 3

        cards.append(
            Panel(
                (
                    f"[bold]{remaining} additional finding(s)[/bold]\n\n"
                    "See the generated report for the complete list of "
                    "prioritized attack paths."
                ),
                title="[bold]Additional Findings[/bold]",
                border_style=BORDER,
                expand=True,
            )
        )

    return Group(*cards)