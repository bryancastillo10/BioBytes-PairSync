import numpy as np
import matplotlib as plt
import matplotlib.pyplot as pltpy


# Function for the Dot Plot Algorithm
def fillMat(M):
    count = 0
    M[0][0] = ""
    for rows in range(1, M.shape[0]):
        for cols in range(1, M.shape[1]):
            if M[rows][0] == M[0][cols]:
                M[rows][cols] = "*"
                if rows == cols:
                    count += 1
            else:
                M[rows][cols] = " "
    incorr = M.shape[0] - count - 1
    print(f"Number of aligned bases: {count}")
    print(f"Number of unaligned bases: {incorr} \n")


# def fill_print():
#     D = np.zeros([len(sequence1) + 1, len(sequence2) + 1], dtype=str)
#     for r in range(0, len(sequence1)):
#         D[r + 1][0] = sequence1[r : r + 1]
#     for c in range(0, len(sequence2)):
#         D[0][c + 1] = sequence2[c : c + 1]
#     fillMat(D)
#     print(D)


def fill_plot():
    M = np.zeros([len(sequence1) + 1, len(sequence2) + 1], dtype=str)
    # print(D), print(D.shape[0])
    for rows in range(0, len(sequence1)):
        M[rows + 1][0] = sequence1[rows : rows + 1]
    for cols in range(0, len(sequence2)):
        M[0][c + 1] = sequence2[cols : cols + 1]
    fillMat(M)

    cmap = plt.colors.ListedColormap(["dodgerblue", "white"])
    bounds = [0, 0.5, 1]
    norm = plt.colors.BoundaryNorm(bounds, cmap.N)

    fig, ax = pltpy.subplots(figsize=(10, 10), dpi=70)
    D_red = np.delete(D, 0, axis=1)
    D_red = np.delete(D, 0, axis=0)
    D_red_log = D_red == "*"
    ax.imshow(D_red_log, cmap=cmap, norm=norm)


# Example Usage
sequence1 = "GAGATTACAGATTACAT"
sequence2 = "TACCATTGGATTACAGT"
