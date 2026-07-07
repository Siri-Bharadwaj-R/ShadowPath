"""
ShadowPath Dashboard Page
"""

from PyQt6.QtCore import Qt
from ..widgets.graph_widget import GraphWidget
from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QListWidget,
    QListWidgetItem,
)

from ..widgets.metric_card import MetricCard


class DashboardPage(QWidget):
    """
    Dashboard page.
    """

    def __init__(self):
        super().__init__()

        self.build_ui()

    # ======================================================

    def build_ui(self):

        root = QVBoxLayout(self)
        root.setContentsMargins(24, 24, 24, 24)
        root.setSpacing(20)

        # ======================================================
        # Security Score
        # ======================================================

        security_frame = QFrame()

        security_layout = QVBoxLayout(security_frame)
        security_layout.setContentsMargins(20, 20, 20, 20)

        title = QLabel("Security Score")

        title.setStyleSheet("""
            QLabel{
                font-size:20px;
                font-weight:700;
                border:none;
            }
        """)

        self.security_score = QLabel("-- / 100")

        self.security_score.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.security_score.setStyleSheet("""
            QLabel{
                font-size:42px;
                font-weight:700;
                color:#3B82F6;
                border:none;
            }
        """)

        security_layout.addWidget(title)
        security_layout.addSpacing(10)
        security_layout.addWidget(self.security_score)

        root.addWidget(security_frame)

        # ======================================================
        # Metric Cards
        # ======================================================

        metrics = QHBoxLayout()
        metrics.setSpacing(16)

        self.total_users = MetricCard(
            "Users",
            "--",
            "Discovered Accounts"
        )

        self.total_groups = MetricCard(
            "Groups",
            "--",
            "Security Groups"
        )

        self.attack_paths = MetricCard(
            "Attack Paths",
            "--",
            "Privilege Escalation Paths"
        )

        self.risk_level = MetricCard(
            "Risk Score",
            "--",
            "Overall Environment"
        )

        metrics.addWidget(self.total_users)
        metrics.addWidget(self.total_groups)
        metrics.addWidget(self.attack_paths)
        metrics.addWidget(self.risk_level)

        root.addLayout(metrics)

        # ======================================================
        # Attack Graph
        # ======================================================

        graph = QFrame()

        graph_layout = QVBoxLayout(graph)

        graph_title = QLabel("Attack Graph")

        graph_title.setStyleSheet("""
            QLabel{
                font-size:18px;
                font-weight:600;
                border:none;
            }
        """)

        self.graph_widget = GraphWidget()

        self.graph_widget.setMinimumHeight(350)

        graph_layout.addWidget(graph_title)
        graph_layout.addWidget(self.graph_widget)
        root.addWidget(graph)

        # ======================================================
        # Bottom Panels
        # ======================================================

        bottom = QHBoxLayout()
        bottom.setSpacing(16)

        # ======================================================
        # Findings
        # ======================================================

        findings_frame = QFrame()

        findings_layout = QVBoxLayout(findings_frame)

        findings_title = QLabel("Top Findings")

        findings_title.setStyleSheet("""
            QLabel{
                font-size:18px;
                font-weight:600;
                border:none;
            }
        """)

        self.findings_list = QListWidget()

        findings_layout.addWidget(findings_title)
        findings_layout.addWidget(self.findings_list)

        bottom.addWidget(findings_frame)

        # ======================================================
        # Recommendations
        # ======================================================

        recommendations_frame = QFrame()

        recommendations_layout = QVBoxLayout(
            recommendations_frame
        )

        recommendations_title = QLabel(
            "Recommendations"
        )

        recommendations_title.setStyleSheet("""
            QLabel{
                font-size:18px;
                font-weight:600;
                border:none;
            }
        """)

        self.recommendations_list = QListWidget()

        recommendations_layout.addWidget(
            recommendations_title
        )

        recommendations_layout.addWidget(
            self.recommendations_list
        )

        bottom.addWidget(recommendations_frame)

        root.addLayout(bottom)

    # ======================================================

    def set_security_score(
        self,
        score: int,
    ):

        self.security_score.setText(
            f"{score} / 100"
        )

    # ======================================================

    def clear_dashboard(self):

        self.security_score.setText("-- / 100")

        self.total_users.set_value("--")
        self.total_groups.set_value("--")
        self.attack_paths.set_value("--")
        self.risk_level.set_value("--")

        self.findings_list.clear()
        self.recommendations_list.clear()

    # ======================================================

    def load_result(self, result):

        self.graph_widget.load_graph(
            result.graph
        )

        self.set_security_score(
            result.summary["overall_score"]
        )

        self.total_users.set_value(
            result.users
        )

        self.total_groups.set_value(
            result.groups
        )

        self.attack_paths.set_value(
            len(result.attack_paths)
        )

        self.risk_level.set_value(
            result.summary["overall_score"]
        )

        # -----------------------------
        # Findings
        # -----------------------------

        self.findings_list.clear()

        for finding in result.findings[:5]:

            self.findings_list.addItem(
                QListWidgetItem(
                    f"[{finding.severity}] "
                    f"{finding.id} | "
                    f"Risk {finding.score}\n"
                    f"{' -> '.join(finding.path)}"
                )
            )

        # -----------------------------
        # Recommendations
        # -----------------------------

        self.recommendations_list.clear()

        for recommendation in result.remediation_plan[:5]:

            self.recommendations_list.addItem(
                QListWidgetItem(
                    recommendation["recommendation"]
                )
            )
        stats = result.graph_intelligence["graph_statistics"]

        summary = f"""
        Domain
        ------
        {result.domain}

        Overall Security Score
        ----------------------
        {result.summary["overall_score"]}/100

        Attack Paths
        ------------
        {stats["attack_paths"]}

        Critical Findings
        -----------------
        {result.summary["critical"]}

        High Findings
        -------------
        {result.summary["high"]}

        Average Attack Path Length
        --------------------------
        {stats["average_path_length"]}

        Unique Entry Points
        -------------------
        {stats["unique_entry_points"]}

        Unique Targets
        --------------
        {stats["unique_targets"]}

        Graph Nodes
        -----------
        {stats["graph_nodes"]}

        Graph Edges
        -----------
        {stats["graph_edges"]}
        """

        self.graph_summary.setText(summary.strip())