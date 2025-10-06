#!/usr/bin/env python

from PySide6 import QtWidgets
import sys
import model
import view


if __name__ == "__main__":
    m = model.Model("address_book.txt")
    app = QtWidgets.QApplication(sys.argv)
    liste = view.View(m)
    liste.resize(200, 500)
    liste.show()
    sys.exit(app.exec())
