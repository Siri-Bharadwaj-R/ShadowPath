"""
ShadowPath Graph Widget
"""

from PyQt6.QtCore import Qt
from PyQt6.QtGui import (
    QBrush,
    QColor,
    QPen,
    QPainter,
)
from PyQt6.QtWidgets import (
    QGraphicsEllipseItem,
    QGraphicsLineItem,
    QGraphicsScene,
    QGraphicsTextItem,
    QGraphicsView,
)


class GraphWidget(QGraphicsView):

    def __init__(self):
        super().__init__()

        self.scene = QGraphicsScene()

        self.setScene(self.scene)
        self.setBackgroundBrush(
            QColor("#111827")
        )

        self.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )

        self.setDragMode(
            QGraphicsView.DragMode.ScrollHandDrag
        )

        self.setMinimumHeight(400)

    # =====================================================

    def clear_graph(self):

        self.scene.clear()

    # =====================================================

    def load_graph(self, graph):

        self.scene.clear()

        positions = {}

        x = 80
        y = 80

        spacing_x = 170
        spacing_y = 100

        # ---------------- Nodes ----------------

        for index, node in enumerate(graph.nodes):

            px = x + (index % 5) * spacing_x
            py = y + (index // 5) * spacing_y

            positions[node] = (px, py)

            circle = QGraphicsEllipseItem(
                px,
                py,
                45,
                45,
            )

            # -------------------------------------------------
            # Node Color
            # -------------------------------------------------

            node_lower = node.lower()

            if "domain admin" in node_lower or "domainadmins" in node_lower:
                color = QColor("#DC2626")  # Critical Red

            elif "admin" in node_lower:
                color = QColor("#EA580C")  # Orange

            elif "group" in node_lower:
                color = QColor("#7C3AED")  # Purple

            elif "user" in node_lower:
                color = QColor("#2563EB")  # Blue

            else:
                color = QColor("#06B6D4")  # Cyan

            circle.setBrush(
                QBrush(color)
            )

            circle.setPen(
                QPen(
                    QColor("#E5E7EB"),
                    2,
                )
            )

            self.scene.addItem(circle)

            # ---------------- Label ----------------

            display_name = node

            # Shorten long Active Directory group names
            if len(display_name) > 18:
                display_name = display_name[:15] + "..."

            label = QGraphicsTextItem(display_name)

            label.setDefaultTextColor(
                QColor("#D1D5DB")
            )

            font = label.font()
            font.setPointSize(10)
            font.setBold(True)
            label.setFont(font)

            label.setPos(
                px - 5,
                py + 55,
            )

            self.scene.addItem(label)

        # ---------------- Edges ----------------

        for source, target in graph.edges:

            x1, y1 = positions[source]
            x2, y2 = positions[target]

            line = QGraphicsLineItem(
                x1 + 20,
                y1 + 20,
                x2 + 20,
                y2 + 20,
            )

            line.setPen(
                QPen(
                    QColor("#4B5563"),
                    3,
                )
            )

            self.scene.addItem(line)

# =====================================================

    def wheelEvent(self, event):

        if event.angleDelta().y() > 0:

            self.scale(1.15, 1.15)

        else:

            self.scale(0.85, 0.85)