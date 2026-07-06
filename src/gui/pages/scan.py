"""
ShadowPath Scan Page

Active Directory Scan Interface
"""

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QFrame,
    QGridLayout,
    QTextEdit,
    QProgressBar,
)


class ScanPage(QWidget):
    """
    Active Directory scan page.
    """

    scan_requested = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.build_ui()

        self.start_button.clicked.connect(
            self.scan_requested.emit
        )

    def build_ui(self):

        root = QVBoxLayout(self)
        root.setContentsMargins(24, 24, 24, 24)
        root.setSpacing(20)

        # =====================================================
        # Header
        # =====================================================

        title = QLabel("Active Directory Scan")
        title.setStyleSheet("""
            QLabel{
                font-size:24px;
                font-weight:700;
                border:none;
            }
        """)

        root.addWidget(title)

        # =====================================================
        # Top Section
        # =====================================================

        top_layout = QHBoxLayout()
        top_layout.setSpacing(20)

        environment = QFrame()
        env_layout = QGridLayout(environment)

        env_layout.addWidget(QLabel("Domain"), 0, 0)
        self.domain_label = QLabel("--")
        env_layout.addWidget(self.domain_label, 0, 1)

        env_layout.addWidget(QLabel("Domain Controller"), 1, 0)
        self.dc_label = QLabel("--")
        env_layout.addWidget(self.dc_label, 1, 1)

        env_layout.addWidget(QLabel("LDAP"), 2, 0)
        self.ldap_label = QLabel("Disconnected")
        env_layout.addWidget(self.ldap_label, 2, 1)

        env_layout.addWidget(QLabel("Last Scan"), 3, 0)
        self.last_scan_label = QLabel("Never")
        env_layout.addWidget(self.last_scan_label, 3, 1)

        # =====================================================

        actions = QFrame()
        action_layout = QVBoxLayout(actions)

        self.start_button = QPushButton("Start Scan")
        self.stop_button = QPushButton("Stop Scan")

        self.start_button.setMinimumHeight(46)
        self.stop_button.setMinimumHeight(46)

        self.stop_button.setEnabled(False)

        action_layout.addWidget(self.start_button)
        action_layout.addWidget(self.stop_button)
        action_layout.addStretch()

        top_layout.addWidget(environment, 3)
        top_layout.addWidget(actions, 1)

        root.addLayout(top_layout)

        # =====================================================
        # Progress
        # =====================================================

        progress_frame = QFrame()
        progress_layout = QVBoxLayout(progress_frame)

        progress_title = QLabel("Scan Progress")
        progress_title.setStyleSheet("""
            QLabel{
                font-size:18px;
                font-weight:600;
                border:none;
            }
        """)

        self.progress = QProgressBar()
        self.progress.setValue(0)

        self.progress_label = QLabel("Waiting to start...")

        progress_layout.addWidget(progress_title)
        progress_layout.addWidget(self.progress)
        progress_layout.addWidget(self.progress_label)

        root.addWidget(progress_frame)

        # =====================================================
        # Scan Log
        # =====================================================

        log_frame = QFrame()
        log_layout = QVBoxLayout(log_frame)

        log_title = QLabel("Live Scan Log")
        log_title.setStyleSheet("""
            QLabel{
                font-size:18px;
                font-weight:600;
                border:none;
            }
        """)

        self.log = QTextEdit()
        self.log.setReadOnly(True)
        self.log.setPlaceholderText(
            "Scanner output will appear here..."
        )

        log_layout.addWidget(log_title)
        log_layout.addWidget(self.log)

        root.addWidget(log_frame)

        # =====================================================
        # Summary
        # =====================================================

        summary = QFrame()
        summary_layout = QGridLayout(summary)

        summary_layout.addWidget(QLabel("Users"), 0, 0)
        self.users_label = QLabel("--")
        summary_layout.addWidget(self.users_label, 0, 1)

        summary_layout.addWidget(QLabel("Groups"), 1, 0)
        self.groups_label = QLabel("--")
        summary_layout.addWidget(self.groups_label, 1, 1)

        summary_layout.addWidget(QLabel("Relationships"), 2, 0)
        self.relationships_label = QLabel("--")
        summary_layout.addWidget(self.relationships_label, 2, 1)

        summary_layout.addWidget(QLabel("Attack Paths"), 3, 0)
        self.attack_paths_label = QLabel("--")
        summary_layout.addWidget(self.attack_paths_label, 3, 1)

        summary_layout.addWidget(QLabel("Critical Findings"), 4, 0)
        self.critical_label = QLabel("--")
        summary_layout.addWidget(self.critical_label, 4, 1)

        root.addWidget(summary)

    # =========================================================

    def append_log(self, message: str):
        self.log.append(message)

    # =========================================================

    def clear_log(self):
        self.log.clear()

    # =========================================================

    def set_progress(self, value: int, message: str):
        self.progress.setValue(value)
        self.progress_label.setText(message)

    # =========================================================

    def update_results(self, result):

        self.domain_label.setText(result.domain)
        self.ldap_label.setText("Connected")

        self.users_label.setText(str(result.users))
        self.groups_label.setText(str(result.groups))
        self.relationships_label.setText(str(result.relationships))
        self.attack_paths_label.setText(
            str(len(result.attack_paths))
        )
        self.critical_label.setText(
            str(result.summary["critical"])
        )

        self.set_progress(
            100,
            "Scan completed successfully."
        )

        self.append_log("Connected to Active Directory")
        self.append_log("Relationships collected")
        self.append_log("Attack graph generated")
        self.append_log("Attack paths discovered")
        self.append_log("Security analysis complete")