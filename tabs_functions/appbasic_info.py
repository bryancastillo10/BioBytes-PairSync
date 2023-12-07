from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QFontDatabase
from textwrap import dedent

from ui.tabs.basic_info_ui import Ui_Form

from gene_toolkit.seq_info import BioSeq


class BasicInfo(QWidget):
    def __init__(self):
        super(BasicInfo, self).__init__()
        self.ui = Ui_Form()
        self.bio = BioSeq()
        self.ui.setupUi(self)
        self.stylesheet_file("static/style/basic_info_tab_style.qss")
        QFontDatabase.addApplicationFont(
            ":/fonts/Lora-VariableFont/Lora-VariableFont_wght.ttf"
        )

        #### ====== Signal Buttons  ======####
        self.ui.start_btn.clicked.connect(self.start_clicked)
        self.ui.clear_btn.clicked.connect(self.remove_output)
        ## self.ui.load_btn.clicked.connect(self.function)

    def stylesheet_file(self, style_path):
        style_path = "static/style/basic_info_tab_style.qss"
        with open(style_path, "r") as f:
            style = f.read()
            self.setStyleSheet(style)

    def start_clicked(self):
        #### ====== Retrieve Values ======####
        seq = self.ui.seq_input.toPlainText()
        seq_type = self.ui.comboBox.currentText()
        label = self.ui.lineEdit.text()
        if not label:
            label = " [No Sample Label Added] "

        try:
            self.bio = BioSeq(seq=seq, seq_type=seq_type, label=label)
            #### ====== Methods  ======####
            seq_freq = self.bio.nucleotide_frequency()

            all_output = dedent(
                f"""
                [1] Biomolecule Type: {seq_type}\n
                [2] Sample Label:{label}\n
                [3] Nucleotide Frequency: {seq_freq}
        =========================================
            """
            )
            self.ui.textBrowser.append(all_output)

        except AssertionError as e:
            self.ui.textBrowser.append(
                f"""Provided data doesn't seem to be a correct {seq_type} sequence. Please try again.
        ========================================
                """
            )

    def remove_output(self):
        self.ui.textBrowser.clear()
