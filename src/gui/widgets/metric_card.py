"""
ShadowPath Metric Card

Reusable dashboard metric widget.
"""

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
)


class MetricCard(QFrame):
    """
    Dashboard metric card.
    """

    def __init__(
        self,
        title: str,
        value: str = "--",
        subtitle: str = ""
    ):
        super().__init__()

        self.setMinimumHeight(140)
        self.setObjectName("MetricCard")

        layout = QVBoxLayout(self)

        layout.setContentsMargins(20, 18, 20, 18)
        layout.setSpacing(8)

        # ------------------------------------------

        self.title = QLabel(title.upper())

        self.title.setStyleSheet("""
            QLabel{
                color:#9CA3AF;
                font-size:11px;
                font-weight:600;
                letter-spacing:1px;
                border:none;
            }
        """)

        # ------------------------------------------

        self.value = QLabel(value)

        self.value.setAlignment(
            Qt.AlignmentFlag.AlignLeft
        )

        self.value.setStyleSheet("""
            QLabel{
                font-size:34px;
                font-weight:700;
                color:#F9FAFB;
                border:none;
            }
        """)

        # ------------------------------------------

        self.subtitle = QLabel(subtitle)

        self.subtitle.setStyleSheet("""
            QLabel{
                color:#6B7280;
                font-size:11px;
                border:none;
            }
        """)

        layout.addWidget(self.title)
        layout.addStretch()
        layout.addWidget(self.value)
        layout.addWidget(self.subtitle)

    # ===================================================

    def set_value(self, value):

        self.value.setText(str(value))

    # ===================================================

    def set_subtitle(self, text):

        self.subtitle.setText(text)

    # ===================================================

    def set_title(self, title):

        self.title.setText(title.upper())