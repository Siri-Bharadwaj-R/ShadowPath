from rich.panel import Panel
from rich.table import Table

from ui.framework.palette import BORDER


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

        if self.score >= 80:
            color = "green"
        elif self.score >= 50:
            color = "yellow"
        else:
            color = "bright_red"

        bar = (
            f"[{color}]"
            + "█" * filled
            + "[grey35]"
            + "░" * empty
        )

        table = Table.grid()

        table.add_row(
            f"[bold]{self.score}/100[/bold]"
        )

        table.add_row(bar)

        return Panel(
            table,
            title=f"[bold]{self.title}[/bold]",
            border_style=BORDER,
            expand=True,
        )