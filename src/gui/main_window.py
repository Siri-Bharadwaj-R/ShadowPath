"""
ShadowPath Main Window
"""

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QStackedWidget,
)

from .widgets.sidebar import Sidebar
from .widgets.topbar import TopBar
from .widgets.statusbar import StatusBar

from .pages.dashboard import DashboardPage
from .pages.scan import ScanPage
from .pages.attack_paths import AttackPathsPage
from .pages.mitre import MitrePage
from .pages.reports import ReportsPage
from .pages.settings import SettingsPage


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("ShadowPath")
        self.resize(1600, 900)
        self.setMinimumSize(1280, 720)

        self.build_ui()

    # =====================================================

    def build_ui(self):

        central = QWidget()
        self.setCentralWidget(central)

        root = QHBoxLayout(central)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # Sidebar
        self.sidebar = Sidebar()
        root.addWidget(self.sidebar)

        # Right Side
        right = QWidget()
        right_layout = QVBoxLayout(right)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(0)

        root.addWidget(right)

        # Top Bar
        self.topbar = TopBar()
        right_layout.addWidget(self.topbar)

        # Pages
        self.stack = QStackedWidget()

        self.dashboard = DashboardPage()
        self.scan = ScanPage()
        self.attack_paths = AttackPathsPage()
        self.mitre = MitrePage()
        self.reports = ReportsPage()
        self.settings = SettingsPage()

        self.stack.addWidget(self.dashboard)
        self.stack.addWidget(self.scan)
        self.stack.addWidget(self.attack_paths)
        self.stack.addWidget(self.mitre)
        self.stack.addWidget(self.reports)
        self.stack.addWidget(self.settings)

        right_layout.addWidget(self.stack)

        # Status Bar
        self.status = StatusBar()
        self.setStatusBar(self.status)

        # Connections
        self.sidebar.page_requested.connect(
            self.change_page
        )

    # =====================================================

    def change_page(self, page: str):

        pages = {
            "Dashboard": (
                0,
                "Dashboard",
            ),
            "Scan": (
                1,
                "Scan",
            ),
            "Attack Paths": (
                2,
                "Attack Paths",
            ),
            "MITRE": (
                3,
                "MITRE ATT&CK",
            ),
            "Reports": (
                4,
                "Reports",
            ),
            "Settings": (
                5,
                "Settings",
            ),
        }

        index, title = pages[page]

        self.stack.setCurrentIndex(index)

        self.topbar.set_page_title(title)