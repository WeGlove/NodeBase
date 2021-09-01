from PyQt5.QtGui import QBrush, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGraphicsRectItem, QGraphicsItem


class Node:

    def __init__(self, scene, position):
        self.rect = QGraphicsRectItem(0, 0, 200, 50)
        self.rect.setPos(position.x(), position.y())
        self.brush = QBrush(Qt.red)
        self.rect.setBrush(self.brush)
        self.rect.setFlag(QGraphicsItem.ItemIsMovable)

        scene.addItem(self.rect)
