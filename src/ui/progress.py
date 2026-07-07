from rich.progress import (
    Progress,
    SpinnerColumn,
    TextColumn,
    BarColumn,
    TaskProgressColumn,
    TimeElapsedColumn,
    TimeRemainingColumn,
)

from .console import console


class ProgressManager:
    """
    Manages Rich progress bars for ShadowPath.

    This class provides a reusable interface for displaying
    progress throughout the application.
    """

    def __init__(self):
        self.progress = Progress(
            SpinnerColumn(),
            TextColumn("[title]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            TimeElapsedColumn(),
            TimeRemainingColumn(),
            console=console,
        )

    def start(self):
        """Start the progress display."""
        self.progress.start()

    def stop(self):
        """Stop the progress display."""
        self.progress.stop()

    def add_task(self, description: str, total: int):
        """Create a new progress task."""
        return self.progress.add_task(description, total=total)

    def advance(self, task_id, advance: int = 1):
        """Advance a task by the specified amount."""
        self.progress.advance(task_id, advance)


# Shared progress manager instance
progress_manager = ProgressManager()