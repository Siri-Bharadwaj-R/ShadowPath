"""
ShadowPath Top Bar
"""

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QFrame,
)


class TopBar(QFrame):
    """
    Application top navigation bar.
    """

    def __init__(self):
        super().__init__()

        self.setFixedHeight(64)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(20, 10, 20, 10)
        layout.setSpacing(12)

        self.title = QLabel("Dashboard")
        self.title.setStyleSheet("""
            QLabel{
                font-size:22px;
                font-weight:700;
                border:none;
            }
        """)

        layout.addWidget(self.title)

        layout.addStretch()

        self.scan_button = QPushButton("Scan")
        self.report_button = QPushButton("Generate Report")
        self.help_button = QPushButton("Help")

        for button in (
            self.scan_button,
            self.report_button,
            self.help_button,
        ):
            button.setCursor(Qt.CursorShape.PointingHandCursor)
            button.setMinimumHeight(40)
            button.setMinimumWidth(120)

        layout.addWidget(self.scan_button)
        layout.addWidget(self.report_button)
        layout.addWidget(self.help_button)

    def set_page_title(self, title: str):
        """
        Update page heading.
        """

        self.title.setText(title)