from PyQt5.QtWidgets import QWidget, QFileDialog, QMessageBox
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
        self.stylesheet_file(style_path="static/style/basic_info_tab_style.qss")
        QFontDatabase.addApplicationFont(
            ":/fonts/Lora-VariableFont/Lora-VariableFont_wght.ttf"
        )
        #### ====== Signal Buttons  ======####
        self.ui.load_btn.clicked.connect(self.load_file)
        self.ui.start_btn.clicked.connect(self.start_clicked)
        self.ui.clear_btn.clicked.connect(self.remove_output)
        self.ui.save_btn.clicked.connect(self.save_output)

    def stylesheet_file(self, style_path):
        """Read the Stylesheet of the GUI"""
        with open(style_path, "r") as f:
            style = f.read()
            self.setStyleSheet(style)

    def start_clicked(self):
        """Retrieving the input values upon clicking the start button"""
        #### ====== Retrieve Values ======####
        input_text = self.ui.seq_input.toPlainText()
        seq_type = self.ui.comboBox.currentText()
        label = self.ui.lineEdit.text() or " [No Sample Label Added] "

        #### ====== Handling error for the Input ======####
        try:
            if not input_text:
                raise ValueError()
            elif input_text.startswith("http://") or input_text.startswith("https://"):
                webR = WebRetrieve(url=input_text)
                seq = webR.get_sequence()
                self.proceed_bioseq(seq, seq_type, label)
            else:
                self.proceed_bioseq(input_text, seq_type, label)
        except ValueError:
            self.pop_warning(
                "Wrong Input Field. Please fill up with an appropriate sequence. Make sure to select the correct biomolecule type."
            )

    def proceed_bioseq(self, seq, seq_type, label):
        """Implements the methods on class BioSeq"""
        self.bio = BioSeq(seq=seq, seq_type=seq_type, label=label)
        #### ====== Methods  ======####
        if self.bio.seq_type == "DNA" or self.bio.seq_type == "RNA":
            seq_info = self.bio.get_seq_info()
            seq_freq = self.bio.nucleotide_frequency()
            percent_gc = self.bio.gc_content()
            reverse_comp = self.bio.reverse_complement()
            seq_transcript = self.bio.transcription()
            seq_translation = self.bio.translate_seq()
            self.dna_rna_output(
                seq_info,
                seq_freq,
                percent_gc,
                reverse_comp,
                seq_transcript,
                seq_translation,
            )
        elif self.bio.seq_type == "Protein":
            seq_info = self.bio.get_seq_info()
            seq_freq = self.bio.nucleotide_frequency()
            seq_mw = self.bio.amino_mw()
            seq_iep = self.bio.calc_iso_point()
            rf = [frames for frames in self.bio.proteins_from_rf(list(seq))]
            orf_list = "\n".join([f" Region{i+1}: {rf}" for i, rf in enumerate(rf)])
            self.protein_ouptut(seq_info, seq_freq, seq_mw, seq_iep, orf_list)

    def dna_rna_output(
        self,
        seq_info,
        seq_freq,
        percent_gc,
        reverse_comp,
        seq_transcript,
        seq_translation,
    ):
        """Output Format for DNA/RNA Input Sequence"""
        all_output = dedent(
            f"""
                    [1] Sequence Information  \n{seq_info}
                    [2] Nucleotide Frequency  \n{seq_freq}
                    [3] GC Content: {percent_gc} %  
                    [4] Reverse Complement  3'-> 5'   \n{reverse_comp}
                    [5] Transcription (DNA to mRNA)   \n{seq_transcript}
                    [6] Translation (mRNA to Protein) \n{seq_translation}
                =========================================
                """
        )
        self.ui.textBrowser.append(all_output)

    def protein_ouptut(self, seq_info, seq_freq, seq_mw, seq_iep, orf_list):
        """Output Format for Protein Sequence"""
        all_output = dedent(
            f"""
            [1] Sequence Information  \n{seq_info}
            [2] Amino Acid Frequency     \n{seq_freq}
            [3] Amino Acid MW: {seq_mw} Da
            [4] Isoelectric Point: {seq_iep}
            [5] Open Reading Frames:       \n {orf_list}
        """
        )
        self.ui.textBrowser.append(all_output)

    def save_output(self, all_output):
        """Saving the Output Text as .txt file"""
        save_options = QFileDialog.Options()
        file_dialog = QFileDialog(self)
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        file_dialog.setNameFilter("Text Files (*.txt);;All Files (*)")
        file_dialog.setStyleSheet(self.styleSheet())

        file_name, _ = file_dialog.getSaveFileName(
            self,
            "Save Output File",
            "sequence info",
            "Text Files (*.txt);;All Files (*)",
            options=save_options,
        )

        if file_name:
            with open(file_name, "w") as file_out:
                file_out.write(all_output)

    def remove_output(self):
        """Clear Button for the Output Section"""
        self.ui.textBrowser.clear()

    def load_file(self):
        """Load Sequence from a file"""
        options = QFileDialog.Options()
        file_dialog = QFileDialog(self, options=options)
        file_dialog.setNameFilter(
            "Text Files (*.txt);;FASTA Files (*.fasta);;All Files (*)"
        )
        file_dialog.setStyleSheet("static/style/basic_info_tab_style.qss")
        file_name, _ = file_dialog.getOpenFileName(
            self,
            "Load FASTA or .txt File",
            "",
            "Text Files (*.txt);;FASTA Files (*.fasta);;All Files (*)",
            options=options,
        )
        if file_name:
            try:
                with open(file_name, "r") as file_in:
                    content = file_in.read()

                #### ====== Separate the label and sequence  ======####
                label, sequence = self.extract_fasta_content(content)

                #### ====== Connect Label and Sequence to the UI ======####
                self.ui.lineEdit.setText(label)
                self.ui.seq_input.setPlainText(sequence)

            except Exception as e:
                self.pop_warning(f"Error loading file: {str(e)}")

    def extract_fasta_content(self, content):
        """Extract label and sequence from FASTA content"""
        lines = content.split("\n")
        label = ""
        sequence = ""
        for line in lines:
            if line.startswith(">"):
                #### ====== Label is after > character ======####
                label = line[1:].strip()
            else:
                #### ====== Obtain String Sequences  ======####
                sequence += line.strip()
        return label, sequence

    def pop_warning(self, message):
        """Warning Message if the Input is Wrong"""
        pop_warning = QMessageBox()
        pop_warning.setIcon(QMessageBox.Warning)
        pop_warning.setWindowTitle("Input Error")
        pop_warning.setText(message)
        pop_warning.setStyleSheet(
            """
        QMessageBox{
            background-color: rgb(54,54,54); /* charcoal gray*/ 
            }
        QMessageBox QLabel{
            color: #fff;
            }
        QMessageBox QPushButton {
            background-color: rgb(120,157,186); /* light blue */
	        border: 3px solid rgb(5,92,142);
	        border-radius:15px;
	        padding: 5px;
	        color: #000;
            font-size:12px;
            }
        QMessageBox QPushButton::hover{
            background-color: rgba(5,92,142,0.5); /* dark-blue */
	        color: #fff;
	        border-radius: 15px;
            font-size:12px;
            }
        """
        )
        pop_warning.exec_()
