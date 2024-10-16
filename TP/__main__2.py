from TP_corr.loading import load_directory
from TP_corr.kmers import stream_kmers, kmer2str
import heapq as heap
import pandas as pd

def bottom_minhash(seq, k, s):              #liste les kmers et ne garde que les s plus petits
    lst = [-float('inf') for _ in range(s)]
    heap.heapify(lst)
    max_element = -float('inf')
    lst_finale = []
    for kmer in stream_kmers(seq, k):
        if -kmer > max_element :
            heap.heappushpop(lst, -kmer)
            max_element = lst[0]
    for l in lst :
         lst_finale.append(-l)
    lst_finale.sort()
    return lst_finale

def partition_minhash(seq, k, s) :          #créé s buckets avec seulement le minimum par bucket
    lst = [float('inf') for _ in range(s)]
    for kmer in stream_kmers(seq, k):
        idx = kmer%s
        if kmer < lst[idx] :
            lst[idx] = kmer
    lst.sort()
    return lst


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
    s = 1000
    filenames = list(files.keys())
    df = pd.DataFrame(index = filenames, columns = filenames)
    
    # Create all the kmer lists (can be expensive in memory)
    print("Computing all kmer vectors")
    kmer_lists = {}
    for filename in filenames:
        kmer_lists[filename] = []
        # Enumerate all the sequences from a fasta
        for seq in files[filename]:
            kmer_lists[filename].extend(partition_minhash(seq, k, s))

    print("Computing Jaccard similarity for all pairs of samples")
    for i in range(len(files)):
        print(filenames[i])
        df.loc[filenames[i], filenames[i]] = 1.0
        for j in range(i+1, len(files)):
            jaccard = jaccard_from_sorted_lists(kmer_lists[filenames[i]], kmer_lists[filenames[j]])
            df.loc[filenames[i], filenames[j]] = jaccard
    print(df)
