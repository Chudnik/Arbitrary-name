import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from random import *


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)  # Загружаем дизайн
        self.flag = False
        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(255, 0, 0))
            x1 = randint(0, 400)
            y1 = randint(0, 400)
            self.x, self.y = x1, y1
            self.drawEll(qp)
            qp.end()

    def drawEll(self, qp):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())