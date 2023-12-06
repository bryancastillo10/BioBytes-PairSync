from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QFontDatabase
from textwrap import dedent

from ui.tabs.basic_info_ui import Ui_Form

from gene_toolkit.seq_info import BioSeq


class BasicInfo(QWidget):
    def __init__(self):
        super(BasicInfo, self).__init__()
        self.ui = Ui_Form()
        # ==== Class Calling ===#
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
        #### ====== User Input  ======####
        type_choice = self.ui.comboBox.currentText()
        sample_label = self.ui.lineEdit.text()

        #### ====== User Input Sequence  ======####
        DNA_string = self.ui.seq_input.toPlainText()
        seq_freq = self.bio.nucleotide_frequency()

        if not sample_label:
            sample_label = " No Sample Label Added"

        all_output = dedent(
            f"""
            [1] Biomolecule Type: {type_choice}\n
            [2] Sample Label:{sample_label}\n
            [3] Nucleotide: Frequency: {seq_freq}
            =================================
        """
        )
        self.ui.textBrowser.append(all_output)

    def remove_output(self):
        self.ui.textBrowser.clear()
