from dataclasses import dataclass


@dataclass
class Finding:
    id: str
    path: list[str]
    score: int
    severity: str