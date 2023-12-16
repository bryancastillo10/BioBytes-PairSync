class ValidSequence:
    """Class for validating the input string if it is indeed
    a DNA, RNA or Protein based on the reference bases"""

    def __init__(self, seqA, seqB):
        self.seqA = seqA
        self.seqB = seqB

    def sequence_type(self, seq):
        dna_bases = "ATCG"
        rna_bases = "AUCG"
        protein_aa = "ATCGRNDEQHILKMFPSWYV"

        sequence = seq.upper()

        if all(char in dna_bases for char in sequence):
            return "DNA"
        elif all(char in rna_bases for char in sequence):
            return "RNA"
        elif all(char in protein_aa for char in sequence):
            return "Protein"
        else:
            raise ValueError("Invalid characters in the sequence.")

    def pairseq_valid(self):
        seqA_type = self.sequence_type(self.seqA)
        seqB_type = self.sequence_type(self.seqB)

        if seqA_type == seqB_type:
            return True
        else:
            raise ValueError("Both sequences must have the same sequence type.")
