from PyQt5.QtWidgets import (
    QWidget,
    QMessageBox,
    QFileDialog,
    QLineEdit,
    QPlainTextEdit,
)
from PyQt5.QtGui import QFontDatabase

from ui.tabs.local_align_ui import Ui_Form
from seq_algorithm.local_smithwaterman import SmithWatermanAlgorithm, SWScoringSystem


class LocalAlign(QWidget):
    def __init__(self):
        super(LocalAlign, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.stylesheet_file(style_path="static/style/alignment_tab_style.qss")
        QFontDatabase.addApplicationFont(
            ":/fonts/Lora-VariableFont/Lora-VariableFont_wght.ttf"
        )

    #### ====== Signal Buttons  ======####
    # self.ui.load_seq1.clciked.connect()
    # self.ui.load_seq2.clciked.connect()
    # self.ui.clear_btn.clciked.connect()
    # self.ui.align_btn.clciked.connect()
    # self.ui.save_btn.clciked.connect()

    def stylesheet_file(self, style_path):
        with open(style_path, "r") as f:
            style = f.read()
            self.setStyleSheet(style)
