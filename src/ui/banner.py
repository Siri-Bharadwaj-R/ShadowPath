from rich.align import Align
from rich.panel import Panel
from rich.text import Text


from .console import console
from .theme import banner_style


ASCII_LOGO = r"""
███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗
██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║
███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║
╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║
███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝
"""


def show_banner():
    banner = Text()

    banner.append(ASCII_LOGO + "\n", style="info")
    banner.append("ShadowPath\n", style="title")
    banner.append("──────────────────────────────────────────────\n", style="muted")
    banner.append("Active Directory Attack Simulation Platform\n", style="subtitle")
    banner.append("Version 1.0", style="muted")

    console.print(
        Panel(
            Align.center(banner),
            border_style="info",
            padding=(1, 2),
        )
    )