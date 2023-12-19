# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screen.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PyQt5.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PyQt5.QtWidgets import (
    QApplication,
    QFrame,
    QGridLayout,
    QLabel,
    QMainWindow,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName("SplashScreen")
        SplashScreen.resize(300, 300)
        SplashScreen.setMaximumSize(QSize(300, 300))
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.container = QFrame(self.centralwidget)
        self.container.setObjectName("container")
        self.container.setFrameShape(QFrame.NoFrame)
        self.container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.circle_bg = QFrame(self.container)
        self.circle_bg.setObjectName("circle_bg")
        self.circle_bg.setStyleSheet(
            "QFrame {\n"
            "	background-color: rgb(68,71,90);\n"
            "	color: #f8f8f2;\n"
            "	border-radius: 118px;\n"
            ' 	font: 9pt "Segoe UI";\n'
            "}\n"
            ""
        )
        self.circle_bg.setFrameShape(QFrame.NoFrame)
        self.circle_bg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.circle_bg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.texts = QFrame(self.circle_bg)
        self.texts.setObjectName("texts")
        self.texts.setMaximumSize(QSize(16777215, 190))
        self.texts.setStyleSheet("background: none;")
        self.texts.setFrameShape(QFrame.NoFrame)
        self.texts.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.texts)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.loading = QLabel(self.texts)
        self.loading.setObjectName("loading")
        self.loading.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.loading, 3, 0, 1, 1)

        self.title = QLabel(self.texts)
        self.title.setObjectName("title")
        self.title.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamilies(["Comic Sans MS"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.title.setFont(font)
        self.title.setStyleSheet('font: 12pt "Comic Sans MS";')
        self.title.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.title, 0, 0, 1, 1)

        self.frame = QFrame(self.texts)
        self.frame.setObjectName("frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.version = QLabel(self.frame)
        self.version.setObjectName("version")
        self.version.setMinimumSize(QSize(100, 26))
        self.version.setMaximumSize(QSize(100, 26))
        self.version.setStyleSheet(
            "QLabel{\n"
            "	border-radius: 12px;\n"
            "	color: rgb(151,159,200);\n"
            "	background-color: rgb(54,54,54);\n"
            "	padding: 7px;\n"
            "}"
        )
        self.version.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.version, 0, Qt.AlignHCenter)

        self.gridLayout.addWidget(self.frame, 2, 0, 1, 1)

        self.empty = QFrame(self.texts)
        self.empty.setObjectName("empty")
        self.empty.setMinimumSize(QSize(0, 80))
        self.empty.setFrameShape(QFrame.NoFrame)
        self.empty.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.empty, 1, 0, 1, 1)

        self.verticalLayout_4.addLayout(self.gridLayout)

        self.verticalLayout_3.addWidget(self.texts)

        self.verticalLayout_2.addWidget(self.circle_bg)

        self.verticalLayout.addWidget(self.container)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)

    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(
            QCoreApplication.translate("SplashScreen", "Loading...", None)
        )
        self.loading.setText(
            QCoreApplication.translate("SplashScreen", "loading...", None)
        )
        self.title.setText(
            QCoreApplication.translate("SplashScreen", "BioBytes PairSync", None)
        )
        self.version.setText(
            QCoreApplication.translate("SplashScreen", "v1.0.1 Beta", None)
        )
