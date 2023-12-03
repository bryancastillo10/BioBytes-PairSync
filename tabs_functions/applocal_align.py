from PyQt5.QtWidgets import QWidget

from ui.tabs.local_align_ui import Ui_Form


class LocalAlign(QWidget):
    def __init__(self):
        super(LocalAlign, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
