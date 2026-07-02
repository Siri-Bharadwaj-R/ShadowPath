from rich.columns import Columns
from rich.text import Text

from ui.console import console

from ui.dashboard.widgets.overview import build_overview
from ui.dashboard.widgets.security_posture import build_security_posture
from ui.dashboard.widgets.attack_intelligence import build_attack_intelligence
from ui.dashboard.widgets.attack_cards import build_attack_cards
from ui.dashboard.widgets.recommendations import build_recommendations
from ui.dashboard.widgets.assessment import build_assessment


def render_dashboard(data):

    console.print()

    console.rule(
        "[bold bright_cyan]EXECUTIVE SECURITY DASHBOARD[/bold bright_cyan]"
    )

    console.print(
        Text(
            "ShadowPath Active Directory Attack Surface Assessment",
            style="italic bright_black",
            justify="center",
        )
    )

    console.print(
        Text(
            "Read-Only Active Directory Security Assessment",
            style="bright_black",
            justify="center",
        )
    )

    console.print()

    # ==========================================================
    # Environment Overview
    # ==========================================================

    console.rule(
        "[bold white]ENVIRONMENT OVERVIEW[/bold white]"
    )

    console.print()

    console.print(
        build_overview(data)
    )

    console.print()

    # ==========================================================
    # Security Posture
    # ==========================================================

    console.rule(
        "[bold white]SECURITY POSTURE[/bold white]"
    )

    console.print()

    console.print(
        build_security_posture(data)
    )

    console.print()

    # ==========================================================
    # Attack Intelligence
    # ==========================================================

    console.rule(
        "[bold bright_magenta]ATTACK INTELLIGENCE[/bold bright_magenta]"
    )

    console.print()

    console.print(
        build_attack_intelligence(data)
    )

    console.print()

    # ==========================================================
    # Attack Paths
    # ==========================================================

    console.rule(
        "[bold bright_red]TOP PRIVILEGE ESCALATION PATHS[/bold bright_red]"
    )

    console.print()

    console.print(
        build_attack_cards(data)
    )

    console.print()

    # ==========================================================
    # Executive Summary
    # ==========================================================

    console.rule(
        "[bold white]EXECUTIVE SUMMARY[/bold white]"
    )

    console.print()

    console.print(
        Columns(
            [
                build_recommendations(data),
                build_assessment(data),
            ],
            equal=True,
            expand=True,
        )
    )

    console.print()

    console.rule(
        "[bold green]ASSESSMENT COMPLETED SUCCESSFULLY[/bold green]"
    )

    console.print(
        Text(
            "ShadowPath completed the Active Directory security assessment successfully.",
            style="bright_black",
            justify="center",
        )
    )

    console.print()