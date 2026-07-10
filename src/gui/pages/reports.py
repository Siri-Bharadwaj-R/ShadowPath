"""
ShadowPath Reports Page

Professional report generation and management interface.
"""

from datetime import datetime

from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QTextEdit,
    QListWidget,
    QListWidgetItem,
    QFrame,
    QFileDialog,
)
import os
import shutil

from PyQt6.QtGui import QDesktopServices
from PyQt6.QtCore import QUrl

from ...analysis.report_generator import generate_report

class ReportsPage(QWidget):
    """
    Report generation and management page.
    """

    def __init__(self):
        super().__init__()

        self.current_report = None
        self.latest_report_path = None
        self.current_result = None

        self.build_ui()

        self.generate_button.clicked.connect(
            self.generate_latest_report
        )

        self.open_button.clicked.connect(
            self.open_latest_report
        )

        self.export_button.clicked.connect(
            self.export_latest_report
        )
    # =========================================================

    def build_ui(self):

        root = QVBoxLayout(self)

        root.setContentsMargins(24, 24, 24, 24)
        root.setSpacing(20)

        # =====================================================
        # Title
        # =====================================================

        title = QLabel("Reports")

        title.setStyleSheet("""
            QLabel{
                font-size:24px;
                font-weight:700;
                border:none;
            }
        """)

        root.addWidget(title)

        # =====================================================
        # Buttons
        # =====================================================

        actions = QHBoxLayout()

        self.generate_button = QPushButton("Generate Report")
        self.open_button = QPushButton("Open Report")
        self.export_button = QPushButton("Export")

        self.generate_button.setMinimumHeight(42)
        self.open_button.setMinimumHeight(42)
        self.export_button.setMinimumHeight(42)

        actions.addWidget(self.generate_button)
        actions.addWidget(self.open_button)
        actions.addWidget(self.export_button)
        actions.addStretch()

        root.addLayout(actions)

        # =====================================================
        # Body
        # =====================================================

        body = QHBoxLayout()
        body.setSpacing(20)

        # =====================================================
        # Report History
        # =====================================================

        history_frame = QFrame()

        history_layout = QVBoxLayout(history_frame)

        history_title = QLabel("Report History")

        history_title.setStyleSheet("""
            QLabel{
                font-size:18px;
                font-weight:600;
                border:none;
            }
        """)

        self.report_list = QListWidget()

        history_layout.addWidget(history_title)
        history_layout.addWidget(self.report_list)

        body.addWidget(history_frame, 1)

        # =====================================================
        # Preview
        # =====================================================

        preview_frame = QFrame()

        preview_layout = QVBoxLayout(preview_frame)

        preview_title = QLabel("Report Preview")

        preview_title.setStyleSheet("""
            QLabel{
                font-size:18px;
                font-weight:600;
                border:none;
            }
        """)

        self.preview = QTextEdit()

        self.preview.setReadOnly(True)

        self.preview.setPlaceholderText(
            "Generate or select a report to preview its summary."
        )

        preview_layout.addWidget(preview_title)
        preview_layout.addWidget(self.preview)

        body.addWidget(preview_frame, 3)

        root.addLayout(body)

    # =========================================================

    def add_report(self, name: str):

        self.report_list.addItem(
            QListWidgetItem(name)
        )

    # =========================================================

    def clear_reports(self):

        self.report_list.clear()

    # =========================================================

    def set_preview(self, text: str):

        self.preview.setPlainText(text)

    # =========================================================

    def select_output_directory(self):

        directory = QFileDialog.getExistingDirectory(
            self,
            "Select Output Directory"
        )

        return directory

    # =========================================================

    def load_result(self, result):

        self.current_result = result

        self.clear_reports()

        report_path = generate_report(
            result.findings,
            result.summary,
        )

        self.latest_report_path = report_path

        report_name = os.path.basename(report_path)

        self.current_report = report_name

        self.add_report(report_name)

        preview = f"""
        ShadowPath Executive Security Report

        Domain
        ------
        {result.domain}

        Overall Security Score
        ----------------------
        {result.summary["overall_score"]}/100

        Users
        -----
        {result.users}

        Groups
        ------
        {result.groups}

        Relationships
        -------------
        {result.relationships}

        Attack Paths
        ------------
        {len(result.attack_paths)}

        Critical Findings
        -----------------
        {result.summary["critical"]}

        High Findings
        -------------
        {result.summary["high"]}

        Medium Findings
        ---------------
        {result.summary["medium"]}

        Low Findings
        ------------
        {result.summary["low"]}

        Report Status
        -------------
        Generated Successfully

        Analysis Time
        -------------
    {datetime.now().strftime("%d %b %Y %H:%M:%S")}
    """

        self.set_preview(preview.strip())

    # =========================================================

    def generate_latest_report(self):

        if self.current_result is None:
            return

        report_path = generate_report(
            self.current_result.findings,
            self.current_result.summary,
        )

        self.latest_report_path = report_path

        self.clear_reports()

        report_name = os.path.basename(report_path)

        self.current_report = report_name

        self.add_report(report_name)

    # =========================================================

    def open_latest_report(self):

        if not self.latest_report_path:
            return

        QDesktopServices.openUrl(
            QUrl.fromLocalFile(
                self.latest_report_path
            )
        )

    # =========================================================

    def export_latest_report(self):

        if not self.latest_report_path:
            return

        destination, _ = QFileDialog.getSaveFileName(
            self,
            "Export Report",
            os.path.basename(
                self.latest_report_path
            ),
            "PDF Files (*.pdf)"
        )

        if destination:
            shutil.copyfile(
                self.latest_report_path,
                destination,
            )

