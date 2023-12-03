# ❯ python -m day3.main
# ❯ python -m day3.main
# [PERF] part1 6.876230 ms
# Part 1: 519444
# [PERF] part2 0.046730 ms
# Part 2: 74528807

import math
from collections import defaultdict

from utils import log_time, neighbours

gears = defaultdict(list)


@log_time
def part1(rows):
    """Sum the part numbers"""
    parts = []
    for r, row in enumerate(rows):
        current_digit = []
        for col, ch in enumerate(row):
            if ch.isdigit():
                current_digit.append(ch)
            # Check if this is the end of the number which is either
            # the end of the row or the next char is a symbol
            if col == len(row) - 1 or not row[col + 1].isnumeric():
                if current_digit:
                    if is_part(current_digit, (r, col), rows):
                        parts.append(int("".join(current_digit)))
                    current_digit = []
    # print("All parts:", parts)
    return sum(parts)


def is_part(part, pos, grid):
    """Check if the part is a part number
    A part is adjacent to a symbol"""

    for i in range(len(part)):
        # check each digit in the part
        test_pos = (pos[0], pos[1] - i)
        for n in neighbours(*test_pos):
            if in_bounds(n, grid):
                # check for symbols other than dots
                if not grid[n[0]][n[1]].isnumeric() and grid[n[0]][n[1]] != ".":
                    # if it is a gear add it to the collection for part 2
                    if grid[n[0]][n[1]] == "*":
                        gears[n].append(int("".join(part)))
                    return True
    return False


def in_bounds(pos, grid):
    """Check if the position is in the grid"""
    return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])


@log_time
def part2():
    """Find the sum of the product of parts for gears with two parts"""
    return sum(math.prod(parts) for parts in gears.values() if len(parts) == 2)


lines = [l.strip() for l in open("day3/input.txt", encoding="utf8").readlines()]

print("Part 1:", part1(lines))
print("Part 2:", part2())
