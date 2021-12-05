def transpose(seq):
    return list(zip(*seq))


def to_dec(l):
    return int("".join(map(str, l)), 2)


def chunk(seq, n):
    for i in range(0, len(seq), n):
        yield seq[i:i+n]
