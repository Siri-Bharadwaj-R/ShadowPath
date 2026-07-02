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

        info = Table.grid(expand=True)

        info.add_column(ratio=1)
        info.add_column(ratio=1)

        info.add_row(
            f"[bold]Severity[/bold]  [{severity_color}]{self.finding.severity.upper()}[/{severity_color}]",
            f"[bold]Score[/bold]  [bright_green]{self.finding.score}[/bright_green]"
        )

        info.add_row(
            f"[bold]Entry[/bold]  [bright_cyan]{self.finding.path[0]}[/bright_cyan]",
            f"[bold]Target[/bold]  [bright_magenta]{self.finding.path[-1]}[/bright_magenta]"
        )

        body = Group(

            info,

            Text(),

            Text(
                "Attack Path",
                style="bold white"
            ),

            Text(
                " → ".join(self.finding.path),
                style="white"
            ),

            Text(),

            Text(
                "Attack Simulation",
                style="bold bright_cyan"
            )
        )

        for index, step in enumerate(
            self.finding.simulation,
            start=1
        ):

            body.renderables.append(

                Text(
                    f"{index}. {step}",
                    style="white"
                )

            )
        body.renderables.append(Text())

        body.renderables.append(

            Text(
                "MITRE ATT&CK",
                style="bold bright_red"
            )

        )

        for technique in self.finding.mitre:
            body.renderables.append(

                Text(
                    f"{technique['id']}  {technique['description']}",
                    style="white"
                )

            )
        # ====================================================
        # Attack Intelligence
        # ====================================================

        body.renderables.append(Text())

        body.renderables.append(

            Text(
                "Attack Intelligence",
                style="bold bright_magenta"
            )

        )

        intelligence = Table.grid(expand=True)

        intelligence.add_column(ratio=1)
        intelligence.add_column(ratio=1)

        intelligence.add_row(
            f"[bold]Blast Radius[/bold]  {self.finding.blast_radius}",
            f"[bold]Complexity[/bold]  {self.finding.attack_complexity}"
        )

        intelligence.add_row(
            f"[bold]Lateral Movement[/bold]  {self.finding.lateral_movement}",
            f"[bold]Privilege Concentration[/bold]  {self.finding.privilege_concentration}"
        )

        choke_points = (
            ", ".join(self.finding.choke_points)
            if self.finding.choke_points
            else "None"
        )

        intelligence.add_row(
            f"[bold]Choke Points[/bold]  {choke_points}",
            ""
        )

        body.renderables.append(intelligence)

        body.renderables.append(Text())

        body.renderables.append(

            Text(
                "Analyst Assessment",
                style="bold bright_yellow"
            )

        )

        body.renderables.append(

            Text(
                self.finding.intelligence_summary,
                style="white"
            )

        )

        return Panel(
            body,
            title=f"[bold bright_cyan]{self.finding.id}[/bold bright_cyan]",
            border_style=BORDER,
            padding=(1, 2),
            expand=True,
        )


def build_attack_cards(data):

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

                (
                    f"[bold]{len(findings)-3} additional finding(s)[/bold]\n\n"
                    "See the generated report for the complete assessment."
                ),

                title="[bold]Additional Findings[/bold]",

                border_style=BORDER,

                expand=True,

            )

        )

    return Group(*cards)