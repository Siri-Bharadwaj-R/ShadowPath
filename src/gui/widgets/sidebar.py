"""
ShadowPath Sidebar
"""

from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QSizePolicy,
)


class Sidebar(QWidget):
    """
    Left navigation sidebar.
    """

    page_requested = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.buttons = {}

        self.setObjectName("Sidebar")
        self.setFixedWidth(240)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(18, 20, 18, 20)
        layout.setSpacing(10)

        title = QLabel("ShadowPath")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("""
            QLabel{
                font-size:20px;
                font-weight:700;
                padding:12px;
            }
        """)

        layout.addWidget(title)

        layout.addSpacing(20)

        self.add_button(layout, "Dashboard")
        self.add_button(layout, "Scan")
        self.add_button(layout, "Attack Paths")
        self.add_button(layout, "MITRE")
        self.add_button(layout, "Reports")
        self.add_button(layout, "Settings")

        layout.addStretch()

        version = QLabel("Version 1.0.0")
        version.setAlignment(Qt.AlignmentFlag.AlignCenter)
        version.setStyleSheet("""
            QLabel{
                color:#A1A1AA;
                font-size:10px;
                padding:6px;
            }
        """)

        layout.addWidget(version)

        self.select("Dashboard")

    def add_button(self, layout, name: str):

        button = QPushButton(name)

        button.setCursor(Qt.CursorShape.PointingHandCursor)
        button.setMinimumHeight(46)
        button.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Fixed
        )

        button.clicked.connect(
            lambda _, n=name: self.on_clicked(n)
        )

        self.buttons[name] = button
        layout.addWidget(button)

    def on_clicked(self, name: str):

        self.select(name)
        self.page_requested.emit(name)

    def select(self, selected: str):

        for name, button in self.buttons.items():

            if name == selected:

                button.setStyleSheet("""
                    QPushButton{
                        background:#3B82F6;
                        color:white;
                        border:none;
                        border-radius:8px;
                        font-weight:600;
                        text-align:left;
                        padding-left:18px;
                    }

                    QPushButton:hover{
                        background:#60A5FA;
                    }
                """)

            else:

                button.setStyleSheet("""
                    QPushButton{
                        background:#20232A;
                        color:#F3F4F6;
                        border:1px solid #343A46;
                        border-radius:8px;
                        text-align:left;
                        padding-left:18px;
                    }

                    QPushButton:hover{
                        background:#2A2E36;
                    }
                """)