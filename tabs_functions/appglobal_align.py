from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QFontDatabase

from ui.tabs.global_align_ui import Ui_Form


class GlobalAlign(QWidget):
    def __init__(self):
        super(GlobalAlign, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
