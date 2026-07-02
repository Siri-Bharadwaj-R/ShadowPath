from ui.banner import show_banner
from ui.runner import pipeline

from ui.dashboard.layout import render_dashboard
from ui.dashboard.dashboard_data import DashboardData

from ad.ldap_collector import LDAPCollector
from ad.relationship_builder import RelationshipBuilder

from core.graph_builder import build_graph

from analysis.attack_paths import find_attack_paths
from analysis.path_prioritizer import prioritize_attack_paths
from analysis.risk_engine import calculate_risk
from analysis.attack_simulator import generate_attack_simulation
from analysis.intelligence_engine import generate_graph_intelligence
from analysis.findings import Finding
from analysis.report_generator import generate_report
from analysis.security_summary import generate_security_summary

from visualization.graph_visualizer import visualize_graph


def main():

    show_banner()

    collector = LDAPCollector(
        server_ip="192.168.56.10",
        username="SHADOWPATH\\Administrator",
        password="Password123!",
        base_dn="DC=shadowpath,DC=local"
    )

    pipeline.run_stage(
        "Connecting to Active Directory",
        collector.connect
    )

    builder = RelationshipBuilder(collector)

    relationships = pipeline.run_stage(
        "Building Relationships",
        builder.build
    )

    graph = pipeline.run_stage(
        "Building Attack Graph",
        build_graph,
        relationships
    )

    attack_paths = pipeline.run_stage(
        "Discovering Attack Paths",
        find_attack_paths,
        graph
    )

    attack_paths = pipeline.run_stage(
        "Prioritizing Attack Paths",
        prioritize_attack_paths,
        attack_paths
    )

    graph_intelligence = pipeline.run_stage(
        "Generating Attack Intelligence",
        generate_graph_intelligence,
        graph,
        attack_paths
    )

    findings = []

    for index, path in enumerate(attack_paths, start=1):

        score, severity = calculate_risk(path)

        finding = Finding(
            id=f"SP-{index:03}",
            path=path,
            score=score,
            severity=severity,
        )

        finding.simulation = generate_attack_simulation(path)

        # ==========================================
        # Attack Intelligence
        # ==========================================

        finding.blast_radius = len(path)

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

        shared_nodes = []

        for node in path:

            frequency = graph_intelligence["node_frequency"].get(node, 0)

            if frequency > 1:
                shared_nodes.append(node)

        finding.choke_points = shared_nodes

        if len(shared_nodes) >= 3:
            finding.lateral_movement = "High"
        elif len(shared_nodes) >= 1:
            finding.lateral_movement = "Moderate"
        else:
            finding.lateral_movement = "Low"

        privileged = 0

        for node in path:

            if node in graph_intelligence["tier0_assets"]:
                privileged += 1

        if privileged >= 2:
            finding.privilege_concentration = "Very High"
        elif privileged == 1:
            finding.privilege_concentration = "High"
        else:
            finding.privilege_concentration = "Low"

        if shared_nodes:
            finding.intelligence_summary = (
                f"This attack path traverses {len(shared_nodes)} "
                f"shared privilege node(s): {', '.join(shared_nodes)}. "
                f"The path ultimately reaches "
                f"{path[-1]}, making it a high-priority "
                f"privilege escalation route."
            )
        else:
            finding.intelligence_summary = (
                f"This attack path reaches {path[-1]} "
                f"without traversing shared privilege hubs."
            )
        findings.append(finding)

    summary = pipeline.run_stage(
        "Assessing Security Posture",
        generate_security_summary,
        findings
    )

    dashboard_data = DashboardData(
        domain="shadowpath.local",
        users=len(collector.get_users()),
        groups=len(collector.get_groups()),
        relationships=len(relationships),
        graph_nodes=graph.number_of_nodes(),
        graph_edges=graph.number_of_edges(),
        findings=findings,
        summary=summary,
    )

    # Store graph intelligence for future dashboard widgets
    dashboard_data.graph_intelligence = graph_intelligence

    render_dashboard(
        dashboard_data
    )

    pipeline.run_stage(
        "Generating Professional Report",
        generate_report,
        findings,
        summary
    )

    pipeline.run_stage(
        "Rendering Attack Graph",
        visualize_graph,
        graph
    )


if __name__ == "__main__":
    main()