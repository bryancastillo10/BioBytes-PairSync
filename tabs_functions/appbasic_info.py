from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QFontDatabase
from textwrap import dedent

from ui.tabs.basic_info_ui import Ui_Form

from gene_toolkit.seq_info import BioSeq


class BasicInfo(QWidget):
    """First Tab of the GUI App. Gathering Basic Information in a Sequence"""

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
        ## self.ui.load_btn.clicked.connect(self.function)
        self.ui.start_btn.clicked.connect(self.start_clicked)
        self.ui.clear_btn.clicked.connect(self.remove_output)
        ## self.ui.save_btn.clicked.connect(self.function)

    def stylesheet_file(self, style_path):
        """Read the Stylesheet of the GUI"""
        style_path = "static/style/basic_info_tab_style.qss"
        with open(style_path, "r") as f:
            style = f.read()
            self.setStyleSheet(style)

    def start_clicked(self):
        """Processing of the User Input. Returns the Output based on Class BioSeq Methods"""
        #### ====== Retrieve Values ======####
        self.seq = self.ui.seq_input.toPlainText()
        self.seq_type = self.ui.comboBox.currentText()
        self.label = self.ui.lineEdit.text()
        if not self.label:
            self.label = " [No Sample Label Added] "

        #### ====== Output Format and Class BioSeq Instance ======####
        try:
            self.bio = BioSeq(seq=self.seq, seq_type=self.seq_type, label=self.label)
            #### ====== Methods  ======####
            seq_info = self.bio.get_seq_info()
            seq_freq = self.bio.nucleotide_frequency()

            all_output = dedent(
                f"""
                Sequence Information: \n {seq_info}
                Nucleotide Frequency: \n {seq_freq} \n
        =========================================
            """
            )
            self.ui.textBrowser.append(all_output)

        except AssertionError as e:
            self.ui.textBrowser.append(
                f"""Provided data doesn't seem to be a correct {self.seq_type} sequence. Please try again.
        ========================================
                """
            )

    def remove_output(self):
        self.ui.textBrowser.clear()
