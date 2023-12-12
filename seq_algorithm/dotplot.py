import numpy as np
import matplotlib
import matplotlib.pyplot as plt


# Biomolecules Dictionary for Validation
Biomolecules = {
    "DNA": ["A", "T", "C", "G"],
    "RNA": ["A", "U", "C", "G"],
    "Protein": [
        "A",
        "R",
        "N",
        "D",
        "C",
        "E",
        "Q",
        "G",
        "H",
        "I",
        "L",
        "K",
        "M",
        "F",
        "P",
        "S",
        "T",
        "W",
        "Y",
        "V",
        "*",
    ],
}


class DotMatrix:
    def __init__(self, M, seqA, seqB, seq_type="DNA"):
        self.M = M
        self.seq_type = seq_type
        self.seqA = seqA
        self.seqB = seqB
        self.is_valid = self.__validate()
        if not self.is_valid:
            raise ValueError()

    def __validate(self):
        if set(Biomolecules[self.seq_type]).issuperset(self.seqA) and set(
            Biomolecules[self.seq_type]
        ).issuperset(self.seqB):
            return True

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

    def fill_plot(self, figsize=(10, 10), dpi=70):
        self.M = np.full((len(self.seqA) + 1, len(self.seqB) + 1), "", dtype=str)
        for rows in range(0, len(self.seqA)):
            self.M[rows + 1][0] = self.seqA[rows : rows + 1]
        for cols in range(0, len(self.seqB)):
            self.M[0][cols + 1] = self.seqB[cols : cols + 1]
        match, mismatch, M = self.matrix_dim()

        cmap = matplotlib.colors.ListedColormap(["dodgerblue", "white"])
        bounds = [0, 0.5, 1]
        norm = matplotlib.colors.BoundaryNorm(bounds, cmap.N)

        fig, ax = plt.subplots(figsize=figsize, dpi=dpi)
        M_blu = np.delete(self.M, 0, axis=1)
        M_blu = np.delete(self.M, 0, axis=0)
        M_blu_log = M_blu == "*"
        ax.imshow(M_blu_log, cmap=cmap, norm=norm)

        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_ylabel("Sequence 1")
        ax.set_xlabel("Sequence 2")

        subcaption = (
            f"Number of aligned bases: {match}\nNumber of unaligned bases: {mismatch}"
        )
        fig.text(0.5, 0.02, subcaption, fontsize=10, ha="center")


# Example Usage
sequence1 = "ATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGAT"
sequence2 = "ATCGATAGATCGATCGATAGATCGATCGATCGATCGATCGATCGATCGAT"

dm = DotMatrix(M=None, seqA=sequence1, seqB=sequence2, seq_type="DNA")
dm.fill_plot(figsize=(8, 8), dpi=80)
plt.show()
