#!/usr/bin/env python

from PySide6 import QtWidgets, QtGui, QtCore
import sys


class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None): 
        super().__init__(parent)
        self.image = QtGui.QImage("coffee.png")
        self.target = QtCore.QRect(10, 10, 810, 610)
        self.source = QtCore.QRect(0, 0, self.image.width(), self.image.height())
        
    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawImage(self.target, self.image, self.source)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = MyWidget()
    widget.resize(830, 630)
    widget.show()
    sys.exit(app.exec())
 
