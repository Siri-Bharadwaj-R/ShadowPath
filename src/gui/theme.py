"""
ShadowPath Theme

Professional Dark Theme
"""

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication


# ============================================================
# Color Palette
# ============================================================

BACKGROUND = "#181A1F"
SURFACE = "#20232A"
SURFACE_ALT = "#2A2E36"

ACCENT = "#3B82F6"
ACCENT_HOVER = "#60A5FA"

TEXT_PRIMARY = "#F3F4F6"
TEXT_SECONDARY = "#A1A1AA"

SUCCESS = "#22C55E"
WARNING = "#F59E0B"
DANGER = "#EF4444"

BORDER = "#343A46"


# ============================================================
# Global Stylesheet
# ============================================================

STYLE_SHEET = f"""

QMainWindow {{
    background-color: {BACKGROUND};
}}

QWidget {{
    background-color: {BACKGROUND};
    color: {TEXT_PRIMARY};
    font-size: 10pt;
}}

QFrame {{
    background-color: {SURFACE};
    border: 1px solid {BORDER};
    border-radius: 10px;
}}

QLabel {{
    color: {TEXT_PRIMARY};
    background: transparent;
}}

QPushButton {{
    background-color: {SURFACE_ALT};
    color: {TEXT_PRIMARY};
    border: 1px solid {BORDER};
    border-radius: 8px;
    padding: 8px 16px;
}}

QPushButton:hover {{
    background-color: {ACCENT};
}}

QPushButton:pressed {{
    background-color: {ACCENT_HOVER};
}}

QLineEdit {{
    background-color: {SURFACE};
    border: 1px solid {BORDER};
    border-radius: 8px;
    padding: 8px;
}}

QComboBox {{
    background-color: {SURFACE};
    border: 1px solid {BORDER};
    border-radius: 8px;
    padding: 6px;
}}

QComboBox::drop-down {{
    border: none;
}}

QTableWidget {{
    background-color: {SURFACE};
    border: 1px solid {BORDER};
    gridline-color: {BORDER};
}}

QHeaderView::section {{
    background-color: {SURFACE_ALT};
    padding: 8px;
    border: none;
}}

QTreeWidget {{
    background-color: {SURFACE};
    border: 1px solid {BORDER};
}}

QScrollArea {{
    border: none;
}}

QScrollBar:vertical {{
    background: {BACKGROUND};
    width: 10px;
}}

QScrollBar::handle:vertical {{
    background: {SURFACE_ALT};
    border-radius: 5px;
}}

QScrollBar::handle:vertical:hover {{
    background: {ACCENT};
}}

QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical {{
    height: 0px;
}}

QMenu {{
    background-color: {SURFACE};
    border: 1px solid {BORDER};
}}

QMenu::item {{
    padding: 8px 24px;
}}

QMenu::item:selected {{
    background-color: {ACCENT};
}}

QStatusBar {{
    background-color: {SURFACE};
}}

QToolTip {{
    background-color: {SURFACE_ALT};
    color: {TEXT_PRIMARY};
    border: 1px solid {BORDER};
}}

"""


# ============================================================
# Theme Loader
# ============================================================

def apply_theme(app: QApplication) -> None:
    """
    Apply the ShadowPath application theme.
    """

    app.setStyle("Fusion")

    font = QFont("Segoe UI", 10)
    app.setFont(font)

    app.setStyleSheet(STYLE_SHEET)