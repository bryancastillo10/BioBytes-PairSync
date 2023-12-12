from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QFontDatabase

from ui.tabs.dot_plot_ui import Ui_Form

from seq_algorithm.dotplot import DotMatrix


class DotPlot(QWidget):
    def __init__(self):
        super(DotPlot, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.stylesheet_file("static/style/dot_plot_tab_style.qss")
        QFontDatabase.addApplicationFont(
            ":/fonts/Lora-VariableFont/Lora-VariableFont_wght.ttf"
        )
        #### ====== Signal Buttons  ======####
        # self.ui.load_seq1.clicked.connect(self.load_file1)
        # self.ui.load_seq2.clicked.connect(self.load_file2)
        # self.ui.save_btn.clicked.connect(self.function)
        # self.ui.plot_btn.clicked.connect(self.function)

    def stylesheet_file(self, style_path):
        style_path = "static/style/dot_plot_tab_style.qss"
        with open(style_path, "r") as f:
            style = f.read()
            self.setStyleSheet(style)
