from PyQt5.QtWidgets import QWidget, QFileDialog
from PyQt5.QtGui import QFontDatabase
from textwrap import dedent

from ui.tabs.basic_info_ui import Ui_Form

from gene_toolkit.seq_info import BioSeq
from gene_toolkit.parser import WebRetrieve


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
        self.ui.save_btn.clicked.connect(self.save_output)

    def stylesheet_file(self, style_path):
        """Read the Stylesheet of the GUI"""
        style_path = "static/style/basic_info_tab_style.qss"
        with open(style_path, "r") as f:
            style = f.read()
            self.setStyleSheet(style)

    def start_clicked(self):
        """Processing of the User Input. Returns the Output based on Class BioSeq Methods"""
        #### ====== Retrieve Values ======####
        input_text = self.ui.seq_input.toPlainText()
        self.seq_type = self.ui.comboBox.currentText()
        self.label = self.ui.lineEdit.text()
        if not self.label:
            self.label = " [No Sample Label Added] "

        #### ====== Output Format and Class BioSeq Instance ======####
        try:
            if input_text.startswith("http://") or input_text.startswith("https://"):
                try:
                    webR = WebRetrieve(url=input_text)
                    self.seq = webR.get_sequence()
                except ValueError as e:
                    self.ui.textBrowser.append(f"Error: {str(e)}")
                    return
            else:
                self.seq = input_text

            self.bio = BioSeq(seq=self.seq, seq_type=self.seq_type, label=self.label)
            #### ====== Methods  ======####
            seq_info = self.bio.get_seq_info()
            seq_freq = self.bio.nucleotide_frequency()
            percent_gc = self.bio.gc_content()
            seq_transcript = self.bio.transcription()
            seq_translation = self.bio.translate_seq()
            all_output = dedent(
                f"""
                [1] Sequence Information  \n{seq_info}
                [2] Nucleotide Frequency  \n{seq_freq}
                [3] GC Content: {percent_gc} %  
                [4] Transcription (DNA to mRNA)   \n{seq_transcript}
                [5] Translation (mRNA to Protein) \n{seq_translation}
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

    def save_output(self):
        """Saving the Output Text as .txt file"""
        save_options = QFileDialog.Options()
        save_options |= QFileDialog.DontUseNativeDialog
        file_dialog = QFileDialog(self, options=save_options)
        file_dialog.setNameFilter("Text Files (*.txt);;All Files (*)")
        file_dialog.setStyleSheet(self.styleSheet())
        file_name, _ = file_dialog.getSaveFileName(
            self,
            "Save File",
            "",
            "Text Files (*.txt);;All Files (*)",
            options=save_options,
        )
        if file_name:
            with open("out.txt", "w") as file_out:
                file_out.write(self.all_output)

    def remove_output(self):
        """Clear Button for the Output Section"""
        self.ui.textBrowser.clear()
