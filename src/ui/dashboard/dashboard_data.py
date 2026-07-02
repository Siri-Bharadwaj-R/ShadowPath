from dataclasses import dataclass, field


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

    # NEW
    graph_intelligence: dict = field(default_factory=dict)

    report_path: str = "reports/shadowpath_report.pdf"