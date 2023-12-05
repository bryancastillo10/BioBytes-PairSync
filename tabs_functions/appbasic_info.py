from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QFontDatabase

from ui.tabs.basic_info_ui import Ui_Form


class BasicInfo(QWidget):
    def __init__(self):
        super(BasicInfo, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.stylesheet_file("static/style/tab1style.qss")
        QFontDatabase.addApplicationFont(
            ":/fonts/Lora-VariableFont/Lora-VariableFont_wght.ttf"
        )

    def stylesheet_file(self, style_path):
        style_path = "static/style/tab1style.qss"
        with open(style_path, "r") as f:
            style = f.read()
            self.setStyleSheet(style)
