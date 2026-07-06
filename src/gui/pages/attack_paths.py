"""
ShadowPath Attack Paths Page

Displays discovered attack paths with filtering,
searching and detailed path inspection.
"""

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

        self.severity_filter = QComboBox()
        self.severity_filter.addItems([
            "All Severities",
            "Critical",
            "High",
            "Medium",
            "Low"
        ])

        self.export_button = QPushButton("Export")

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

        self.table.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows
        )

        self.table.setSelectionMode(
            QTableWidget.SelectionMode.SingleSelection
        )

        self.table.setAlternatingRowColors(True)

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
        length: int
    ):
        """
        Add one attack path.
        """

        row = self.table.rowCount()

        self.table.insertRow(row)

        self.table.setItem(
            row,
            0,
            QTableWidgetItem(severity)
        )

        self.table.setItem(
            row,
            1,
            QTableWidgetItem(str(risk))
        )

        self.table.setItem(
            row,
            2,
            QTableWidgetItem(source)
        )

        self.table.setItem(
            row,
            3,
            QTableWidgetItem(target)
        )

        self.table.setItem(
            row,
            4,
            QTableWidgetItem(str(length))
        )

    # ==========================================================

    def show_path_details(self, text: str):
        """
        Display detailed information
        for the selected attack path.
        """

        self.details.setPlainText(text)