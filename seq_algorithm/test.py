from global_needleman import NeedlemanWunschAlgorithm, NWScoringSystem
from local_smithwaterman import SmithWatermanAlgorithm, SWScoringSystem


def global_alignment(sample_A, sample_B):
    scoring_system = NWScoringSystem(match=1, mismatch=-1, gap=-2)
    global_align = NeedlemanWunschAlgorithm(scoring_system)
    aligned_seq_A, aligned_seq_B = global_align.seq_alignment(sample_A, sample_B)
    percent_similarity_g = global_align.calc_similarity()
    return aligned_seq_A, aligned_seq_B, percent_similarity_g


def local_alignment(sample_A, sample_B):
    scoring_system = SWScoringSystem(match=2, mismatch=-1, gap=-1)
    local_align = SmithWatermanAlgorithm(scoring_system)
    aligned_seq_A, aligned_seq_B = local_align.seq_alignment(sample_A, sample_B)
    percent_similarity_l = local_align.calc_similarity()
    return aligned_seq_A, aligned_seq_B, percent_similarity_l


sample_A = "AGTACATGGTCACTGAGGCTCTGCGCTAGTACGTACGTACGCTAGTCGTAGCTAGTCA"
sample_B = "AGCATGCTAGTACGCTAGTCGTAGCTAGTCACTGAGGCTCTGCGCTAGTACGTACGTACG"

alignment_type = input(
    "Enter 'global' for global alignment or 'local' for local alignment: "
)

print("Original Sequence A:", sample_A)
print("Original Sequence B:", sample_B)
print("\n")

if alignment_type.lower() == "global":
    seqA, seqB, similarity_g = global_alignment(sample_A, sample_B)
    print("Aligned Sequence A:", seqA)
    print("Aligned Sequence B:", seqB)
    print(f"Percentage Similarity of the Two Sequences: {similarity_g} %")

elif alignment_type.lower() == "local":
    seqA, seqB, similarity_l = local_alignment(sample_A, sample_B)
    print("Aligned Sequence A:", seqA)
    print("Aligned Sequence B:", seqB)
    print(f"Percentage Similarity of the Two Sequences: {similarity_l} %")
else:
    print("Invalid choice! Please enter either 'global' or 'local'.")
