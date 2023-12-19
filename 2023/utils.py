import time
from typing import Callable, Iterable, Sequence, TypeVar

T = TypeVar("T")
PointType = tuple[int, int]


def transpose(seq: Iterable) -> Iterable:
    return list(zip(*seq))


def chunk(seq: Sequence, n: int) -> Iterable:
    for i in range(0, len(seq), n):
        yield seq[i : i + n]


def flatten(nested: Iterable[Iterable]) -> Iterable:
    return [item for sublist in nested for item in sublist]


def log_time(method: Callable) -> Callable:
    def timed(*args, **kwargs):
        ts = time.time()
        result = method(*args, **kwargs)
        te = time.time()

        print(f"[PERF] {method.__name__} {(te-ts)*1000:2f} ms")
        return result

    return timed


def slide(seq: Sequence[T], window: int) -> Iterable[Sequence[T]]:
    for i in range(len(seq) - window + 1):
        yield seq[i : i + window]


def neighbours(k: int, j: int) -> list[tuple[int, int]]:
    """Returns a list of indexes of the neighbours of k, j"""
    return [
        (k - 1, j - 1),
        (k, j - 1),
        (k + 1, j - 1),
        (k - 1, j),
        (k + 1, j),
        (k - 1, j + 1),
        (k, j + 1),
        (k + 1, j + 1),
    ]


def compass_neighbours(k: int, j: int) -> list[tuple[int, int]]:
    """Returns a list of indexes of the neighbours of k, j"""
    return [
        (k, j - 1),
        (k - 1, j),
        (k + 1, j),
        (k, j + 1),
    ]


def manhatten_distance(p1: PointType, p2: PointType) -> int:
    """Calculate the manhatten distance between two points

    Manhatten distance is the shortest distance between two points on a grid when
    you can only move horizontally or vertically
    """
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
