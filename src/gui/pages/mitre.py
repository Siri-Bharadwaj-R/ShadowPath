"""
ShadowPath MITRE ATT&CK Page

Displays ATT&CK techniques identified during
attack path analysis.
"""

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QFrame,
    QTableWidget,
    QTableWidgetItem,
    QTextEdit,
    QPushButton,
    QHeaderView,
)


class MitrePage(QWidget):
    """
    MITRE ATT&CK Mapping page.
    """

    def __init__(self):
        super().__init__()

        self.mappings = []

        self.build_ui()

    # =========================================================

    def build_ui(self):

        root = QVBoxLayout(self)

        root.setContentsMargins(24, 24, 24, 24)
        root.setSpacing(20)

        # =====================================================
        # Title
        # =====================================================

        title = QLabel("MITRE ATT&CK Mapping")

        title.setStyleSheet("""
            QLabel{
                font-size:24px;
                font-weight:700;
                border:none;
            }
        """)

        root.addWidget(title)

        # =====================================================
        # Statistics
        # =====================================================

        stats = QHBoxLayout()
        stats.setSpacing(16)

        stats.addWidget(self.metric_card("Techniques", "--"))
        stats.addWidget(self.metric_card("Tactics", "--"))
        stats.addWidget(self.metric_card("Critical", "--"))
        stats.addWidget(self.metric_card("Coverage", "--"))

        root.addLayout(stats)

        # =====================================================
        # Main Area
        # =====================================================

        body = QHBoxLayout()
        body.setSpacing(20)

        # =====================================================
        # Technique Table
        # =====================================================

        table_frame = QFrame()

        table_layout = QVBoxLayout(table_frame)

        table_title = QLabel("Mapped Techniques")

        table_title.setStyleSheet("""
            QLabel{
                font-size:18px;
                font-weight:600;
                border:none;
            }
        """)

        self.table = QTableWidget()

        self.table.setColumnCount(4)

        self.table.setHorizontalHeaderLabels([
            "Technique",
            "ID",
            "Tactic",
            "Severity"
        ])

        self.table.verticalHeader().setVisible(False)

        self.table.setAlternatingRowColors(True)

        self.table.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows
        )

        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        self.table.setSortingEnabled(True)

        table_layout.addWidget(table_title)
        table_layout.addWidget(self.table)

        body.addWidget(table_frame, 3)

        # =====================================================
        # Details Panel
        # =====================================================

        detail_frame = QFrame()

        detail_layout = QVBoxLayout(detail_frame)

        detail_title = QLabel("Technique Details")

        detail_title.setStyleSheet("""
            QLabel{
                font-size:18px;
                font-weight:600;
                border:none;
            }
        """)

        self.details = QTextEdit()

        self.details.setReadOnly(True)

        self.details.setPlaceholderText(
            "Select a MITRE ATT&CK technique to view details."
        )

        self.reference_button = QPushButton(
            "Open MITRE Reference"
        )

        detail_layout.addWidget(detail_title)
        detail_layout.addWidget(self.details)
        detail_layout.addWidget(self.reference_button)

        body.addWidget(detail_frame, 2)

        root.addLayout(body)

        # =====================================================
        # Signals
        # =====================================================

        self.table.itemSelectionChanged.connect(
            self.update_details
        )

    # =========================================================

    def metric_card(self, title: str, value: str):

        frame = QFrame()

        layout = QVBoxLayout(frame)

        layout.setContentsMargins(16, 16, 16, 16)

        heading = QLabel(title)

        heading.setStyleSheet("""
            QLabel{
                color:#A1A1AA;
                font-size:13px;
                border:none;
            }
        """)

        number = QLabel(value)

        number.setStyleSheet("""
            QLabel{
                font-size:28px;
                font-weight:700;
                border:none;
            }
        """)

        layout.addWidget(heading)
        layout.addStretch()
        layout.addWidget(number)

        return frame

    # =========================================================

    def clear(self):

        self.table.setRowCount(0)
        self.details.clear()

    # =========================================================

    def add_mapping(
        self,
        technique: str,
        technique_id: str,
        tactic: str,
        severity: str,
    ):

        row = self.table.rowCount()

        self.table.insertRow(row)

        self.table.setItem(
            row,
            0,
            QTableWidgetItem(technique)
        )

        self.table.setItem(
            row,
            1,
            QTableWidgetItem(technique_id)
        )

        self.table.setItem(
            row,
            2,
            QTableWidgetItem(tactic)
        )

        severity_item = QTableWidgetItem(severity)

        if severity == "Critical":
            severity_item.setBackground(Qt.GlobalColor.darkRed)

        elif severity == "High":
            severity_item.setBackground(Qt.GlobalColor.darkYellow)

        elif severity == "Medium":
            severity_item.setBackground(Qt.GlobalColor.darkCyan)

        self.table.setItem(
            row,
            3,
            severity_item
        )

    # =========================================================

    def show_details(self, text: str):

        self.details.setPlainText(text)

    # =========================================================

    def load_result(self, result):

        self.clear()

        self.mappings = []

        for finding in result.findings:

            for technique in finding.mitre:

                self.add_mapping(
                    technique["name"],
                    technique["id"],
                    technique["tactic"],
                    finding.severity,
                )

                self.mappings.append(
                    (technique, finding)
                )

    # =========================================================

    def update_details(self):

        row = self.table.currentRow()

        if row < 0:
            return

        technique, finding = self.mappings[row]

        text = f"""
Technique
---------

{technique["name"]}

Technique ID
------------

{technique["id"]}

Tactic
------

{technique["tactic"]}

Severity
--------

{finding.severity}

Risk Score
----------

{finding.score}

Attack Path
-----------

{" -> ".join(finding.path)}

Attack Simulation
-----------------

{chr(10).join(finding.simulation)}
"""

        self.details.setPlainText(text.strip())