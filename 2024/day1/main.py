from collections import Counter
from typing import Sequence


def parseInput(filename: str) -> tuple[Sequence[int], Sequence[int]]:
    with open(filename) as f:
        lines = f.readlines()

    a, b = zip(*(map(int, line.split()) for line in lines))

    return list(a), list(b)

def part1(data: tuple[Sequence[int], Sequence[int]]) -> None:
    """ Part 1: Find the sum of the absolute differences between the sorted pairs """
    a = sorted(data[0])
    b = sorted(data[1])
    paird = zip(a, b)

    print("Part 1: ", sum([abs(x - y) for x, y in paird]))

def part2(data: tuple[Sequence[int], Sequence[int]]) -> None:
    """ Part 2: Find the sum of the left multiplied by the frequency of the right """
    counted = Counter(data[1])
    print("Part 2: ", sum(counted[x] * x for x in data[0]))


data = parseInput('./day1/input.txt')

print("Day 1 of 2024")
part1(data)
part2(data)