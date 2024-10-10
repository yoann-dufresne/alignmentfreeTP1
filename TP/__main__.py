from TP.loading import load_directory
from TP.kmers import stream_kmers, kmer2str



def jaccard_from_sorted_lists(lstA, lstB):
    idxA = 0
    idxB = 0

    intersection = 0
    union = 0

    while idxA < len(lstA) and idxB < len(lstB):
        union += 1
        if lstA[idxA] == lstB[idxB]:
            intersection += 1
            idxA += 1
            idxB += 1
        elif lstA[idxA] < lstB[idxB]:
            idxA += 1
        else:
            idxB += 1

    union += len(lstA) - idxA
    union += len(lstB) - idxB

    return intersection / union



if __name__ == "__main__":
    print("Computation of Jaccard similarity between files")

    # Load all the files in a dictionary
    print("Loading files")
    files = load_directory("data")
    k = 21
    
    filenames = list(files.keys())
    
    # Create all the kmer lists (can be expensive in memory)
    print("Computing all kmer vectors")
    kmer_lists = {}
    for filename in filenames:
        kmer_lists[filename] = []
        # Enumerate all the sequences from a fasta
        for seq in files[filename]:
            kmer_lists[filename].extend(stream_kmers(seq, k))
        # Sort the kmer lists to speed up the comparison
        kmer_lists[filename].sort()

    print("Computing Jaccard similarity for all pairs of samples")
    for i in range(len(files)):
        for j in range(i+1, len(files)):
            jaccard = jaccard_from_sorted_lists(kmer_lists[filenames[i]], kmer_lists[filenames[j]])
            print(filenames[i], filenames[j], jaccard)
