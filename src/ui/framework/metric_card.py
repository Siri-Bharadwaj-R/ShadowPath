from rich.align import Align
from rich.panel import Panel
from rich.text import Text

from .palette import BORDER
from .spacing import MEDIUM
from .typography import HEADING


class MetricCard:

    def __init__(
        self,
        title: str,
        value: str,
        color: str = "bright_cyan",
        subtitle: str | None = None,
    ):
        self.title = title
        self.value = value
        self.color = color
        self.subtitle = subtitle

    def render(self):

        body = Text()

        body.append(
            f"{self.value}\n",
            style=f"bold {self.color}"
        )

        if self.subtitle:
            body.append(
                self.subtitle,
                style="grey70"
            )

        return Panel(
            Align.center(body),
            title=f"[{HEADING}]{self.title}[/{HEADING}]",
            border_style=BORDER,
            padding=MEDIUM,
            expand=True,
        )