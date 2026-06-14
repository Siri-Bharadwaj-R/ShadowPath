from core.parser import load_relationships
from core.graph_builder import build_graph

from analysis.attack_paths import find_attack_paths
from analysis.risk_engine import calculate_risk
from analysis.findings import Finding

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

    print("\nAttack Findings:")

    for finding in findings:

        print("\nPath:")
        print(" -> ".join(finding.path))

        print(f"Risk Score: {finding.score}")
        print(f"Severity : {finding.severity}")

    visualize_graph(graph)


if __name__ == "__main__":
    main()