# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ip_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(324, 314)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.ip_in = QtWidgets.QLineEdit(Form)
        self.ip_in.setGeometry(QtCore.QRect(90, 10, 141, 21))
        self.ip_in.setObjectName("ip_in")
        self.maska_in = QtWidgets.QLineEdit(Form)
        self.maska_in.setGeometry(QtCore.QRect(90, 40, 141, 21))
        self.maska_in.setObjectName("maska_in")
        self.btn = QtWidgets.QPushButton(Form)
        self.btn.setGeometry(QtCore.QRect(100, 70, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn.setFont(font)
        self.btn.setObjectName("btn")
        self.info_ou = QtWidgets.QTextEdit(Form)
        self.info_ou.setEnabled(True)
        self.info_ou.setGeometry(QtCore.QRect(0, 100, 321, 211))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.info_ou.setFont(font)
        self.info_ou.setObjectName("info_ou")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Калькулятор ip адресов"))
        self.label.setText(_translate("Form", "IP адрес"))
        self.label_2.setText(_translate("Form", "Маска "))
        self.btn.setText(_translate("Form", "Расчитать"))
