from ui.console import console


def success(message: str):
    console.print(f"[success]✓[/success] {message}")


def info(message: str):
    console.print(f"[info]ℹ[/info] {message}")


def warning(message: str):
    console.print(f"[warning]⚠[/warning] {message}")


def error(message: str):
    console.print(f"[error]✗[/error] {message}")