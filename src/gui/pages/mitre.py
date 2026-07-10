"""
ShadowPath MITRE ATT&CK Page

Displays ATT&CK techniques identified during
attack path analysis.
"""

from PyQt6.QtGui import QDesktopServices
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QAbstractItemView
from PyQt6.QtGui import QColor
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtCore import QUrl
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
        root.setSpacing(14)

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
        stats.setSpacing(10)

        self.techniques_card = self.metric_card(
            "Techniques",
            "--",
        )

        self.tactics_card = self.metric_card(
            "Tactics",
            "--",
        )

        self.critical_card = self.metric_card(
            "Critical",
            "--",
        )

        self.coverage_card = self.metric_card(
            "Coverage",
            "--",
        )

        stats.addWidget(self.techniques_card)
        stats.addWidget(self.tactics_card)
        stats.addWidget(self.critical_card)
        stats.addWidget(self.coverage_card)

        root.addLayout(stats)

        root.addLayout(stats)

        # =====================================================
        # Main Area
        # =====================================================

        body = QHBoxLayout()
        body.setSpacing(14)

        # =====================================================
        # Table
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

        self.table.setAlternatingRowColors(False)

        self.table.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows
        )

        self.table.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )

        self.table.setStyleSheet("""
        QTableWidget{
        background:#1F2937;
        alternate-background-color:#1F2937;
        gridline-color:#374151;
        selection-background-color:#F3F4F6;
        selection-color:#111827;
        }
        QTableWidget::item:selected{
        background:#F3F4F6;
        color:#111827;
        }
        """)

        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        self.table.setSortingEnabled(False)

        table_layout.addWidget(table_title)
        table_layout.addWidget(self.table)

        body.addWidget(table_frame, 3)

        # =====================================================
        # Details
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
        self.reference_button.clicked.connect(
            self.open_reference
        )

        body.addWidget(detail_frame, 2)

        root.addLayout(body)

        self.table.itemSelectionChanged.connect(
            self.update_details
        )

    # =========================================================

    def metric_card(self, title: str, value: str):

        frame = QFrame()

        frame.setFixedHeight(90)

        layout = QHBoxLayout(frame)

        layout.setContentsMargins(18, 14, 18, 14)

        heading = QLabel(title)

        heading.setStyleSheet("""
            QLabel{
                color:#A1A1AA;
                font-size:14px;
                border:none;
            }
        """)

        number = QLabel(value)

        frame.value_label = number

        number.setStyleSheet("""
            QLabel{
                font-size:28px;
                font-weight:700;
                border:none;
                color:white;
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
        self.mappings.clear()

    # =========================================================

    def add_mapping(
        self,
        technique,
        technique_id,
        tactic,
        severity,
    ):

        row = self.table.rowCount()

        self.table.insertRow(row)

        self.table.setItem(
            row,
            0,
            QTableWidgetItem(str(technique))
        )

        self.table.setItem(
            row,
            1,
            QTableWidgetItem(str(technique_id))
        )

        self.table.setItem(
            row,
            2,
            QTableWidgetItem(str(tactic))
        )

        severity_item = QTableWidgetItem(str(severity))

        if severity == "Critical":
            severity_item.setForeground(QColor("white"))
            severity_item.setBackground(QColor("#B91C1C"))

        elif severity == "High":
            severity_item.setForeground(QColor("black"))
            severity_item.setBackground(QColor("#FBBF24"))

        elif severity == "Medium":
            severity_item.setForeground(QColor("white"))
            severity_item.setBackground(QColor("#2563EB"))

        self.table.setItem(
            row,
            3,
            severity_item
        )

    # =========================================================

    def load_result(self, result):

        self.clear()

        if result is None:
            return

        findings = getattr(result, "findings", [])

        for finding in findings:

            mitre = getattr(finding, "mitre", [])

            if not mitre:
                continue

            for technique in mitre:

                if isinstance(technique, dict):

                    name = technique.get("name", "Unknown")

                    technique_id = technique.get("id", "")

                    tactic = technique.get("tactic", "")

                else:

                    name = getattr(technique, "name", "Unknown")

                    technique_id = getattr(technique, "id", "")

                    tactic = getattr(technique, "tactic", "")

                self.add_mapping(
                    name,
                    technique_id,
                    tactic,
                    getattr(finding, "severity", ""),
                )

                self.mappings.append(
                    (technique, finding)
                )

        if self.table.rowCount() > 0:
            self.table.clearSelection()

            self.table.selectRow(0)

            self.update_details()
        techniques = self.table.rowCount()

        tactics = len({
            self.table.item(row, 2).text()
            for row in range(self.table.rowCount())
        })

        critical = sum(
            1
            for row in range(self.table.rowCount())
            if self.table.item(row, 3).text() == "Critical"
        )

        coverage = techniques * 5
        coverage = min(coverage, 100)
        self.techniques_card.value_label.setText(str(techniques))
        self.tactics_card.value_label.setText(str(tactics))
        self.critical_card.value_label.setText(str(critical))
        self.coverage_card.value_label.setText(f"{coverage}%")

    # =========================================================

    def update_details(self):

        row = self.table.currentRow()

        if row < 0:
            self.details.clear()
            return

        if row >= len(self.mappings):
            self.details.clear()
            return

        technique, finding = self.mappings[row]

        if isinstance(technique, dict):

            name = technique.get("name", "Unknown")
            tid = technique.get("id", "")
            tactic = technique.get("tactic", "")

        else:

            name = getattr(technique, "name", "Unknown")
            tid = getattr(technique, "id", "")
            tactic = getattr(technique, "tactic", "")

        path = getattr(finding, "path", [])
        simulation = getattr(finding, "simulation", [])

        text = f"""
Technique
---------

{name}

Technique ID
------------

{tid}

Tactic
------

{tactic}

Severity
--------

{getattr(finding, "severity", "")}

Risk Score
----------

{getattr(finding, "score", "")}

Attack Path
-----------

{" -> ".join(path)}

Attack Simulation
-----------------

{chr(10).join(simulation)}
"""

        self.details.setPlainText(text.strip())

# =========================================================

    def open_reference(self):

        QDesktopServices.openUrl(
            QUrl("https://attack.mitre.org/matrices/enterprise/")
    )