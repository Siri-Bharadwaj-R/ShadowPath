"""
ShadowPath Main Window
"""
def start_scan(self):

    print("START SCAN CLICKED")

    self.scan.clear_log()

from PyQt6.QtCore import QThread
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

from .workers.scan_worker import ScanWorker


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("ShadowPath")
        self.resize(1600, 900)
        self.setMinimumSize(1280, 720)

        self.worker = None
        self.thread = None

        self.build_ui()

    # =====================================================

    def build_ui(self):

        central = QWidget()
        self.setCentralWidget(central)

        root = QHBoxLayout(central)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # -------------------------------------------------

        self.sidebar = Sidebar()
        root.addWidget(self.sidebar)

        # -------------------------------------------------

        right = QWidget()

        right_layout = QVBoxLayout(right)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(0)

        root.addWidget(right)

        # -------------------------------------------------

        self.topbar = TopBar()
        right_layout.addWidget(self.topbar)

        # -------------------------------------------------

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

        # -------------------------------------------------

        self.status = StatusBar()
        self.setStatusBar(self.status)

        # -------------------------------------------------

        self.sidebar.page_requested.connect(
            self.change_page
        )

        self.scan.scan_requested.connect(
            self.start_scan
        )

    # =====================================================

    def change_page(self, page: str):

        pages = {

            "Dashboard": (0, "Dashboard"),

            "Scan": (1, "Scan"),

            "Attack Paths": (2, "Attack Paths"),

            "MITRE": (3, "MITRE ATT&CK"),

            "Reports": (4, "Reports"),

            "Settings": (5, "Settings"),
        }

        index, title = pages[page]

        self.stack.setCurrentIndex(index)

        self.topbar.set_page_title(title)

    # =====================================================

    def start_scan(self):

        self.scan.clear_log()

        self.scan.set_progress(
            0,
            "Starting scan..."
        )

        self.scan.start_button.setEnabled(False)

        self.thread = QThread()

        self.worker = ScanWorker()

        self.worker.moveToThread(self.thread)

        self.thread.started.connect(
            self.worker.run
        )

        self.worker.progress.connect(
            self.on_progress
        )

        self.worker.finished.connect(
            self.scan_finished
        )

        self.worker.error.connect(
            self.scan_failed
        )

        self.worker.finished.connect(
            self.thread.quit
        )

        self.worker.finished.connect(
            self.worker.deleteLater
        )

        self.thread.finished.connect(
            self.thread.deleteLater
        )

        self.thread.start()

    # =====================================================

    def on_progress(
        self,
        stage,
        percent,
    ):

        self.scan.set_progress(
            percent,
            stage,
        )

        self.scan.append_log(stage)

    # =====================================================

    def scan_finished(self, result):
        self.scan.update_results(result)

        self.dashboard.set_security_score(
            result.summary["overall_score"]
        )

        self.dashboard.total_users.set_value(result.users)
        self.dashboard.total_groups.set_value(result.groups)
        self.dashboard.attack_paths.set_value(len(result.attack_paths))
        self.dashboard.risk_level.set_value(result.summary["overall_score"])

        print("Dashboard OK")

        self.scan.start_button.setEnabled(True)

        print("Everything finished")

        self.status.showMessage(
            "Scan completed successfully."
        )
    # =====================================================

    def scan_failed(self, message):
        print(message)

        self.scan.append_log(message)

        self.scan.start_button.setEnabled(True)

        self.status.showMessage(
            "Scan failed."
        )