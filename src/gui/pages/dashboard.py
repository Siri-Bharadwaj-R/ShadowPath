"""
ShadowPath Dashboard Page
"""

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
)

from ..widgets.metric_card import MetricCard


class DashboardPage(QWidget):
    """
    Dashboard page.
    """

    def __init__(self):
        super().__init__()

        self.build_ui()

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
        self.security_score.setAlignment(Qt.AlignmentFlag.AlignCenter)

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

        self.graph_placeholder = QLabel(
            "Interactive attack graph will appear here after a scan."
        )

        self.graph_placeholder.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.graph_placeholder.setMinimumHeight(300)

        graph_layout.addWidget(graph_title)
        graph_layout.addWidget(self.graph_placeholder)

        root.addWidget(graph)

        # ======================================================
        # Bottom Panels
        # ======================================================

        bottom = QHBoxLayout()
        bottom.setSpacing(16)

        # ---------------- Top Findings ----------------

        self.findings_frame = QFrame()

        findings_layout = QVBoxLayout(self.findings_frame)

        findings_title = QLabel("Top Findings")

        findings_title.setStyleSheet("""
            QLabel{
                font-size:18px;
                font-weight:600;
                border:none;
            }
        """)

        self.findings_placeholder = QLabel(
            "No findings available."
        )

        self.findings_placeholder.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        findings_layout.addWidget(findings_title)
        findings_layout.addWidget(self.findings_placeholder)

        # ---------------- Recommendations ----------------

        self.recommendations_frame = QFrame()

        recommendations_layout = QVBoxLayout(
            self.recommendations_frame
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

        self.recommendations_placeholder = QLabel(
            "Recommendations will appear after analysis."
        )

        self.recommendations_placeholder.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        recommendations_layout.addWidget(
            recommendations_title
        )

        recommendations_layout.addWidget(
            self.recommendations_placeholder
        )

        bottom.addWidget(self.findings_frame)
        bottom.addWidget(self.recommendations_frame)

        root.addLayout(bottom)

    # ======================================================

    def set_security_score(self, score: int):

        self.security_score.setText(f"{score} / 100")

    # ======================================================

    def clear_dashboard(self):

        self.security_score.setText("-- / 100")

        self.total_users.set_value("--")
        self.total_groups.set_value("--")
        self.attack_paths.set_value("--")
        self.risk_level.set_value("--")

        self.findings_placeholder.setText(
            "No findings available."
        )

        self.recommendations_placeholder.setText(
            "Recommendations will appear after analysis."
        )