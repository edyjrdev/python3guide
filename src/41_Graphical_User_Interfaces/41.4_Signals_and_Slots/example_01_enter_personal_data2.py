#!/usr/bin/env python

import sys
from PySide6 import QtWidgets, QtCore
from maindialog import Ui_Maindialog


class MyDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Maindialog()
        self.ui.setupUi(self)

        # Set up slots
        self.ui.buttonOK.clicked.connect(self.onOK)
        self.ui.buttonCancel.clicked.connect(self.onCancel)

    def onOK(self):
        # Daten auslesen
        print(f"First name: {self.ui.first_name.text()}")
        print(f"Nachname: {self.ui.last_name.text()}")
        print(f"Address: {self.ui.address.toPlainText()}")
        
        date = self.ui.date_of_birth.date().toString("MM/dd/yyyy")
        print(f"Date of Birth: {date}")
        if self.ui.tnc.checkState():
            print("T&Cs accepted")
        if self.ui.newsletter.checkState():
            print("Subscribed to newsletter")
            
        self.close()

    def onCancel(self):
        print("Too bad")
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dialog = MyDialog()
    dialog.show()
    sys.exit(app.exec())

