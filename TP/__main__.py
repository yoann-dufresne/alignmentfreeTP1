from TP.loading import load_directory
from TP.kmers import stream_kmers, kmer2str

def create_index(seq, k):   #dictionnaire avec tous les kmers canoniques (clés) 
                            #et leur fréquence d'apparition dans la séquence 1 (valeur)
    index = dict()
    for kmer in stream_kmers(seq, k):
        if kmer not in index :
            index[kmer] = 1
        else :
            index[kmer] += 1
    return index


def jaccard(fileA, fileB, k): #calcule la distance Jaccard entre deux séquences selon l'intersection et l'union de leur kmer
    j = 0
    index = create_index(fileA, k)
    files_intersect = 0
    files_union = sum(index.values())
    for kmer in stream_kmers(fileB, k):
        if kmer in index and index[kmer] > 0 :
            files_intersect += 1
            index[kmer] -= 1
        else :
            files_union += 1
    j = files_intersect/files_union
    return j

def concatenate_seq(seq):       #accolle les différentes séquences d'un fichier fasta
    new_seq = ""
    for l in seq :
        new_seq += l
    return new_seq


if __name__ == "__main__":
    print("Computation of Jaccard similarity between files")

    # Load all the files in a dictionary
    files = load_directory("data")
    k = 21
    
    print("Computing Jaccard similarity for all pairs of samples")
    filenames = list(files.keys())
    for n in range(len(files)):
        files[filenames[n]] = concatenate_seq(files[filenames[n]])  #permet d'éviter le problème de plusieurs séquences dans un fichier

    for i in range(len(files)):
       for j in range(i+1, len(files)):
            
            j_val = jaccard(files[filenames[i]],files[filenames[j]],k)
            print(filenames[i], filenames[j], j_val)
