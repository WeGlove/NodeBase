from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QCursor
from Node import Node


class Editor:

    def __init__(self):
        self.app = QApplication([])

        self.scene = QGraphicsScene(0, 0, 400, 200)

        self.nodes = []

        self.view = QGraphicsView(self.scene)

        def f(event):
            cursor = QCursor()
            self.nodes.append(Node(self.scene, cursor.pos()))
        self.view.mouseDoubleClickEvent = f
        self.view.show()

    def start(self):
        self.app.exec()


editor = Editor()
editor.start()
