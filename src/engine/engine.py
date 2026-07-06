"""
ShadowPath Engine

Enterprise backend orchestration layer.
"""

from typing import Callable

from ..ad.ldap_collector import LDAPCollector
from ..ad.relationship_builder import RelationshipBuilder

from ..core.graph_builder import build_graph

from ..analysis.attack_paths import find_attack_paths
from ..analysis.path_prioritizer import prioritize_attack_paths
from ..analysis.risk_engine import calculate_risk
from ..analysis.attack_simulator import generate_attack_simulation
from ..analysis.mitre_engine import generate_mitre_mapping
from ..analysis.intelligence_engine import generate_graph_intelligence
from ..analysis.remediation_engine import generate_remediation_plan
from ..analysis.security_summary import generate_security_summary
from ..analysis.findings import Finding
from .models import EngineResult


class ShadowPathEngine:

    def __init__(
        self,
        server_ip: str,
        username: str,
        password: str,
        base_dn: str,
        progress_callback: Callable[[str, int], None] | None = None,
    ):

        self.collector = LDAPCollector(
            server_ip=server_ip,
            username=username,
            password=password,
            base_dn=base_dn,
        )

        self.progress_callback = progress_callback

    # =========================================================

    def update_progress(
        self,
        stage: str,
        percent: int,
    ):

        if self.progress_callback:
            self.progress_callback(stage, percent)

    # =========================================================

    def connect(self):

        self.update_progress(
            "Connecting to Active Directory",
            5,
        )

        self.collector.connect()

    # =========================================================

    def collect_relationships(self):

        self.update_progress(
            "Collecting Relationships",
            15,
        )

        builder = RelationshipBuilder(
            self.collector
        )

        return builder.build()

    # =========================================================

    def build_graph(self, relationships):

        self.update_progress(
            "Building Attack Graph",
            30,
        )

        return build_graph(
            relationships
        )

    # =========================================================

    def discover_attack_paths(self, graph):

        self.update_progress(
            "Discovering Attack Paths",
            45,
        )

        attack_paths = find_attack_paths(
            graph
        )

        attack_paths = prioritize_attack_paths(
            attack_paths
        )

        return attack_paths

    # =========================================================

    # =========================================================

    def analyze_attack_paths(
        self,
        graph,
        attack_paths,
    ):

        self.update_progress(
            "Generating Attack Intelligence",
            60,
        )

        graph_intelligence = generate_graph_intelligence(
            graph,
            attack_paths,
        )

        self.update_progress(
            "Generating Remediation Plan",
            70,
        )

        remediation_plan = generate_remediation_plan(
            attack_paths,
            graph_intelligence,
        )

        findings = []

        for index, path in enumerate(
            attack_paths,
            start=1,
        ):

            findings.append(
                self._build_finding(
                    index,
                    path,
                    graph_intelligence,
                )
            )

        return (
            findings,
            graph_intelligence,
            remediation_plan,
        )

    # =========================================================
    # =========================================================

    def _build_finding(
        self,
        index,
        path,
        graph_intelligence,
    ) -> Finding:

        score, severity = calculate_risk(path)

        finding = Finding(
            id=f"SP-{index:03}",
            path=path,
            score=score,
            severity=severity,
        )

        # =====================================================
        # Attack Simulation
        # =====================================================

        finding.simulation = generate_attack_simulation(
            path
        )

        # =====================================================
        # MITRE Mapping
        # =====================================================

        finding.mitre = generate_mitre_mapping(
            path
        )

        # =====================================================
        # Blast Radius
        # =====================================================

        finding.blast_radius = len(path)

        # =====================================================
        # Attack Complexity
        # =====================================================

        if len(path) <= 2:
            finding.attack_complexity = "Very Low"

        elif len(path) == 3:
            finding.attack_complexity = "Low"

        elif len(path) == 4:
            finding.attack_complexity = "Moderate"

        elif len(path) == 5:
            finding.attack_complexity = "High"

        else:
            finding.attack_complexity = "Very High"

        # =====================================================
        # Shared Privilege Nodes
        # =====================================================

        shared_nodes = []

        for node in path:

            frequency = (
                graph_intelligence[
                    "node_frequency"
                ].get(node, 0)
            )

            if frequency > 1:
                shared_nodes.append(node)

        finding.choke_points = shared_nodes

        # =====================================================
        # Lateral Movement
        # =====================================================

        if len(shared_nodes) >= 3:
            finding.lateral_movement = "High"

        elif len(shared_nodes) >= 1:
            finding.lateral_movement = "Moderate"

        else:
            finding.lateral_movement = "Low"

        # =====================================================
        # Privilege Concentration
        # =====================================================

        privileged = 0

        for node in path:

            if node in graph_intelligence[
                "tier0_assets"
            ]:
                privileged += 1

        if privileged >= 2:
            finding.privilege_concentration = (
                "Very High"
            )

        elif privileged == 1:
            finding.privilege_concentration = (
                "High"
            )

        else:
            finding.privilege_concentration = (
                "Low"
            )

        # =====================================================
        # Intelligence Summary
        # =====================================================

        if shared_nodes:

            finding.intelligence_summary = (
                f"This attack path traverses "
                f"{len(shared_nodes)} shared "
                f"privilege node(s): "
                f"{', '.join(shared_nodes)}. "
                f"The path ultimately reaches "
                f"{path[-1]}, making it a "
                f"high-priority privilege "
                f"escalation route."
            )

        else:

            finding.intelligence_summary = (
                f"This attack path reaches "
                f"{path[-1]} without traversing "
                f"shared privilege hubs."
            )

        return finding

    # =========================================================

    def run(self) -> EngineResult:

        # -----------------------------------------------------
        # Connect
        # -----------------------------------------------------

        self.connect()

        # -----------------------------------------------------
        # Collect Relationships
        # -----------------------------------------------------

        relationships = self.collect_relationships()

        # -----------------------------------------------------
        # Build Graph
        # -----------------------------------------------------

        graph = self.build_graph(
            relationships
        )

        # -----------------------------------------------------
        # Attack Paths
        # -----------------------------------------------------

        attack_paths = self.discover_attack_paths(
            graph
        )

        # -----------------------------------------------------
        # Analysis
        # -----------------------------------------------------

        (
            findings,
            graph_intelligence,
            remediation_plan,
        ) = self.analyze_attack_paths(
            graph,
            attack_paths,
        )

        # -----------------------------------------------------
        # Security Summary
        # -----------------------------------------------------

        self.update_progress(
            "Assessing Security Posture",
            90,
        )

        summary = generate_security_summary(
            findings
        )

        # -----------------------------------------------------
        # Statistics
        # -----------------------------------------------------

        users = len(
            self.collector.get_users()
        )

        groups = len(
            self.collector.get_groups()
        )

        relationships_count = len(
            relationships
        )

        # -----------------------------------------------------
        # Complete
        # -----------------------------------------------------

        self.update_progress(
            "Analysis Complete",
            100,
        )

        return EngineResult(
            domain="shadowpath.local",

            users=users,
            groups=groups,
            relationships=relationships_count,

            graph=graph,

            attack_paths=attack_paths,

            findings=findings,

            summary=summary,

            graph_intelligence=graph_intelligence,

            remediation_plan=remediation_plan,
        )