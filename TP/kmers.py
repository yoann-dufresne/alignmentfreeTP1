from collections import defaultdict

def encode_nucl(letter):
    encoding = {'A': 0, 'C': 1, 'T': 2, 'G': 3}
    return encoding[letter]

def encode_kmer(seq, k):
    kmer = 0
    for letter in seq[0:k]:
        kmer <<= 2
        kmer += encode_nucl(letter)
    return kmer

def enumerate_kmer(seq, k):
    kmer = encode_kmer(seq, k) #seq[0:k]
    mask = (1 << (2*(k-1))) - 1
    for i in range(len(seq) - k + 1):
        yield kmer
        kmer &= mask # kmer = kmer[1:] #
        kmer <<= 2 # kmer.append(seq[i + k])
        kmer |= encode_nucl(seq[i + k - 1])
    yield kmer


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

def stream_kmers(text, k):
    # --- To complete ---
    res = defaultdict(int)
    for i in range(len(text)-k+1):
        res[encode_kmer(text[i:i+k], k)] += 1
    return res
