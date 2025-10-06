#!/usr/bin/env python

import sys
from PySide6 import QtWidgets
from maindialog import Ui_Maindialog


class MyDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Maindialog()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dialog = MyDialog()
    dialog.show()
    sys.exit(app.exec())

