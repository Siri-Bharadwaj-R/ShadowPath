from dataclasses import dataclass, field


@dataclass
class Finding:

    id: str

    path: list[str]

    score: int

    severity: str

    simulation: list[str] = field(default_factory=list)

    business_impact: str = ""

    attack_vector: str = ""

    description: str = ""

    recommendation: str = ""