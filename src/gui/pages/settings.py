"""
ShadowPath Settings Page

Application configuration.
"""

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QFrame,
    QLineEdit,
    QPushButton,
    QCheckBox,
    QComboBox,
    QSpinBox,
)


class SettingsPage(QWidget):
    """
    Application settings page.
    """

    def __init__(self):
        super().__init__()

        self.build_ui()

    # =========================================================

    def build_ui(self):

        root = QVBoxLayout(self)

        root.setContentsMargins(24, 24, 24, 24)
        root.setSpacing(20)

        # =====================================================
        # Title
        # =====================================================

        title = QLabel("Settings")

        title.setStyleSheet("""
            QLabel{
                font-size:24px;
                font-weight:700;
                border:none;
            }
        """)

        root.addWidget(title)

        # =====================================================
        # LDAP Configuration
        # =====================================================

        ldap_frame = QFrame()

        ldap_layout = QGridLayout(ldap_frame)

        ldap_title = QLabel("LDAP Configuration")

        ldap_title.setStyleSheet("""
            QLabel{
                font-size:18px;
                font-weight:600;
                border:none;
            }
        """)

        ldap_layout.addWidget(ldap_title, 0, 0, 1, 2)

        ldap_layout.addWidget(QLabel("Server"), 1, 0)
        self.server_edit = QLineEdit()

        ldap_layout.addWidget(self.server_edit, 1, 1)

        ldap_layout.addWidget(QLabel("Port"), 2, 0)
        self.port_edit = QSpinBox()
        self.port_edit.setMaximum(65535)
        self.port_edit.setValue(389)

        ldap_layout.addWidget(self.port_edit, 2, 1)

        ldap_layout.addWidget(QLabel("Username"), 3, 0)
        self.username_edit = QLineEdit()

        ldap_layout.addWidget(self.username_edit, 3, 1)

        ldap_layout.addWidget(QLabel("Password"), 4, 0)
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(
            QLineEdit.EchoMode.Password
        )

        ldap_layout.addWidget(self.password_edit, 4, 1)

        self.test_connection_button = QPushButton(
            "Test Connection"
        )

        ldap_layout.addWidget(
            self.test_connection_button,
            5,
            1
        )

        root.addWidget(ldap_frame)

        # =====================================================
        # Scan Options
        # =====================================================

        scan_frame = QFrame()

        scan_layout = QVBoxLayout(scan_frame)

        scan_title = QLabel("Scan Options")

        scan_title.setStyleSheet("""
            QLabel{
                font-size:18px;
                font-weight:600;
                border:none;
            }
        """)

        scan_layout.addWidget(scan_title)

        self.include_computers = QCheckBox(
            "Include Computer Objects"
        )

        self.include_groups = QCheckBox(
            "Include Security Groups"
        )

        self.include_disabled = QCheckBox(
            "Include Disabled Accounts"
        )

        self.follow_nested = QCheckBox(
            "Resolve Nested Group Membership"
        )

        self.include_computers.setChecked(True)
        self.include_groups.setChecked(True)
        self.follow_nested.setChecked(True)

        scan_layout.addWidget(self.include_computers)
        scan_layout.addWidget(self.include_groups)
        scan_layout.addWidget(self.include_disabled)
        scan_layout.addWidget(self.follow_nested)

        root.addWidget(scan_frame)

        # =====================================================
        # Appearance
        # =====================================================

        appearance = QFrame()

        appearance_layout = QGridLayout(appearance)

        appearance_title = QLabel("Appearance")

        appearance_title.setStyleSheet("""
            QLabel{
                font-size:18px;
                font-weight:600;
                border:none;
            }
        """)

        appearance_layout.addWidget(
            appearance_title,
            0,
            0,
            1,
            2
        )

        appearance_layout.addWidget(
            QLabel("Theme"),
            1,
            0
        )

        self.theme_combo = QComboBox()

        self.theme_combo.addItems([
            "Dark"
        ])

        appearance_layout.addWidget(
            self.theme_combo,
            1,
            1
        )

        root.addWidget(appearance)

        # =====================================================
        # Buttons
        # =====================================================

        buttons = QHBoxLayout()

        buttons.addStretch()

        self.reset_button = QPushButton(
            "Reset"
        )

        self.save_button = QPushButton(
            "Save Settings"
        )

        self.reset_button.setMinimumWidth(140)
        self.save_button.setMinimumWidth(160)

        buttons.addWidget(self.reset_button)
        buttons.addWidget(self.save_button)

        root.addLayout(buttons)

        root.addStretch()

    # =========================================================

    def settings(self):

        return {
            "server": self.server_edit.text(),
            "port": self.port_edit.value(),
            "username": self.username_edit.text(),
            "password": self.password_edit.text(),
            "include_computers": self.include_computers.isChecked(),
            "include_groups": self.include_groups.isChecked(),
            "include_disabled": self.include_disabled.isChecked(),
            "follow_nested": self.follow_nested.isChecked(),
            "theme": self.theme_combo.currentText(),
        }

    # =========================================================

    def load_settings(self, settings: dict):

        self.server_edit.setText(
            settings.get("server", "")
        )

        self.port_edit.setValue(
            settings.get("port", 389)
        )

        self.username_edit.setText(
            settings.get("username", "")
        )

        self.password_edit.setText(
            settings.get("password", "")
        )

        self.include_computers.setChecked(
            settings.get("include_computers", True)
        )

        self.include_groups.setChecked(
            settings.get("include_groups", True)
        )

        self.include_disabled.setChecked(
            settings.get("include_disabled", False)
        )

        self.follow_nested.setChecked(
            settings.get("follow_nested", True)
        )