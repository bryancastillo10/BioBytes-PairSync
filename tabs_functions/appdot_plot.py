from PyQt5.QtWidgets import (
    QWidget,
    QMessageBox,
    QGraphicsPixmapItem,
    QGraphicsScene,
    QFileDialog,
    QLineEdit,
    QPlainTextEdit,
)

from PyQt5.QtGui import QFontDatabase, QImage, QPixmap
from PyQt5.QtCore import Qt

import matplotlib.backends.backend_qt5agg as FigureCanvas
import numpy as np

from ui.tabs.dot_plot_ui import Ui_Form
from seq_algorithm.dotplot import DotMatrix
from seq_algorithm.validate import ValidSequence


class DotPlot(QWidget):
    """Second Tab of the GUI App. Dot Plot Sequence Alignment"""

    def __init__(self):
        super(DotPlot, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.stylesheet_file(style_path="static/style/dot_plot_tab_style.qss")
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
        self.ui.save_btn.clicked.connect(self.save_img)
        self.ui.clear_btn.clicked.connect(self.remove_output)
        self.ui.plot_btn.clicked.connect(self.plot_clicked)

    def stylesheet_file(self, style_path):
        with open(style_path, "r") as f:
            style = f.read()
            self.setStyleSheet(style)

    def plot_clicked(self):
        """Retrieving the input values upon clicking the Plot button"""
        #### ====== Retrieve Values ======####
        label_1 = (
            self.ui.label_seq1.text() or " No Sample Label Added [First Sequence] "
        )
        input_seq1 = self.ui.textEdit.toPlainText()
        label_2 = (
            self.ui.label_seq2.text() or " No Sample Label Added [Second Sequence] "
        )
        input_seq2 = self.ui.textEdit_2.toPlainText()
        """Implements the methods on class DotMatrix"""
        #### ====== Handling error for the Input ======####
        self.valid = ValidSequence(seqA=input_seq1, seqB=input_seq2)
        try:
            if not input_seq1 or not input_seq2:
                raise ValueError()
            elif self.valid.pairseq_valid():
                self.dm = DotMatrix(
                    M=np.empty((1, 1), dtype=str), seqA=input_seq1, seqB=input_seq2
                )
                fig = self.dm.fill_plot(label_1=label_1, label_2=label_2)
                self.embed_plot(fig)
            else:
                raise ValueError()
        except ValueError as e:
            self.pop_warning(
                f"DotMatrix Error: Wrong Input Field. Please fill up with an appropriate sequence. "
            )

    def embed_plot(self, fig):
        """Embed the MatplotLib plot into the QGraphicsView"""
        ###===  Render Matplotlib through Canvas ===###
        canvas = FigureCanvas.FigureCanvasQTAgg(fig)
        canvas.draw()
        width, height = canvas.get_width_height()

        img = QImage(canvas.buffer_rgba(), width, height, QImage.Format_RGBA8888)

        if not self.ui.graphicsView.scene():
            self.ui.graphicsView.setScene(QGraphicsScene())

        ###===  QGraphicsView Adjustment ===###
        pixmap_item = QGraphicsPixmapItem(QPixmap(img))
        self.ui.graphicsView.scene().clear()
        self.ui.graphicsView.setFixedSize(800, 600)
        self.ui.graphicsView.setSceneRect(0, 0, img.width(), img.height())
        self.ui.graphicsView.fitInView(
            self.ui.graphicsView.sceneRect(), Qt.KeepAspectRatio
        )
        self.ui.graphicsView.scene().addItem(pixmap_item)

    def load_file(self, label_widget: QLineEdit, sequence_widget: QPlainTextEdit):
        """Load Sequence from a file"""
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

    def remove_output(self):
        """Clear Button for the Output Section"""
        self.ui.graphicsView.scene().clear()

    def save_img(self):
        """Save the content of the QGraphicsView's viewport as a PNG file"""
        file_dialog = QFileDialog(self)
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        file_dialog.setNameFilter("PNG Files (*.png)")

        if file_dialog.exec_() == QFileDialog.Accepted:
            path = file_dialog.selectedFiles()[0]
            if self.ui.graphicsView.scene():
                viewport = self.ui.graphicsView.viewport()
                screenshot = viewport.grab()
                screenshot.save(path)

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
