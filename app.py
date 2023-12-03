from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QFrame,
    QSizeGrip,
)
from PyQt5.QtCore import Qt

from ui.main_window import Ui_MainWindow
from ui import resources_rc

import sys
import os

from tabs_functions.appbasic_info import BasicInfo
from tabs_functions.appdot_plot import DotPlot
from tabs_functions.applocal_align import LocalAlign
from tabs_functions.appglobal_align import GlobalAlign


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.stylesheet_file("static/style/style.qss")
        # self.setWindowFlag(Qt.FramelessWindowHint)
        # self.setWindowTitle("no title")

        ## ==================================####
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

    def stylesheet_file(self, style_path):
        style_path = "static/style/style.qss"
        with open(style_path, "r") as f:
            style = f.read()
            self.setStyleSheet(style)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyWindow()
    window.show()

    sys.exit(app.exec())
