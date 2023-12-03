from PyQt5.QtWidgets import QWidget

from ui.tabs.dot_plot_ui import Ui_Form


class DotPlot(QWidget):
    def __init__(self):
        super(DotPlot, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
