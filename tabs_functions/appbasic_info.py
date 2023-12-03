from PyQt5.QtWidgets import QWidget

from ui.tabs.basic_info_ui import Ui_Form


class BasicInfo(QWidget):
    def __init__(self):
        super(BasicInfo, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
