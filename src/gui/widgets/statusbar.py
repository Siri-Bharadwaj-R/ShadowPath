"""
ShadowPath Status Bar
"""

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QStatusBar,
    QLabel,
)


class StatusBar(QStatusBar):
    """
    Bottom application status bar.
    """

    def __init__(self):
        super().__init__()

        self.setFixedHeight(32)

        self.connection_label = QLabel("Disconnected")
        self.connection_label.setAlignment(
            Qt.AlignmentFlag.AlignVCenter
        )

        self.scan_label = QLabel("No Scan Running")
        self.scan_label.setAlignment(
            Qt.AlignmentFlag.AlignVCenter
        )

        self.version_label = QLabel("ShadowPath v1.0.0")
        self.version_label.setAlignment(
            Qt.AlignmentFlag.AlignVCenter
        )

        self.addWidget(self.connection_label)
        self.addPermanentWidget(self.scan_label)
        self.addPermanentWidget(self.version_label)

    def set_connection_status(self, connected: bool):

        if connected:
            self.connection_label.setText("Connected to Active Directory")
        else:
            self.connection_label.setText("Disconnected")

    def set_scan_status(self, text: str):
        self.scan_label.setText(text)

    def set_version(self, version: str):
        self.version_label.setText(version)