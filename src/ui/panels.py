from rich.panel import Panel

from .console import console


def show_panel(title: str, content: str):
    console.print(
        Panel(
            content,
            title=title,
            border_style="info",
            expand=False,
        )
    )