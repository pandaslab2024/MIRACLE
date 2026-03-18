def revcomp(seq):
    comp = str.maketrans("AUGC", "UACG")
    return seq.translate(comp)[::-1]


def generate_candidates(seq, length=10):
    candidates = []
    for i in range(len(seq) - length + 1):
        region = seq[i:i+length]
        tna = revcomp(region)
        candidates.append((i, region, tna))
    return candidates