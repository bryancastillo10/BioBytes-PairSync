from Bio import SeqIO
from urllib.parse import urlparse


class WebRetrieve:
    """Class for retrieving sequence from NCBI Database"""

    def __init__(self, url):
        self.url = url

    def extract_accession_number(url):
        parsed_url = urlparse(url)
        segments = parsed_url.path.split("/")
        accession_number = segments[-1]
        return accession_number

    def record_from_ncbi(url):
        accession_number = extract_accession_number(url)
        if not accession_number:
            print("Invalid URL. Please provide a valid NCBI nucleotide sequence URL.")
            return
        handle = Entrez.efetch(
            db="nucleotide", id=accession_number, rettype="gb", retmode="text"
        )
        record = SeqIO.read(handle, "genbank")
        handle.close()
        return record

    def get_sequence(self):
        seq_record = self.record_from_ncbi()
        return str(seq_record.seq)
