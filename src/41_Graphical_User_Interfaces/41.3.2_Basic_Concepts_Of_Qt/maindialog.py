# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maindialog.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateEdit, QDialog,
    QFormLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Maindialog(object):
    def setupUi(self, Maindialog):
        if not Maindialog.objectName():
            Maindialog.setObjectName(u"Maindialog")
        Maindialog.resize(367, 433)
        self.verticalLayout = QVBoxLayout(Maindialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Maindialog)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.last_name = QLineEdit(self.groupBox)
        self.last_name.setObjectName(u"last_name")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.last_name)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.date_of_birth = QDateEdit(self.groupBox)
        self.date_of_birth.setObjectName(u"date_of_birth")

        self.horizontalLayout_2.addWidget(self.date_of_birth)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.address = QTextEdit(self.groupBox)
        self.address.setObjectName(u"address")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.address)

        self.first_name = QLineEdit(self.groupBox)
        self.first_name.setObjectName(u"first_name")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.first_name.sizePolicy().hasHeightForWidth())
        self.first_name.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.first_name)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Maindialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tnc = QCheckBox(self.groupBox_2)
        self.tnc.setObjectName(u"tnc")

        self.verticalLayout_2.addWidget(self.tnc)

        self.newsletter = QCheckBox(self.groupBox_2)
        self.newsletter.setObjectName(u"newsletter")

        self.verticalLayout_2.addWidget(self.newsletter)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.buttonOK = QPushButton(Maindialog)
        self.buttonOK.setObjectName(u"buttonOK")

        self.horizontalLayout.addWidget(self.buttonOK)

        self.buttonCancel = QPushButton(Maindialog)
        self.buttonCancel.setObjectName(u"buttonCancel")

        self.horizontalLayout.addWidget(self.buttonCancel)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Maindialog)

        self.buttonOK.setDefault(True)


        QMetaObject.connectSlotsByName(Maindialog)
    # setupUi

    def retranslateUi(self, Maindialog):
        Maindialog.setWindowTitle(QCoreApplication.translate("Maindialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("Maindialog", u"Personal Data", None))
        self.label_2.setText(QCoreApplication.translate("Maindialog", u"Last Name", None))
        self.label_3.setText(QCoreApplication.translate("Maindialog", u"Date of Birth", None))
        self.label_4.setText(QCoreApplication.translate("Maindialog", u"Address", None))
        self.label.setText(QCoreApplication.translate("Maindialog", u"First Name", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Maindialog", u"Additional Information", None))
        self.tnc.setText(QCoreApplication.translate("Maindialog", u"T&&Cs read and accepted", None))
        self.newsletter.setText(QCoreApplication.translate("Maindialog", u"Subscribe to newsletter", None))
        self.buttonOK.setText(QCoreApplication.translate("Maindialog", u"OK", None))
        self.buttonCancel.setText(QCoreApplication.translate("Maindialog", u"Cancel", None))
    # retranslateUi

