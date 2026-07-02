from rich.align import Align
from rich.panel import Panel
from rich.text import Text

from ui.framework.palette import BORDER
from ui.framework.spacing import MEDIUM
from ui.framework.typography import HEADING


class StatusCard:

    def __init__(
        self,
        title: str,
        status: str,
        color: str = "green",
    ):
        self.title = title
        self.status = status
        self.color = color

    def render(self):

        body = Text()

        body.append(
            self.status,
            style=f"bold {self.color}"
        )

        return Panel(
            Align.center(body),
            title=f"[{HEADING}]{self.title}[/{HEADING}]",
            border_style=BORDER,
            padding=MEDIUM,
            expand=True,
        )