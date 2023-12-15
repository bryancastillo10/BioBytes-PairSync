from PyQt5.QtWidgets import (
    QWidget,
    QMessageBox,
    QFileDialog,
    QLineEdit,
    QPlainTextEdit,
)
from PyQt5.QtGui import QFontDatabase
from textwrap import dedent

from ui.tabs.local_align_ui import Ui_Form
from seq_algorithm.local_smithwaterman import SmithWatermanAlgorithm, SWScoringSystem


class LocalAlign(QWidget):
    def __init__(self):
        super(LocalAlign, self).__init__()
        self.ui = Ui_Form()
        self.score = SWScoringSystem()
        self.ui.setupUi(self)
        self.stylesheet_file(style_path="static/style/alignment_tab_style.qss")
        QFontDatabase.addApplicationFont(
            ":/fonts/Lora-VariableFont/Lora-VariableFont_wght.ttf"
        )

        #### ====== Signal Buttons  ======####
        # self.ui.load_seq1.clicked.connect()
        # self.ui.load_seq2.clicked.connect()
        self.ui.clear_btn.clicked.connect(self.remove_output)
        self.ui.align_btn.clicked.connect(self.align_clicked)
        # self.ui.save_btn.clicked.connect()

    def stylesheet_file(self, style_path):
        with open(style_path, "r") as f:
            style = f.read()
            self.setStyleSheet(style)

    def align_clicked(self):
        """Retrieving the input values upon clicking the Align button"""
        #### ====== Retrieve Values ======####
        label_1 = self.ui.seq1_label.text() or "No Sample Label Added [First Sequence]"
        input_seq1 = self.ui.textEdit.toPlainText()
        label_2 = self.ui.seq2_label.text() or "No Sample Label Added [First Sequence]"
        input_seq2 = self.ui.textEdit_2.toPlainText()

        #### ====== Handling error for the Input ======####

        try:
            if not input_seq1 or not input_seq2:
                raise ValueError()
            else:
                scoring_system = SWScoringSystem(match=2, mismatch=-1, gap=-1)
                self.algorithm = SmithWatermanAlgorithm(
                    scoring_system, seqA=input_seq1, seqB=input_seq2
                )
                self.start_alignment(input_seq1, input_seq2, label_1, label_2)
        except ValueError:
            self.pop_warning(
                "Wrong Input Field. Please fill up with an appropriate sequence. Make sure to select the correct biomolecule type."
            )

    def start_alignment(self, input_seq1, input_seq2, label_1, label_2):
        #### ====== Handling error for the Input ======####
        local_align = self.algorithm
        aligned_seq_A, aligned_seq_B = local_align.seq_alignment(input_seq1, input_seq2)
        similarity_l = local_align.calc_similarity()
        self.show_output(
            aligned_seq_A, input_seq1, input_seq2, aligned_seq_B, similarity_l
        )

    def show_output(
        self, aligned_seq_A, input_seq1, input_seq2, aligned_seq_B, similarity_l
    ):
        """Output Format for Aligned Sequence"""
        aligned_output = dedent(
            f""" 
                [1] Original Sequence A: \n{input_seq1}
                [2] Original Sequence B: \n{input_seq2}

                [3] Aligned Sequence A: \n{aligned_seq_A}
                [4] Aligned Sequence B: \n{aligned_seq_B}

                [5] PPercentage Similarity of the Two Sequences: {similarity_l} %
                =========================================
            """
        )
        self.ui.textBrowser_2.append(aligned_output)

    def remove_output(self):
        """Clear Button for the Output Section"""
        self.ui.textBrowser_2.clear()

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
