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

    graph_intelligence: dict = field(default_factory=dict)

    remediation_plan: list = field(default_factory=list)

    report_path: str = "reports/shadowpath_report.pdf"