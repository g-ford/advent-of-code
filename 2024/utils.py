import time
from typing import Callable, Iterable, Sequence, TypeVar

T = TypeVar("T")
PointType = tuple[int, int]


def transpose(seq: Iterable) -> Iterable:
    """Transpose a 2D array"""
    return list(zip(*seq))


def chunk(seq: Sequence, n: int) -> Iterable:
    """Split a sequence into chunks of size n"""
    for i in range(0, len(seq), n):
        yield seq[i : i + n]


def flatten(nested: Iterable[Iterable]) -> Iterable:
    """Flatten a nested iterable"""
    return [item for sublist in nested for item in sublist]


def log_time(method: Callable) -> Callable:
    """Decorator to log the time a function takes to execute"""
    def timed(*args, **kwargs):
        ts = time.time()
        result = method(*args, **kwargs)
        te = time.time()

        print(f"[PERF] {method.__name__} {(te-ts)*1000:2f} ms")
        return result

    return timed


def slide(seq: Sequence[T], window: int) -> Iterable[Sequence[T]]:
    """Slide a window over a sequence"""
    for i in range(len(seq) - window + 1):
        yield seq[i : i + window]


def neighbours(k: int, j: int) -> list[tuple[int, int]]:
    """Returns a list of indexes of the neighbours of k, j
    Neighbours are the 8 cells surrounding the cell in a 2D grid"""
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
    """Returns a list of indexes of the neighbours of k, j where you can only move in the cardinal directions"""
    return [
        (k, j - 1),
        (k - 1, j),
        (k + 1, j),
        (k, j + 1),
    ]


def manhatten_distance(p1: PointType, p2: PointType) -> int:
    """Calculate the manhatten distance between two points

    Manhatten distance is the shortest distance between two points on a grid when
    you can only move in the cardinal directions"""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
