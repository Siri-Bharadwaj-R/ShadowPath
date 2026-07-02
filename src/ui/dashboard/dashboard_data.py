from dataclasses import dataclass


@dataclass
class DashboardData:
    domain: str

    users: int
    groups: int
    relationships: int

    graph_nodes: int
    graph_edges: int

    findings: list

    summary: dict

    report_path: str = "reports/shadowpath_report.pdf"