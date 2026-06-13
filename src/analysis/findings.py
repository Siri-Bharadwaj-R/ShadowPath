from dataclasses import dataclass


@dataclass
class Finding:
    path: list[str]
    score: int
    severity: str