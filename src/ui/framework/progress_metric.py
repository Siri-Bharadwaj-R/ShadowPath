from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from .palette import BORDER


class ProgressMetric:

    def __init__(
        self,
        title: str,
        score: int,
    ):
        self.title = title
        self.score = score

    def render(self):

        filled = max(0, min(20, self.score // 5))
        empty = 20 - filled

        if self.score >= 90:
            color = "green"
            posture = "Excellent"

        elif self.score >= 75:
            color = "bright_green"
            posture = "Good"

        elif self.score >= 60:
            color = "yellow"
            posture = "Fair"

        elif self.score >= 40:
            color = "bright_yellow"
            posture = "Poor"

        else:
            color = "bright_red"
            posture = "Critical"

        bar = (
            f"[{color}]"
            + "█" * filled
            + "[grey35]"
            + "░" * empty
        )

        table = Table.grid(expand=True)

        score_text = Text(
            f"{self.score}/100",
            style=f"bold {color}",
            justify="center",
        )

        posture_text = Text(
            posture,
            style=f"bold {color}",
            justify="center",
        )

        bar_text = Text.from_markup(bar)

        table.add_row(score_text)
        table.add_row(posture_text)
        table.add_row(bar_text)

        return Panel(
            table,
            title=f"[bold]{self.title}[/bold]",
            border_style=BORDER,
            padding=(1, 2),
            expand=True,
        )