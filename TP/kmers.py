
def kmer2str(val, k):
    """ Transform a kmer integer into a its string representation
    :param int val: An integer representation of a kmer
    :param int k: The number of nucleotides involved into the kmer.
    :return str: The kmer string formatted
    """
    letters = ['A', 'C', 'T', 'G']
    str_val = []
    for _ in range(k):
        str_val.append(letters[val & 0b11])
        val >>= 2

    str_val.reverse()
    return "".join(str_val)

def encode_nuc(letter) :
    encoding ={'A':0, 'C':1, 'T':2, 'G':3}
    return encoding[letter]

def encode_kmer(seq, k) :
    kmer = 0
    for letter in seq[0:k]:
        kmer <<= 2
        kmer += encode_nuc(letter)
    return kmer

def encode_rletter(letter) :
    encoding_reverse ={'A':'T', 'C':'G', 'T':'A', 'G':'C'}
    return encoding_reverse[letter]

def encode_rkmer(seq,k):
    rkmer = 0
    rseq = seq[0:k]
    for letter in rseq[::-1]:
        rkmer <<= 2
        rletter = encode_rletter(letter)
        rkmer += encode_nuc(rletter)
    return rkmer

def stream_kmers(seq, k):
    mask = (1<<(2*(k-1)))-1
    kmer = encode_kmer(seq,k)
    rkmer = encode_rkmer(seq,k)
    for i in range(len(seq)-(k-1)-1) :
        yield min(kmer, rkmer)
        kmer &= mask
        kmer <<= 2
        kmer |= encode_nuc(seq[i+k])
        rkmer >>=2
        rletter = encode_rletter(seq[i+k])
        rkmer |= encode_nuc(rletter)<<(2*(k-1))
    yield min(kmer, rkmer)
