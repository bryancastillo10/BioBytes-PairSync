from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QFontDatabase

from ui.tabs.local_align_ui import Ui_Form


class LocalAlign(QWidget):
    def __init__(self):
        super(LocalAlign, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.stylesheet_file("static/style/tab34style.qss")
        QFontDatabase.addApplicationFont(
            ":/fonts/Lora-VariableFont/Lora-VariableFont_wght.ttf"
        )

    def stylesheet_file(self, style_path):
        style_path = "static/style/tab34style.qss"
        with open(style_path, "r") as f:
            style = f.read()
            self.setStyleSheet(style)
