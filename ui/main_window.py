# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\User\Desktop\pairwise_gui\ui\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1297, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Lora-VariableFont")
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_menu_widget = QtWidgets.QWidget(self.centralwidget)
        self.left_menu_widget.setObjectName("left_menu_widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.left_menu_widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gen_tools = QtWidgets.QFrame(self.left_menu_widget)
        self.gen_tools.setMinimumSize(QtCore.QSize(0, 0))
        self.gen_tools.setMaximumSize(QtCore.QSize(16777215, 80))
        self.gen_tools.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gen_tools.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gen_tools.setObjectName("gen_tools")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.gen_tools)
        self.horizontalLayout_7.setContentsMargins(3, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.gen_tools)
        self.label_9.setMinimumSize(QtCore.QSize(40, 40))
        self.label_9.setMaximumSize(QtCore.QSize(40, 40))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/icons/icons/app_icon_dna_32.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        self.label = QtWidgets.QLabel(self.gen_tools)
        font = QtGui.QFont()
        font.setFamily("Lora-VariableFont")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_7.addWidget(self.label)
        self.gridLayout_2.addWidget(self.gen_tools, 0, 0, 1, 1)
        self.menu_btns = QtWidgets.QFrame(self.left_menu_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_btns.sizePolicy().hasHeightForWidth())
        self.menu_btns.setSizePolicy(sizePolicy)
        self.menu_btns.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_btns.setObjectName("menu_btns")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.menu_btns)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_1 = QtWidgets.QPushButton(self.menu_btns)
        font = QtGui.QFont()
        font.setFamily("Lora-VariableFont")
        self.btn_1.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/icons/icons/dna-helix-32.ico"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.btn_1.setIcon(icon)
        self.btn_1.setObjectName("btn_1")
        self.verticalLayout_3.addWidget(self.btn_1)
        self.btn_2 = QtWidgets.QPushButton(self.menu_btns)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(":/icons/icons/scatter-plot-32.ico"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.btn_2.setIcon(icon1)
        self.btn_2.setObjectName("btn_2")
        self.verticalLayout_3.addWidget(self.btn_2)
        self.btn_3 = QtWidgets.QPushButton(self.menu_btns)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap(":/icons/icons/extensions-32.ico"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.btn_3.setIcon(icon2)
        self.btn_3.setObjectName("btn_3")
        self.verticalLayout_3.addWidget(self.btn_3)
        self.btn_4 = QtWidgets.QPushButton(self.menu_btns)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap(":/icons/icons/internet-32.ico"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.btn_4.setIcon(icon3)
        self.btn_4.setObjectName("btn_4")
        self.verticalLayout_3.addWidget(self.btn_4)
        self.gridLayout_2.addWidget(
            self.menu_btns, 1, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop
        )
        self.about = QtWidgets.QFrame(self.left_menu_widget)
        self.about.setMaximumSize(QtCore.QSize(16777215, 80))
        self.about.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.about.setFrameShadow(QtWidgets.QFrame.Raised)
        self.about.setObjectName("about")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.about)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_10 = QtWidgets.QLabel(self.about)
        self.label_10.setMinimumSize(QtCore.QSize(50, 50))
        self.label_10.setMaximumSize(QtCore.QSize(50, 50))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(":/icons/icons/analysis32.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(
            self.label_10, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter
        )
        self.label_2 = QtWidgets.QLabel(self.about)
        self.label_2.setMinimumSize(QtCore.QSize(0, 30))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2, 0, QtCore.Qt.AlignLeft)
        self.gridLayout_2.addWidget(self.about, 2, 0, 1, 1)
        self.more_info = QtWidgets.QFrame(self.left_menu_widget)
        self.more_info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.more_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.more_info.setObjectName("more_info")
        self.gridLayout = QtWidgets.QGridLayout(self.more_info)
        self.gridLayout.setContentsMargins(5, 0, 10, 4)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.more_info)
        font = QtGui.QFont()
        font.setFamily("Lora-VariableFont")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.more_info)
        font = QtGui.QFont()
        font.setFamily("Lora-VariableFont")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.more_info)
        self.label_11.setMinimumSize(QtCore.QSize(40, 40))
        self.label_11.setMaximumSize(QtCore.QSize(40, 40))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap(":/images/images/web-development.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.more_info)
        self.label_12.setMinimumSize(QtCore.QSize(40, 40))
        self.label_12.setMaximumSize(QtCore.QSize(40, 40))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap(":/images/images/github.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 1, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.more_info)
        self.label_13.setMinimumSize(QtCore.QSize(40, 40))
        self.label_13.setMaximumSize(QtCore.QSize(40, 40))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap(":/images/images/paypal.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.more_info)
        font = QtGui.QFont()
        font.setFamily("Lora-VariableFont")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.more_info, 3, 0, 1, 1)
        self.horizontalLayout.addWidget(self.left_menu_widget)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lora-VariableFont")
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.header_frame = QtWidgets.QFrame(self.frame_2)
        self.header_frame.setStyleSheet("")
        self.header_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_frame.setObjectName("header_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.toggle_menu = QtWidgets.QFrame(self.header_frame)
        self.toggle_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.toggle_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.toggle_menu.setObjectName("toggle_menu")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.toggle_menu)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.menu_btn = QtWidgets.QPushButton(self.toggle_menu)
        self.menu_btn.setMaximumSize(QtCore.QSize(16777215, 50))
        self.menu_btn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(
            QtGui.QPixmap(":/icons/icons/align-center.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        icon4.addPixmap(
            QtGui.QPixmap(":/icons/icons/arrow-right-circle.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.On,
        )
        self.menu_btn.setIcon(icon4)
        self.menu_btn.setIconSize(QtCore.QSize(40, 40))
        self.menu_btn.setCheckable(True)
        self.menu_btn.setObjectName("menu_btn")
        self.horizontalLayout_3.addWidget(self.menu_btn)
        self.label_6 = QtWidgets.QLabel(self.toggle_menu)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.horizontalLayout_2.addWidget(self.toggle_menu, 0, QtCore.Qt.AlignLeft)
        self.title = QtWidgets.QFrame(self.header_frame)
        self.title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title.setObjectName("title")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.title)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.title)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(
            self.label_7, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter
        )
        self.horizontalLayout_2.addWidget(self.title)
        self.min_max_close = QtWidgets.QFrame(self.header_frame)
        self.min_max_close.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.min_max_close.setFrameShadow(QtWidgets.QFrame.Raised)
        self.min_max_close.setObjectName("min_max_close")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.min_max_close)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.min_btn = QtWidgets.QPushButton(self.min_max_close)
        self.min_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.min_btn.setMaximumSize(QtCore.QSize(30, 30))
        self.min_btn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(
            QtGui.QPixmap(":/icons/icons/minus.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.min_btn.setIcon(icon5)
        self.min_btn.setObjectName("min_btn")
        self.horizontalLayout_4.addWidget(self.min_btn)
        self.max_btn = QtWidgets.QPushButton(self.min_max_close)
        self.max_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.max_btn.setMaximumSize(QtCore.QSize(30, 30))
        self.max_btn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(
            QtGui.QPixmap(":/icons/icons/maximize-2.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.max_btn.setIcon(icon6)
        self.max_btn.setObjectName("max_btn")
        self.horizontalLayout_4.addWidget(self.max_btn)
        self.close_btn = QtWidgets.QPushButton(self.min_max_close)
        self.close_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.close_btn.setMaximumSize(QtCore.QSize(30, 30))
        self.close_btn.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(
            QtGui.QPixmap(":/icons/icons/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.close_btn.setIcon(icon7)
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout_4.addWidget(self.close_btn)
        self.horizontalLayout_2.addWidget(
            self.min_max_close, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignTop
        )
        self.gridLayout_3.addWidget(self.header_frame, 0, 0, 1, 1)
        self.tab_frame = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_frame.sizePolicy().hasHeightForWidth())
        self.tab_frame.setSizePolicy(sizePolicy)
        self.tab_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tab_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tab_frame.setObjectName("tab_frame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_frame)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tabWidget = QtWidgets.QTabWidget(self.tab_frame)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.verticalLayout_8.addWidget(self.tabWidget)
        self.gridLayout_3.addWidget(self.tab_frame, 1, 0, 1, 1)
        self.footer_frame = QtWidgets.QFrame(self.frame_2)
        self.footer_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer_frame.setObjectName("footer_frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.footer_frame)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.copyright = QtWidgets.QFrame(self.footer_frame)
        self.copyright.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.copyright.setFrameShadow(QtWidgets.QFrame.Raised)
        self.copyright.setObjectName("copyright")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.copyright)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.copyright)
        font = QtGui.QFont()
        font.setFamily("Lora-VariableFont")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_7.addWidget(self.label_8, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_5.addWidget(self.copyright)
        self.grip_frame = QtWidgets.QFrame(self.footer_frame)
        self.grip_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.grip_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.grip_frame.setObjectName("grip_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.grip_frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.size_grip = QtWidgets.QFrame(self.grip_frame)
        self.size_grip.setMinimumSize(QtCore.QSize(20, 20))
        self.size_grip.setMaximumSize(QtCore.QSize(50, 50))
        self.size_grip.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.size_grip.setObjectName("size_grip")
        self.verticalLayout.addWidget(self.size_grip)
        self.horizontalLayout_5.addWidget(
            self.grip_frame, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom
        )
        self.gridLayout_3.addWidget(
            self.footer_frame, 2, 0, 1, 1, QtCore.Qt.AlignBottom
        )
        self.footer_frame.raise_()
        self.header_frame.raise_()
        self.tab_frame.raise_()
        self.horizontalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(-1)
        self.menu_btn.toggled["bool"].connect(self.left_menu_widget.setHidden)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "GENERAL TOOLS"))
        self.btn_1.setText(_translate("MainWindow", "Basic Information"))
        self.btn_2.setText(_translate("MainWindow", "Dot Plot "))
        self.btn_3.setText(_translate("MainWindow", "Local Alignment"))
        self.btn_4.setText(_translate("MainWindow", "Global Alignment"))
        self.label_2.setText(_translate("MainWindow", "ABOUT "))
        self.label_5.setText(_translate("MainWindow", "Donation"))
        self.label_3.setText(_translate("MainWindow", "Developer's Info"))
        self.label_4.setText(_translate("MainWindow", "GitHub"))
        self.label_6.setText(_translate("MainWindow", "MENU"))
        self.label_7.setText(_translate("MainWindow", "BioBytes PairSync"))
        self.label_8.setText(
            _translate(
                "MainWindow", "Copyright BioBytes PairSync v1.0.1 All Rights Reserved"
            )
        )
