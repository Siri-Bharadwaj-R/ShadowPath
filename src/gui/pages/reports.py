"""
ShadowPath Reports Page

Professional report generation and management interface.
"""

from PyQt6.QtCore import Qt
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


class ReportsPage(QWidget):
    """
    Report generation and management page.
    """

    def __init__(self):
        super().__init__()

        self.current_report = None

        self.build_ui()

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
        # Action Buttons
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
        # Main Area
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

        self.report_list.addItem(QListWidgetItem(name))

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