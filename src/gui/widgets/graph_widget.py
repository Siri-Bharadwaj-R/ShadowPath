"""
ShadowPath Graph Widget
"""

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QBrush, QColor, QPen
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

        self.setRenderHint(
            self.renderHints()
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
                40,
                40,
            )

            circle.setBrush(
                QBrush(QColor("#3B82F6"))
            )

            circle.setPen(
                QPen(Qt.GlobalColor.white)
            )

            self.scene.addItem(circle)

            label = QGraphicsTextItem(node)

            label.setDefaultTextColor(
                Qt.GlobalColor.white
            )

            label.setPos(
                px,
                py + 45,
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
                    QColor("#6B7280"),
                    2,
                )
            )

            self.scene.addItem(line)