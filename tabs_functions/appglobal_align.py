from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QFontDatabase

from ui.tabs.global_align_ui import Ui_Form


class GlobalAlign(QWidget):
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
    # self.ui.align_btn.clicked.connect(self.align_clicked)
    # self.ui.save_btn.clciked.connect()

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
        input_seq2 = self.ui.textEdit.toPlainText()

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
