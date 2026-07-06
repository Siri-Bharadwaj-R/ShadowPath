"""
ShadowPath Scan Page

Active Directory Scan Interface
"""

from PyQt6.QtCore import Qt
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

    def __init__(self):
        super().__init__()

        self.build_ui()

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

        # -----------------------------------------

        environment = QFrame()

        env_layout = QGridLayout(environment)

        env_layout.addWidget(QLabel("Domain"), 0, 0)
        env_layout.addWidget(QLabel("--"), 0, 1)

        env_layout.addWidget(QLabel("Domain Controller"), 1, 0)
        env_layout.addWidget(QLabel("--"), 1, 1)

        env_layout.addWidget(QLabel("LDAP"), 2, 0)
        env_layout.addWidget(QLabel("Disconnected"), 2, 1)

        env_layout.addWidget(QLabel("Last Scan"), 3, 0)
        env_layout.addWidget(QLabel("Never"), 3, 1)

        # -----------------------------------------

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

        self.progress_label = QLabel(
            "Waiting to start..."
        )

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
        summary_layout.addWidget(QLabel("--"), 0, 1)

        summary_layout.addWidget(QLabel("Groups"), 1, 0)
        summary_layout.addWidget(QLabel("--"), 1, 1)

        summary_layout.addWidget(QLabel("Relationships"), 2, 0)
        summary_layout.addWidget(QLabel("--"), 2, 1)

        summary_layout.addWidget(QLabel("Attack Paths"), 3, 0)
        summary_layout.addWidget(QLabel("--"), 3, 1)

        summary_layout.addWidget(QLabel("Critical Findings"), 4, 0)
        summary_layout.addWidget(QLabel("--"), 4, 1)

        root.addWidget(summary)

    # =========================================================

    def append_log(self, message: str):
        """
        Append a line to the live scan log.
        """

        self.log.append(message)

    # =========================================================

    def clear_log(self):
        self.log.clear()

    # =========================================================

    def set_progress(self, value: int, message: str):

        self.progress.setValue(value)
        self.progress_label.setText(message)