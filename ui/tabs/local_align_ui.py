# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\user\Documents\Data Science\pairwise_gui\ui\tabs\local_align.ui'
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
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.title = QtWidgets.QFrame(Form)
        self.title.setMaximumSize(QtCore.QSize(16777215, 16777210))
        self.title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title.setObjectName("title")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.title)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(self.title)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_6 = QtWidgets.QLabel(self.title)
        self.label_6.setMaximumSize(QtCore.QSize(50, 50))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/images/images/bases1.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 0, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.title)
        self.des = QtWidgets.QFrame(Form)
        self.des.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.des.setFrameShadow(QtWidgets.QFrame.Raised)
        self.des.setObjectName("des")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.des)
        self.verticalLayout.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.des)
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 110))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.verticalLayout_3.addWidget(self.des)
        self.frame_3 = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setContentsMargins(5, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.seq2_frame = QtWidgets.QFrame(self.frame_3)
        self.seq2_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.seq2_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.seq2_frame.setObjectName("seq2_frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.seq2_frame)
        self.verticalLayout_7.setContentsMargins(5, 0, 0, 10)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.seq2_frame)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3)
        self.textEdit_2 = QtWidgets.QTextEdit(self.seq2_frame)
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout_7.addWidget(self.textEdit_2)
        self.gridLayout.addWidget(self.seq2_frame, 1, 0, 1, 1)
        self.seq1_frame = QtWidgets.QFrame(self.frame_3)
        self.seq1_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.seq1_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.seq1_frame.setObjectName("seq1_frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.seq1_frame)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.seq1_frame)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.textEdit = QtWidgets.QTextEdit(self.seq1_frame)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_6.addWidget(self.textEdit)
        self.gridLayout.addWidget(self.seq1_frame, 0, 0, 1, 1)
        self.align_framed = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.align_framed.sizePolicy().hasHeightForWidth())
        self.align_framed.setSizePolicy(sizePolicy)
        self.align_framed.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.align_framed.setFrameShadow(QtWidgets.QFrame.Raised)
        self.align_framed.setObjectName("align_framed")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.align_framed)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_8 = QtWidgets.QFrame(self.align_framed)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        self.frame_8.setFont(font)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setContentsMargins(-1, 5, -1, 5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.frame_8)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_5.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.align_framed)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_11 = QtWidgets.QFrame(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_11)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.frame_11)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout_2.addWidget(self.textBrowser_2, 0, 0, 1, 1)
        self.verticalLayout_8.addWidget(self.frame_11)
        self.frame_10 = QtWidgets.QFrame(self.frame_9)
        self.frame_10.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(self.frame_10)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.frame_10)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.gridLayout_3.addWidget(self.textBrowser_3, 0, 1, 1, 1)
        self.verticalLayout_8.addWidget(
            self.frame_10, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom
        )
        self.verticalLayout_5.addWidget(self.frame_9)
        self.start_save_btns = QtWidgets.QFrame(self.align_framed)
        self.start_save_btns.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.start_save_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.start_save_btns.setObjectName("start_save_btns")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.start_save_btns)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.start_save_btns)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/icons/icons/play-circle.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(
            228, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(self.start_save_btns)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(":/icons/icons/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout_5.addWidget(self.start_save_btns)
        self.gridLayout.addWidget(self.align_framed, 0, 1, 2, 1)
        self.verticalLayout_3.addWidget(self.frame_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Local Alignment"))
        self.textBrowser.setHtml(
            _translate(
                "Form",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'PMingLiU'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:10pt;">The Smith-Waterman algorithm, a dynamic programming approach, is a cornerstone in bioinformatics for local sequence alignment. Developed as an improvement over the global alignment algorithms, Smith-Waterman excels in identifying highly similar regions within biological sequences. Unlike global alignment, this algorithm focuses on finding the optimal local alignment by initiating the alignment from every position in the sequences, allowing for the identification of short, conserved regions even in the presence of substantial sequence variations. The algorithm evaluates all possible local alignments, assigning scores to sequence matches, mismatches, and gaps, and then dynamically constructs an alignment matrix. Through traceback, it identifies the optimal local alignment by selecting the path with the highest cumulative score. Smith-Waterman is instrumental in detecting similarities between sequences with divergent regions, making it invaluable in the discovery of functional domains, conserved motifs, and evolutionary relationships in biological data.</span></p></body></html>',
            )
        )
        self.label_3.setText(_translate("Form", "Sequence 2"))
        self.textEdit_2.setPlaceholderText(_translate("Form", "Enter Second Sequence"))
        self.label_2.setText(_translate("Form", "Sequence 1"))
        self.textEdit.setPlaceholderText(_translate("Form", "Enter First Sequence"))
        self.label_4.setText(_translate("Form", "Aligned Sequences"))
        self.label_5.setText(_translate("Form", "Percent Similarity:"))
        self.pushButton.setText(_translate("Form", "Align"))
        self.pushButton_2.setText(_translate("Form", "Save"))
