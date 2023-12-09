from Bio import Entrez, SeqIO
from urllib.parse import urlparse
from PyQt5.QtWidgets import QMessageBox

Entrez.email = "bryan@gmail.com"


class WebRetrieve:
    """Class for retrieving sequence from NCBI Database"""

    def __init__(self, url):
        self.url = url

    def extract_accession_number(self):
        parsed_url = urlparse(self.url)
        segments = parsed_url.path.split("/")
        accession_number = segments[-1]
        return accession_number

    def record_from_ncbi(self):
        accession_number = self.extract_accession_number()
        if not accession_number:
            return f"Invalid URL. Please provide a valid NCBI nucleotide sequence URL."
        handle = Entrez.efetch(
            db="nucleotide", id=accession_number, rettype="gb", retmode="text"
        )
        record = SeqIO.read(handle, "genbank")
        handle.close()
        return record

    def get_sequence(self):
        try:
            seq_record = self.record_from_ncbi()
            if seq_record is not None:
                return str(seq_record.seq)
            else:
                self.show_warning("")
        except Exception:
            self.pop_error(
                "Invalid URL. Please provide a valid NCBI Nucleotide Sequence URL"
            )
            pass

    def pop_error(self, message):
        pop_box = QMessageBox()
        pop_box.setIcon(QMessageBox.Warning)
        pop_box.setWindowTitle("Invalid Input Warning")
        pop_box.setText(message)
        ####===== Set Style ======####
        pop_box.setStyleSheet(
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
        pop_box.exec_()
