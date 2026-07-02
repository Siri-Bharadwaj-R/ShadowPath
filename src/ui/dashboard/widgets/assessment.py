from rich.panel import Panel
from rich.text import Text


def build_assessment(data):
    summary = data.summary
    text = Text()

    if summary["critical"] > 0:
        text.append(
            "ShadowPath identified ",
            style="white",
        )

        text.append(
            f"{summary['critical']} critical ",
            style="bold bright_red",
        )

        text.append(
            "privilege escalation path(s) that could allow attackers to obtain elevated access if left unaddressed.\n\n",
            style="white",
        )

    elif summary["high"] > 0:
        text.append(
            "No critical attack paths were identified. ",
            style="green",
        )

        text.append(
            f"{summary['high']} high-risk path(s) ",
            style="bold yellow",
        )

        text.append(
            "should be reviewed and remediated to reduce the attack surface.\n\n",
            style="white",
        )

    else:
        text.append(
            "No critical or high-risk privilege escalation paths were identified during this assessment.\n\n",
            style="bold green",
        )

    text.append(
        "This assessment was performed in read-only mode. ShadowPath analyzed Active Directory relationships, delegated permissions, and nested group memberships without performing exploitation or making any changes to the environment.\n\n",
        style="cyan",
    )

    text.append(
        "Risk ratings are based on the likelihood of privilege escalation and the potential business impact if an attacker successfully traverses an identified attack path.\n\n",
        style="white",
    )

    text.append(
        "Prioritize remediation of Critical findings first, followed by High-risk attack paths, to reduce overall Active Directory exposure.",
        style="bold yellow",
    )

    return Panel(
        text,
        title="[bold bright_cyan]Executive Assessment[/bold bright_cyan]",
        border_style="bright_blue",
        padding=(1, 2),
        expand=True,
    )