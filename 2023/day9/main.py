# ❯ python -m day9.main
# [PERF] parse_input 1.374960 ms
# [PERF] part1 12.965918 ms
# Part 1:  2174807968
# [PERF] part2 5.629301 ms
# Part 2:  1208

from functools import reduce

import numpy as np
from utils import log_time


def next_in_seq(line):
    """Find the next number in the sequence

    We find the difference between elements, reducing down to 0, then sum up the results"""
    last_numbers = []
    while any(line):
        last_numbers.append(line[-1])
        line = np.diff(line)

    return sum(last_numbers)

def prev_in_seq(line):
    """Find the next number in the sequence

    We find the difference between elements, reducing down to 0, then accumulate
    the differences in reverse order"""
    last_numbers = []
    while any(line):
        last_numbers.append(line[0])
        line = np.diff(line)

    return reduce(lambda x, n: n - x, last_numbers[::-1], 0)

@log_time
def part1(parts):
    return sum(next_in_seq(p) for p in parts)

@log_time
def part2(parts):
    return sum(prev_in_seq(p) for p in parts)


@log_time
def parse_input(lines):
    return [list(map(int, line.strip().split(" "))) for line in lines]


lines = open("day9/input.txt", encoding="utf8").readlines()

parts = parse_input(lines)

print("Part 1: ", part1(parts))
print("Part 2: ", part2(parts))
