"""
ShadowPath Engine Models
"""

from dataclasses import dataclass
import networkx as nx

from ..analysis.findings import Finding



@dataclass
class EngineResult:
    """
    Result returned by the ShadowPath engine.
    """

    domain: str

    users: int
    groups: int
    relationships: int

    graph: nx.DiGraph

    attack_paths: list

    findings: list[Finding]

    summary: dict

    graph_intelligence: dict

    remediation_plan: dict