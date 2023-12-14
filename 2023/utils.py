import time


def transpose(seq):
    return list(zip(*seq))


def to_dec(l):
    return int("".join(map(str, l)), 2)


def chunk(seq, n):
    for i in range(0, len(seq), n):
        yield seq[i : i + n]


def flatten(l):
    return [item for sublist in l for item in sublist]


def log_time(method):
    def timed(*args, **kwargs):
        ts = time.time()
        result = method(*args, **kwargs)
        te = time.time()

        print(f"[PERF] {method.__name__} {(te-ts)*1000:2f} ms")
        return result

    return timed


def slide(seq, window):
    for i in range(len(seq) - window + 1):
        yield seq[i : i + window]


def neighbours(k, j):
    """Returns a list of indexes of the neighbours of k, j"""
    return [
        (k - 1, j - 1), (k, j - 1),(k + 1, j - 1),
        (k - 1, j),                (k + 1, j),
        (k - 1, j + 1),(k, j + 1), (k + 1, j + 1),
    ]


def compass_neighbours(k, j):
    """Returns a list of indexes of the neighbours of k, j"""
    return [
                 (k, j - 1),
        (k - 1, j),         (k + 1, j),
                 (k, j + 1),
    ]


def manhatten_distance(p1, p2):
    """ Calculate the manhatten distance between two points

    Manhatten distance is the shortest distance between two points on a grid when
    you can only move horizontally or vertically
    """
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])