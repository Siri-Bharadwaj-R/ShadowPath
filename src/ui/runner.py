from time import perf_counter

from rich.panel import Panel

from ui.console import console


class PipelineRunner:
    """
    Executes pipeline stages with consistent timing,
    logging and error handling.
    """

    def run_stage(self, title, function, *args, **kwargs):
        console.print()

        console.print(
            Panel.fit(
                f"[title]{title}[/title]",
                border_style="info"
            )
        )

        start = perf_counter()

        try:
            result = function(*args, **kwargs)

            elapsed = perf_counter() - start

            console.print(
                f"[success]✓ Completed[/success] "
                f"({elapsed:.2f}s)"
            )

            return result

        except Exception as e:

            elapsed = perf_counter() - start

            console.print(
                f"[error]✗ Failed[/error] "
                f"({elapsed:.2f}s)"
            )

            raise e


pipeline = PipelineRunner()