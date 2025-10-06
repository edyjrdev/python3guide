#!/usr/bin/env python

from PySide6 import QtWidgets, QtGui, QtCore
import sys


class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None): 
        super().__init__(parent)
        self.image = QtGui.QImage("coffee.png")
        self.target = QtCore.QRect(10, 10, 810, 610)
        self.source = QtCore.QRect(0, 0, self.image.width(), self.image.height())

        self.pen = QtGui.QPen(QtGui.QColor(0,0,0)) 
        self.pen.setWidth(3)

        gradient = QtGui.QLinearGradient(10, 10, 810, 610)
        gradient.setColorAt(0.0, QtGui.QColor(0,0,0,255))
        gradient.setColorAt(1.0, QtGui.QColor(255,255,255,0))
        self.brush = QtGui.QBrush(gradient)
        
    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawImage(self.target, self.image, self.source)
        
        painter.setPen(self.pen) 
        painter.setBrush(self.brush) 
        painter.drawRect(10, 10, 810, 610)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = MyWidget()
    widget.resize(830, 630)
    widget.show()
    sys.exit(app.exec())
 
