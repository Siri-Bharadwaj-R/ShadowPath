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