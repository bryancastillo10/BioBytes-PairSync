# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\User\Desktop\pairwise_gui\ui\tabs\dot_plot.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(982, 709)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.title = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title.setObjectName("title")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.title)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label = QtWidgets.QLabel(self.title)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_5 = QtWidgets.QLabel(self.title)
        self.label_5.setMaximumSize(QtCore.QSize(40, 40))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/images/images/scatter.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.gridLayout_6.addWidget(self.label_5, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.title)
        self.des = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.des.sizePolicy().hasHeightForWidth())
        self.des.setSizePolicy(sizePolicy)
        self.des.setMaximumSize(QtCore.QSize(16777215, 180))
        self.des.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.des.setFrameShadow(QtWidgets.QFrame.Raised)
        self.des.setLineWidth(0)
        self.des.setObjectName("des")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.des)
        self.horizontalLayout_2.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.des)
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 150))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_2.addWidget(self.textBrowser)
        self.verticalLayout_2.addWidget(self.des)
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
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame = QtWidgets.QFrame(self.frame_3)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(0, 0, 0, 5)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.seq1_frame = QtWidgets.QFrame(self.frame)
        self.seq1_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.seq1_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.seq1_frame.setObjectName("seq1_frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.seq1_frame)
        self.gridLayout_4.setContentsMargins(5, 0, 5, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_2 = QtWidgets.QLabel(self.seq1_frame)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_seq1 = QtWidgets.QLineEdit(self.seq1_frame)
        self.label_seq1.setObjectName("label_seq1")
        self.gridLayout_4.addWidget(self.label_seq1, 0, 1, 1, 1)
        self.load_seq1 = QtWidgets.QPushButton(self.seq1_frame)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/icons/icons/upload.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.load_seq1.setIcon(icon)
        self.load_seq1.setObjectName("load_seq1")
        self.gridLayout_4.addWidget(self.load_seq1, 0, 2, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.seq1_frame)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_4.addWidget(self.textEdit, 1, 0, 1, 3)
        self.gridLayout.addWidget(self.seq1_frame, 0, 0, 1, 1)
        self.seq2_frame = QtWidgets.QFrame(self.frame)
        self.seq2_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.seq2_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.seq2_frame.setObjectName("seq2_frame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.seq2_frame)
        self.gridLayout_5.setContentsMargins(5, 0, 5, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_3 = QtWidgets.QLabel(self.seq2_frame)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_seq2 = QtWidgets.QLineEdit(self.seq2_frame)
        self.label_seq2.setObjectName("label_seq2")
        self.gridLayout_5.addWidget(self.label_seq2, 0, 1, 1, 1)
        self.load_seq2 = QtWidgets.QPushButton(self.seq2_frame)
        self.load_seq2.setIcon(icon)
        self.load_seq2.setObjectName("load_seq2")
        self.gridLayout_5.addWidget(self.load_seq2, 0, 2, 1, 1)
        self.textEdit_2 = QtWidgets.QTextEdit(self.seq2_frame)
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout_5.addWidget(self.textEdit_2, 1, 0, 1, 3)
        self.gridLayout.addWidget(self.seq2_frame, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)
        self.out_graph = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out_graph.sizePolicy().hasHeightForWidth())
        self.out_graph.setSizePolicy(sizePolicy)
        self.out_graph.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.out_graph.setFrameShadow(QtWidgets.QFrame.Raised)
        self.out_graph.setObjectName("out_graph")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.out_graph)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_8 = QtWidgets.QFrame(self.out_graph)
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
        self.verticalLayout.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.out_graph)
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
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.frame_9)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_2.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_9)
        self.output_btns = QtWidgets.QFrame(self.out_graph)
        self.output_btns.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.output_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.output_btns.setObjectName("output_btns")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.output_btns)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.plot_btn = QtWidgets.QPushButton(self.output_btns)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(":/icons/icons/pie-chart.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.plot_btn.setIcon(icon1)
        self.plot_btn.setObjectName("plot_btn")
        self.horizontalLayout.addWidget(self.plot_btn)
        spacerItem = QtWidgets.QSpacerItem(
            228, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem)
        self.save_btn = QtWidgets.QPushButton(self.output_btns)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap(":/icons/icons/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.save_btn.setIcon(icon2)
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout.addWidget(self.save_btn)
        self.verticalLayout.addWidget(self.output_btns)
        self.gridLayout_3.addWidget(self.out_graph, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Dot Plot Sequence Alignment"))
        self.textBrowser.setHtml(
            _translate(
                "Form",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Noto Sans'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                '<p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'PMingLiU\';">   Dot plot sequencing is a valuable tool for pairwise sequence alignment in DNA and protein analysis. This method visually represents sequence similarities by placing dots on a graph, where each dot signifies a matching residue or identical subsequence. This straightforward approach aids in the identification of insertions, deletions, and substitutions, providing insights into evolutionary relationships and conserved regions. </span></p></body></html>',
            )
        )
        self.label_2.setText(_translate("Form", "Sequence 1"))
        self.load_seq1.setText(_translate("Form", "Load"))
        self.textEdit.setPlaceholderText(_translate("Form", "Enter First Sequence"))
        self.label_3.setText(_translate("Form", "Sequence 2"))
        self.load_seq2.setText(_translate("Form", "Load"))
        self.textEdit_2.setPlaceholderText(_translate("Form", "Enter Second Sequence"))
        self.label_4.setText(_translate("Form", "Graphical Output"))
        self.plot_btn.setText(_translate("Form", "Plot"))
        self.save_btn.setText(_translate("Form", "Save"))
