from rich.theme import Theme

shadow_theme = Theme({
    "title": "bold bright_cyan",
    "subtitle": "bold white",

    "info": "cyan",
    "muted": "grey62",

    "success": "bold green",
    "warning": "bold yellow",
    "error": "bold red",

    "critical": "bold bright_red",
    "high": "red",
    "medium": "yellow",
    "low": "green",
})

# Style used by banner.py
banner_style = "bold bright_cyan"