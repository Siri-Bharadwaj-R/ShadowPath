"""
ShadowPath Attack Paths Page

Displays discovered attack paths with filtering,
searching and detailed path inspection.
"""

import csv
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtWidgets import QAbstractItemView
from PyQt6.QtGui import QColor
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QAbstractItemView
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QFrame,
    QLineEdit,
    QComboBox,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QTextEdit,
    QPushButton,
)


class AttackPathsPage(QWidget):
    """
    Attack Paths page.
    """

    def __init__(self):
        super().__init__()

        self.build_ui()
        self.findings = []

    def build_ui(self):

        root = QVBoxLayout(self)
        root.setContentsMargins(24, 24, 24, 24)
        root.setSpacing(20)

        # ======================================================
        # Title
        # ======================================================

        title = QLabel("Attack Paths")
        title.setStyleSheet("""
            QLabel{
                font-size:24px;
                font-weight:700;
                border:none;
            }
        """)

        root.addWidget(title)

        # ======================================================
        # Search / Filter
        # ======================================================

        toolbar = QHBoxLayout()

        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText(
            "Search users, groups, computers..."
        )
        self.search_box.textChanged.connect(
            self.filter_table
        )

        self.severity_filter = QComboBox()
        self.severity_filter.addItems([
            "All Severities",
            "Critical",
            "High",
            "Medium",
            "Low"
        ])
        self.severity_filter.currentTextChanged.connect(
            self.filter_table
        )

        self.export_button = QPushButton("Export")
        self.export_button.clicked.connect(
            self.export_attack_paths
        )

        toolbar.addWidget(self.search_box, 1)
        toolbar.addWidget(self.severity_filter)
        toolbar.addWidget(self.export_button)

        root.addLayout(toolbar)

        # ======================================================
        # Main Layout
        # ======================================================

        body = QHBoxLayout()
        body.setSpacing(20)

        # ======================================================
        # Attack Path Table
        # ======================================================

        table_frame = QFrame()

        table_layout = QVBoxLayout(table_frame)

        self.table = QTableWidget()

        self.table.setColumnCount(5)

        self.table.setHorizontalHeaderLabels([
            "Severity",
            "Risk",
            "Source",
            "Target",
            "Length"
        ])

        self.table.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )

        self.table.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows
        )

        self.table.setSelectionMode(
            QTableWidget.SelectionMode.SingleSelection
        )

        self.table.setAlternatingRowColors(False)
        self.table.setStyleSheet("""
        QTableWidget{
            background:#1F2937;
            alternate-background-color:#1F2937;
            gridline-color:#374151;
        }

        QTableWidget::item:selected{
            background:#2563EB;
            color:white;
        }
        """)

        self.table.verticalHeader().setVisible(False)

        header = self.table.horizontalHeader()

        header.setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        self.table.setSortingEnabled(True)

        table_layout.addWidget(self.table)

        body.addWidget(table_frame, 3)

        # ======================================================
        # Details Panel
        # ======================================================

        details_frame = QFrame()

        details_layout = QVBoxLayout(details_frame)

        details_title = QLabel("Path Details")

        details_title.setStyleSheet("""
            QLabel{
                font-size:18px;
                font-weight:600;
                border:none;
            }
        """)

        self.details = QTextEdit()

        self.details.setReadOnly(True)

        self.details.setPlaceholderText(
            "Select an attack path to inspect."
        )

        details_layout.addWidget(details_title)
        details_layout.addWidget(self.details)

        body.addWidget(details_frame, 2)

        root.addLayout(body)

        self.table.itemSelectionChanged.connect(
            self.update_details
    )
    # ==========================================================

    def clear(self):
        """
        Remove all attack paths.
        """

        self.table.setRowCount(0)
        self.details.clear()


    # ==========================================================

    def add_attack_path(
            self,
            severity: str,
            risk: int,
            source: str,
            target: str,
            length: int,
    ):
        """
        Add one attack path.
        """

        row = self.table.rowCount()

        self.table.insertRow(row)

        # -----------------------------
        # Severity
        # -----------------------------

        severity_item = QTableWidgetItem(severity)

        if severity == "Critical":
            severity_item.setBackground(QColor("#DC2626"))

        elif severity == "High":
            severity_item.setBackground(QColor("#EA580C"))

        elif severity == "Medium":
            severity_item.setBackground(QColor("#2563EB"))

        elif severity == "Low":
            severity_item.setBackground(QColor("#10B981"))

        self.table.setItem(
            row,
            0,
            severity_item,
        )

        # -----------------------------
        # Risk
        # -----------------------------

        self.table.setItem(
            row,
            1,
            QTableWidgetItem(str(risk))
        )

        # -----------------------------
        # Source
        # -----------------------------

        self.table.setItem(
            row,
            2,
            QTableWidgetItem(source)
        )

        # -----------------------------
        # Target
        # -----------------------------

        self.table.setItem(
            row,
            3,
            QTableWidgetItem(target)
        )

        # -----------------------------
        # Length
        # -----------------------------

        self.table.setItem(
            row,
            4,
            QTableWidgetItem(str(length))
        )
    # ==========================================================

    def load_result(self, result):
        self.findings = result.findings

        self.clear()

        for finding in result.findings:
            self.add_attack_path(
                severity=finding.severity,
                risk=finding.score,
                source=finding.path[0],
                target=finding.path[-1],
                length=len(finding.path),
            )

    # ==========================================================

    def update_details(self):

        row = self.table.currentRow()

        if row < 0:
            return

        finding = self.findings[row]

        text = f"""
    Finding ID : {finding.id}

    Severity   : {finding.severity}

    Risk Score : {finding.score}

    Attack Path
    -----------

    {" -> ".join(finding.path)}

    Attack Complexity
    -----------------

    {finding.attack_complexity}

    Lateral Movement
    ----------------

    {finding.lateral_movement}

    Privilege Concentration
    -----------------------

    {finding.privilege_concentration}

    Blast Radius
    ------------

    {finding.blast_radius}

    Intelligence
    ------------

    {finding.intelligence_summary}
    """

        self.details.setPlainText(text.strip())

# ==========================================================

    def filter_table(self):

        text = self.search_box.text().lower()

        severity = self.severity_filter.currentText()

        for row in range(self.table.rowCount()):

            visible = True

            if text:

                found = False

                for column in range(self.table.columnCount()):

                    item = self.table.item(row, column)

                    if item and text in item.text().lower():
                        found = True
                        break

                visible = found

            if severity != "All Severities":

                severity_item = self.table.item(row, 0)

                if severity_item and severity_item.text() != severity:
                    visible = False

            self.table.setRowHidden(row, not visible)

# ==========================================================

    def export_attack_paths(self):

        filename, _ = QFileDialog.getSaveFileName(
            self,
            "Export Attack Paths",
            "attack_paths.csv",
            "CSV Files (*.csv)"
        )

        if not filename:
            return

        with open(filename, "w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Severity",
                "Risk",
                "Source",
                "Target",
                "Length"
            ])

            for row in range(self.table.rowCount()):

                if self.table.isRowHidden(row):
                    continue

                writer.writerow([
                    self.table.item(row, 0).text(),
                    self.table.item(row, 1).text(),
                    self.table.item(row, 2).text(),
                    self.table.item(row, 3).text(),
                    self.table.item(row, 4).text(),
                ])