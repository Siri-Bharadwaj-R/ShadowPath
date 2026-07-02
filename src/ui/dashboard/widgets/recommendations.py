from rich.panel import Panel
from rich.text import Text


def build_recommendations(data):
    summary = data.summary
    text = Text()

    text.append("Immediate Actions\n", style="bold white")

    if summary["critical"] > 0:
        text.append(
            "• Investigate all Critical privilege escalation paths immediately.\n",
            style="bold bright_red",
        )

    if summary["high"] > 0:
        text.append(
            "• Review delegated administrative permissions.\n",
            style="yellow",
        )

    text.append(
        "• Audit nested group memberships.\n",
        style="green",
    )

    text.append(
        "• Verify ServerAdmins membership.\n",
        style="green",
    )

    text.append("\n")

    text.append("Security Improvements\n", style="bold white")

    text.append(
        "• Apply the Principle of Least Privilege.\n",
        style="green",
    )

    text.append(
        "• Remove unnecessary privileged group memberships.\n",
        style="green",
    )

    text.append(
        "• Enable continuous Active Directory monitoring.\n",
        style="green",
    )

    text.append(
        "• Review privileged service accounts regularly.",
        style="green",
    )

    return Panel(
        text,
        title="[bold bright_cyan]Recommendations[/bold bright_cyan]",
        border_style="bright_blue",
        padding=(1, 2),
        expand=True,
    )