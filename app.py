from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QFrame,
    QSizeGrip,
    QMessageBox,
    QGraphicsDropShadowEffect,
)
from PyQt5.QtCore import Qt, QPoint, QUrl, QTimer
from PyQt5.QtGui import QColor, QFontDatabase, QIcon, QDesktopServices
from ui.main_window import Ui_MainWindow
from ui import resources_rc
from ui.ui_splash_screen import Ui_SplashScreen
from ui.circular_progress import CircularProgress


import sys
import os

from tabs_functions.appbasic_info import BasicInfo
from tabs_functions.appdot_plot import DotPlot
from tabs_functions.applocal_align import LocalAlign
from tabs_functions.appglobal_align import GlobalAlign


# GLOBAL VARIABLE
counter = 0


class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        # REMOVE TITLE BAR
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.progress = CircularProgress()
        self.progress.width = 270
        self.progress.height = 270
        self.progress.value = 10
        self.progress.move(15, 15)
        self.progress.font_size = 35
        self.progress.add_shadow(True)
        self.progress.progress_width = 10
        self.progress.bg_color = QColor(80, 250, 123, 140)
        self.progress.setFixedSize(self.progress.width, self.progress.height)
        self.progress.setParent(self.ui.centralwidget)
        self.progress.show()

        # ADD DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 80))
        self.setGraphicsEffect(self.shadow)

        # Q TIMER
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(30)

        self.show()

    # UPDATE PROGRESS BAR
    def update(self):
        global counter
        # SET VALUE TO PROGRESS BAR
        self.progress.set_value(counter)
        if counter >= 100:
            self.timer.stop()
            self.main = MyWindow()
            self.main.show()
            self.close()
        counter += 1


class MyWindow(QMainWindow):
    def __init__(self):
        ####===== Initialization Constructor ====###
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## ==================================####
        ##  Style and Customizations of Main Window
        ## =================================####
        self.stylesheet_file("static/style/style.qss")
        QFontDatabase.addApplicationFont(
            ":/fonts/Lora-VariableFont/Lora-VariableFont_wght.ttf"
        )
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMaximizeButtonHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        ## ==================================####
        ##  Resizing and Dragging Initial Objects
        ## =================================####
        self.oldPos = None
        QSizeGrip(self.ui.size_grip)
        ## ==================================####
        ##  Customized min, max, and close button
        ## =================================####

        self.max_btn = self.findChild(QPushButton, "max_btn")
        self.max_btn.clicked.connect(lambda: self.toggle_max())

        self.min_btn = self.findChild(QPushButton, "min_btn")
        self.min_btn.clicked.connect(lambda: self.showMinimized())

        self.close_btn = self.findChild(QPushButton, "close_btn")
        self.close_btn.clicked.connect(lambda: self.close())

        ## =================================####
        ##  Obtain the objects or pages(to launch in main_window)
        ## =================================####
        self.basic_info_btn = self.ui.btn_1
        self.dot_plot_btn = self.ui.btn_2
        self.local_align_btn = self.ui.btn_3
        self.global_align_btn = self.ui.btn_4

        ## ==================================####
        ##  Create Dictionary for menu buttons and tab windows
        ## =================================####
        self.menu_btns_dict = {
            self.basic_info_btn: BasicInfo,
            self.dot_plot_btn: DotPlot,
            self.local_align_btn: LocalAlign,
            self.global_align_btn: GlobalAlign,
        }

        ## ==================================####
        ##  Set Up Functions to Show Start Up Tab
        ## =================================####
        self.show_home_window()

        ## ==================================####
        ##  Signal and Slot Configuration
        ## =================================####
        self.ui.tabWidget.tabCloseRequested.connect(self.close_tab)

        self.basic_info_btn.clicked.connect(self.show_selected_window)
        self.dot_plot_btn.clicked.connect(self.show_selected_window)
        self.local_align_btn.clicked.connect(self.show_selected_window)
        self.global_align_btn.clicked.connect(self.show_selected_window)

        ## ==================================####
        ##  Developer's Info Label Signal
        ## =================================####
        self.ui.devlabel.mousePressEvent = self.show_dev_popup

    ## ==================================####
    ##  About Link Functions
    ## =================================####
    def show_dev_popup(self, event):
        """Provides a popup mesage about the developer"""
        msg = QMessageBox()
        msg.setWindowTitle("About the Developer")
        msg.setText("Hello! The developer of this GUI App is Bryan Castillo! ")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDetailedText(
            f"""
            This software was built to demonstrate my skills in bioinformatics and to promote data science in the field of computational biology. """
        )
        msg.setStyleSheet(self.popup_style())
        msg.exec_()

    def open_GitHub_repo(self):
        """Link to the GitHub Repository of this Project"""
        QDesktopServices.openUrl(
            QUrl("https://github.com/bryancastillo10/pairwise_gui")
        )

    def open_paypal_donate(self):
        """Link to the Paypal Donation"""
        QDesktopServices.openUrl(QUrl("https://paypal.me/BryanAngeloCastillo"))

    ## ==================================####
    ##  Tab Functions
    ## =================================####
    def show_home_window(self):
        """Function for showing home window
        :return:
        """
        result = self.open_tab_flag(self.basic_info_btn)
        self.set_btn_checked(self.basic_info_btn)

        if result[0]:
            self.ui.tabWidget.setCurrentIndex(result[1])
        else:
            tab_title = self.basic_info_btn.text()
            curIndex = self.ui.tabWidget.addTab(BasicInfo(), tab_title)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            self.ui.tabWidget.setVisible(True)

    def set_btn_checked(self, btn):
        """
        Status of the selected button were checked and set other buttons' status off/unchecked
        :param btn: button object
        """
        for button in self.menu_btns_dict.keys():
            if button != btn:
                button.setChecked(False)
            else:
                button.setChecked(True)

    def show_selected_window(self):
        """
        Function for showing the currently selected window
        :return:
        """
        button = self.sender()

        result = self.open_tab_flag(button.text())
        self.set_btn_checked(button)

        if result[0]:
            self.ui.tabWidget.setCurrentIndex(result[1])
        else:
            tab_title = button.text()
            curIndex = self.ui.tabWidget.addTab(
                self.menu_btns_dict[button](), tab_title
            )
            self.ui.tabWidget.setCurrentIndex(curIndex)
            self.ui.tabWidget.setVisible(True)

    def close_tab(self, index):
        """
        Function for closing a tab in tabWidget
        :param index: index of tab
        :return:
        """
        self.ui.tabWidget.removeTab(index)

        if self.ui.tabWidget.count() == 0:
            self.ui.tabWidget.setCurrentIndex(0)
            self.show_home_window()

    def open_tab_flag(self, btn_text):
        """
        To check if the selected window appears or not
        :return: boolean and index
        """
        open_tab_count = self.ui.tabWidget.count()

        for i in range(open_tab_count):
            tab_title = self.ui.tabWidget.tabText(i)
            if tab_title == btn_text:
                return True, i
            else:
                continue
        return (False,)

    ## ==================================####
    ##  QSS File Reading /Stylesheet
    ## =================================####
    def stylesheet_file(self, style_path):
        style_path = "static/style/style.qss"
        with open(style_path, "r") as f:
            style = f.read()
            self.setStyleSheet(style)

    def popup_style(self):
        return """
        QMessageBox{
            background-color: rgb(54,54,54); /* charcoal gray*/ 
            }
        QMessageBox QLabel{
            color: #fff;
            }
        QMessageBox QPushButton {
            background-color: rgb(120,157,186); /* light blue */
	        border: 3px solid rgb(5,92,142);
	        border-radius:12px;
	        padding: 5px;
	        color: #000;
            font-size:12px;
            }
        QMessageBox QPushButton::hover{
            background-color: rgba(5,92,142,0.5); /* dark-blue */
	        color: #fff;
	        border-radius: 12px;
            font-size:12px;
            }
        """

    ## ==================================####
    ##  Min, Max and Close Windows Function
    ## =================================####
    def toggle_max(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()

    def closeEvent(self, event):
        """Confirmation if the user wants to close the main window"""
        close_msg = QMessageBox()
        close_msg.setWindowTitle("The APP is about to Close")
        close_msg.setText("Are you sure you want to terminate BioBytes APP?")
        close_msg.setIcon(QMessageBox.Question)
        close_msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        close_msg.setStyleSheet(self.popup_style())
        response = close_msg.exec_()

        if response == QMessageBox.Yes:
            event.accept()
        elif response == QMessageBox.Cancel:
            event.ignore()

    ## ==================================####
    ##  Default Event and Override Conditions
    ## =================================####
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.oldPos = event.globalPos()

            if self.ui.gitlabel.underMouse():
                self.open_GitHub_repo()

            elif self.ui.paypal_label.underMouse():
                self.open_paypal_donate()

    def mouseMoveEvent(self, event):
        if self.oldPos is not None:
            delta = event.globalPos() - self.oldPos
            self.move(self.pos() + delta)
            self.oldPos = event.globalPos()

    def mouseReleaseEvent(self, event):
        self.oldPos = None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("static/icons/app_icon_dna_32.png"))
    window = SplashScreen()
    window.show()

    sys.exit(app.exec())
