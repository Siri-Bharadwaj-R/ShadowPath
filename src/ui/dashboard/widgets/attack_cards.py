from rich.console import Group
from rich.panel import Panel
from rich.text import Text

from ui.framework.palette import BORDER


class AttackCard:

    def __init__(self, finding):
        self.finding = finding

    def render(self):

        body = Text()

        # Entry Identity
        body.append("Entry Identity\n", style="bold white")
        body.append(
            f"{self.finding.path[0]}\n\n",
            style="bold bright_cyan",
        )

        # Attack Chain
        body.append("Attack Chain\n", style="bold white")
        body.append(
            "  →  ".join(self.finding.path),
            style="white",
        )

        body.append("\n\n")

        # Target
        body.append("Target Asset\n", style="bold white")
        body.append(
            f"{self.finding.path[-1]}\n\n",
            style="bold bright_magenta",
        )

        # Risk
        body.append("Risk Assessment\n", style="bold white")
        body.append(
            f"Severity : {self.finding.severity}\n",
            style="bold bright_red",
        )
        body.append(
            f"Risk Score : {self.finding.score}",
            style="bold bright_green",
        )

        return Panel(
            body,
            title="[bold]Potential Privilege Escalation[/bold]",
            border_style=BORDER,
            padding=(1, 2),
            expand=True,
        )


def build_attack_cards(data):
    """
    Builds the Top Privilege Escalation Paths section.

    Displays the three highest-priority findings and informs the
    user if additional attack paths exist.
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
        cards.append(
            Panel(
                f"[cyan]...and {len(findings) - 3} additional attack path(s).[/cyan]",
                border_style=BORDER,
                expand=True,
            )
        )

    return Group(*cards)