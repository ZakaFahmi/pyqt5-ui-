# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'click.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from popup import *


class Ui_Dialog(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(351, 314)
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(14)
        Dialog.setFont(font)
        Dialog.setStyleSheet("background: white;")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setMinimumSize(QtCore.QSize(141, 0))
        self.pushButton.setStyleSheet("QPushButton {\n"
"background: qlineargradient(x1:0, y0:0, x2:1, y2:1, stop:0 #4364F7, stop:1 #6FB1FC);\n"
"border: none;\n"
"border-radius: 15px;\n"
"padding: 10px;\n"
"color: white;\n"
"font: 11pt;\n"
"}\n"
"QPushButton:hover {\n"
"background: qlineargradient(x1:0, y0:0, x2:1, y2:0, stop:0 #4364F7, stop:1 #6FB1FC);\n"
"}\n"
"QPushButton:pressed {\n"
"background: qlineargradient(x1:0, y0:0, x2:1, y2:1, stop:0 #b3c1ff, stop:1 #b5e4ff);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Click me!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
