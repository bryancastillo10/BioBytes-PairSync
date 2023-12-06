from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QFontDatabase

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

    def stylesheet_file(self, style_path):
        style_path = "static/style/basic_info_tab_style.qss"
        with open(style_path, "r") as f:
            style = f.read()
            self.setStyleSheet(style)

    def start_clicked(self):
        #### ====== User Input  ======####
        type_choice = self.ui.comboBox.currentText()
        sample_label = self.ui.lineEdit.text()

        if sample_label is not None:
            user_output = (
                f"Biomolecule Type: {type_choice} \nSample Label: {sample_label}"
            )
        else:
            user_output = (
                f"Biomolecule Type: {type_choice} \nSample Label: [No Label Added]"
            )

        self.ui.textBrowser.append(user_output)

    def remove_output(self):
        self.ui.textBrowser.clear()
