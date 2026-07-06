"""
ShadowPath
Enterprise Active Directory Attack Path Analysis Platform

GUI Entry Point
"""

import sys

from PyQt6.QtWidgets import QApplication

from .main_window import MainWindow
from .theme import apply_theme


def main() -> None:
    """
    Launch the ShadowPath desktop application.
    """

    app = QApplication(sys.argv)

    app.setApplicationName("ShadowPath")
    app.setApplicationVersion("1.0.0")
    app.setOrganizationName("ShadowPath")

    apply_theme(app)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()