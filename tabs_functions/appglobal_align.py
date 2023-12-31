from PyQt5.QtWidgets import (
    QWidget,
    QMessageBox,
    QFileDialog,
    QLineEdit,
    QPlainTextEdit,
)
from PyQt5.QtGui import QFontDatabase
from textwrap import dedent

from ui.tabs.global_align_ui import Ui_Form
from seq_algorithm.global_needleman import NeedlemanWunschAlgorithm, NWScoringSystem
from seq_algorithm.validate import ValidSequence


class GlobalAlign(QWidget):
    def __init__(self):
        super(GlobalAlign, self).__init__()
        self.ui = Ui_Form()
        self.score = NWScoringSystem()
        self.ui.setupUi(self)
        self.stylesheet_file(style_path="static/style/alignment_tab_style.qss")
        QFontDatabase.addApplicationFont(
            ":/fonts/Lora-VariableFont/Lora-VariableFont_wght.ttf"
        )

        #### ====== Signal Buttons  ======####
        self.ui.load_seq1.clicked.connect(
            lambda: self.load_file(self.ui.label_seq1, self.ui.textEdit)
        )
        self.ui.load_seq2.clicked.connect(
            lambda: self.load_file(self.ui.label_seq2, self.ui.textEdit_2)
        )
        self.ui.clear_btn.clicked.connect(self.remove_output)
        self.ui.align_btn.clicked.connect(self.align_clicked)
        self.ui.save_btn.clicked.connect(self.save_output)

    def stylesheet_file(self, style_path):
        with open(style_path, "r") as f:
            style = f.read()
            self.setStyleSheet(style)

    def align_clicked(self):
        """Retrieving the input values upon clicking the Align button"""
        #### ====== Retrieve Values ======####
        label_1 = self.ui.label_seq1.text() or "No Sample Label Added"
        input_seq1 = self.ui.textEdit.toPlainText()
        label_2 = self.ui.label_seq2.text() or "No Sample Label Added"
        input_seq2 = self.ui.textEdit_2.toPlainText()

        #### ====== Handling error for the Input ======####
        self.valid = ValidSequence(seqA=input_seq1, seqB=input_seq2)
        try:
            if not input_seq1 or not input_seq2:
                raise ValueError()
            elif self.valid.pairseq_valid():
                scoring_system = NWScoringSystem(match=1, mismatch=-1, gap=-2)
                self.algorithm = NeedlemanWunschAlgorithm(
                    scoring_system, seqA=input_seq1, seqB=input_seq2
                )
                self.start_alignment(input_seq1, input_seq2, label_1, label_2)
            else:
                raise ValueError()
        except ValueError:
            self.pop_warning(
                "Wrong Input Field. Please fill up with an appropriate sequence."
            )

    def start_alignment(self, input_seq1, input_seq2, label_1, label_2):
        """Call the methods in the class of the sequence algorithm"""
        #### ====== Call methods for sequence alignment ======####
        global_align = self.algorithm
        aligned_seq_A, aligned_seq_B = global_align.seq_alignment(
            input_seq1, input_seq2
        )
        similarity_g = global_align.calc_similarity()
        self.show_output(
            label_1,
            label_2,
            input_seq1,
            input_seq2,
            aligned_seq_A,
            aligned_seq_B,
            similarity_g,
        )

    def show_output(
        self,
        label_1,
        label_2,
        input_seq1,
        input_seq2,
        aligned_seq_A,
        aligned_seq_B,
        similarity_g,
    ):
        """Output Format for Aligned Sequence"""

        aligned_output = dedent(
            f"""
                [Original Sequence 1]: {label_1} \n{input_seq1}
                [Original Sequence 2]: {label_2} \n{input_seq2}

                [Aligned Sequence 1]: {label_1} \n{aligned_seq_A}
                [Aligned Sequence 2]: {label_2} \n{aligned_seq_B}

                Percentage Similarity of the Two Sequences: {similarity_g} %
                =============================================
        """
        )
        self.ui.textBrowser_2.append(aligned_output)

    def load_file(self, label_widget: QLineEdit, sequence_widget: QPlainTextEdit):
        """Load sequence from a file"""
        options = QFileDialog.Options()
        file_dialog = QFileDialog(self, options=options)
        file_dialog.setNameFilter(
            "Text Files (*.txt);;FASTA Files (*.fasta);;All Files (*)"
        )
        file_dialog.setStyleSheet(self.styleSheet())
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
                label_widget.setText(label)
                sequence_widget.setPlainText(sequence)

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

    def save_output(self):
        """Saving the Output Text as .txt file"""
        save_options = QFileDialog.Options()
        file_dialog = QFileDialog(self)
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        file_dialog.setNameFilter("Text Files (*.txt);;All Files (*)")
        file_dialog.setStyleSheet(self.styleSheet())

        try:
            aligned_output = self.ui.textBrowser_2.toPlainText()
            if aligned_output:
                file_name, _ = file_dialog.getSaveFileName(
                    self,
                    "Save Output File",
                    "global aligned seq",
                    "Text Files (*.txt);;All Files (*)",
                    options=save_options,
                )
                if file_name:
                    with open(file_name, "w") as file_out:
                        file_out.write(aligned_output)
            else:
                raise Exception
        except Exception as e:
            self.pop_warning(f"Error saving file: {str(e)}")

    def remove_output(self):
        """Clear Button for the Output Section"""
        self.ui.textBrowser_2.clear()

    def pop_warning(self, message):
        """Warning Message if the Input is Wrong"""
        pop_warning = QMessageBox()
        pop_warning.setIcon(QMessageBox.Warning)
        pop_warning.setWindowTitle("Input Error")
        pop_warning.setText(message)
        pop_warning.setStyleSheet(self.popup_style())
        pop_warning.exec_()

    def popup_style(self):
        return """
        QMessageBox{
            background-color: rgb(54,54,54); /* charcoal gray*/ 
            }
        QMessageBox QLabel{
            color: #fff;
            }
        QMessageBox QPushButton {
            background-color: rgb(120,157,186); /* light blue */
	        border: 3px solid rgb(5,92,142);
	        border-radius:12px;
	        padding: 5px;
	        color: #000;
            font-size:12px;
            }
        QMessageBox QPushButton::hover{
            background-color: rgba(5,92,142,0.5); /* dark-blue */
	        color: #fff;
	        border-radius: 12px;
            font-size:12px;
            }
        """
