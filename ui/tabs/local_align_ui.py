# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\User\Downloads\Documents\GUI Project\pairwise_gui\gui\pages\local_align.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(982, 696)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 971, 681))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "LOCAL ALIGNMENT SECTION (USING SMITH-WATERMAN ALGORITHM)"))
