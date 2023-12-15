from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import numpy as np
import matplotlib
import matplotlib.pyplot as plt


class DotMatrix:
    def __init__(self, M, seqA, seqB):
        self.M = M
        self.seqA = seqA
        self.seqB = seqB

    def matrix_dim(self):
        match = 0
        self.M[0][0] = ""
        for rows in range(1, self.M.shape[0]):
            for cols in range(1, self.M.shape[1]):
                if self.M[rows][0] == self.M[0][cols]:
                    self.M[rows][cols] = "*"
                    if rows == cols:
                        match += 1
                else:
                    self.M[rows][cols] = " "
        mismatch = self.M.shape[0] - match - 1
        return match, mismatch, self.M

    def fill_plot(self, label_1, label_2):
        self.M = np.full((len(self.seqA) + 1, len(self.seqB) + 1), "", dtype=str)
        for rows in range(0, len(self.seqA)):
            self.M[rows + 1][0] = self.seqA[rows : rows + 1]
        for cols in range(0, len(self.seqB)):
            self.M[0][cols + 1] = self.seqB[cols : cols + 1]
        match, mismatch, M = self.matrix_dim()

        cmap = matplotlib.colors.ListedColormap(["dodgerblue", "white"])
        bounds = [0, 0.5, 1]
        norm = matplotlib.colors.BoundaryNorm(bounds, cmap.N)

        fig, ax = plt.subplots(figsize=(10, 10), dpi=100)
        label_section = f"\n{label_1}\n{label_2}"
        fig.text(0.5, 0.90, label_section, fontsize=15, ha="center")
        M_blu = np.delete(self.M, 0, axis=1)
        M_blu = np.delete(M_blu, 0, axis=0)
        M_blu_log = M_blu == "*"
        ax.imshow(M_blu_log, cmap=cmap, norm=norm)

        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_ylabel("Sequence 1", fontsize=15)
        ax.set_xlabel("Sequence 2", fontsize=15)

        subcaption = (
            f"Number of aligned bases: {match}\nNumber of mismatched bases: {mismatch}"
        )
        fig.text(0.5, 0.02, subcaption, fontsize=15, ha="center")

        return fig


class ValidSequence:
    def __init__(self, seqA, seqB):
        self.seqA = seqA
        self.seqB = seqB

    def sequence_type(self, seq):
        dna_alphabet = "ATCG"
        rna_alphabet = "AUCG"
        prot_alphabet = "ATCGRNDEQHILKMFPSWYV"

        seq_upper = seq.upper()

        if all(char in dna_alphabet for char in seq_upper):
            return "DNA"
        elif all(char in rna_alphabet for char in seq_upper):
            return "RNA"
        elif all(char in prot_alphabet for char in seq_upper):
            return "Protein"
        else:
            raise ValueError("Invalid characters in the sequence.")

    def pairseq_valid(self):
        seq1_type = self.sequence_type(self.seqA)
        seq2_type = self.sequence_type(self.seqB)

        if seq1_type == seq2_type:
            return True
        else:
            raise ValueError("Both sequences must have the same sequence type.")
