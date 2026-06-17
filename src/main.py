from core.parser import load_relationships
from core.graph_builder import build_graph

from analysis.attack_paths import find_attack_paths
from analysis.risk_engine import calculate_risk
from analysis.findings import Finding
from analysis.security_summary import generate_security_summary
from analysis.mitre_mapper import map_mitre_techniques
from analysis.report_generator import generate_report

from visualization.graph_visualizer import visualize_graph


def main():
    relationships = load_relationships(
        "../data/sample_domain.json"
    )

    print("Loaded Relationships:\n")

    for relationship in relationships:
        print(
            f"{relationship.source} -> {relationship.target}"
        )

    graph = build_graph(relationships)

    print("\nNodes:")
    print(list(graph.nodes()))

    print("\nEdges:")
    print(list(graph.edges()))

    attack_paths = find_attack_paths(graph)

    findings = []

    for path in attack_paths:

        score, severity = calculate_risk(path)

        finding = Finding(
            path=path,
            score=score,
            severity=severity
        )

        findings.append(finding)

    summary = generate_security_summary(findings)

    print("\nSecurity Assessment Summary")
    print("-" * 30)

    print(f"Overall Security Score : {summary['overall_score']}/100")

    print(f"Critical Findings      : {summary['critical']}")
    print(f"High Findings          : {summary['high']}")
    print(f"Medium Findings        : {summary['medium']}")
    print(f"Low Findings           : {summary['low']}")

    print("\nAttack Findings:")

    for finding in findings:

        print("\nPath:")
        print(" -> ".join(finding.path))

        print(f"Risk Score: {finding.score}")
        print(f"Severity : {finding.severity}")
        techniques = map_mitre_techniques(
            finding.path
        )

        print("\nMITRE ATT&CK Techniques:")

        for technique_id, technique_name in techniques:
            print(
                f"{technique_id} - {technique_name}"
            )

    generate_report(
        findings,
        summary
    )
    visualize_graph(graph)


if __name__ == "__main__":
    main()