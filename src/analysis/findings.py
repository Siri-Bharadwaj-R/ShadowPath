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

    # ============================
    # Attack Intelligence Engine
    # ============================

    blast_radius: int = 0

    attack_complexity: str = ""

    choke_points: list[str] = field(default_factory=list)

    lateral_movement: str = ""

    privilege_concentration: str = ""

    intelligence_summary: str = ""