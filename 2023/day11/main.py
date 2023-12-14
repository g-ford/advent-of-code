
from itertools import combinations

import networkx as nx
from utils import log_time, manhatten_distance, transpose


@log_time
def part2(parts, expand=2):
    galaxies = []
    # Expanding by once less than asked for, as we always add one to the end of
    # each iteration
    expand = expand - 1
    r = 0
    for i, row in enumerate(parts):
        c = 0
        if row[0] == '-':
            r += expand
        for j, col in enumerate(row):
            if col == '-':
                c += expand
            if col == '#':
                galaxies.append((r, c, i, j))
            c += 1
        r += 1

    pairs = combinations(galaxies, 2)
    return sum(manhatten_distance(*p) for p in pairs)

@log_time
def parse_input(lines):
    lines = [line.strip() for line in lines]

    # expand the map vertically
    empty = [i for i, line in enumerate(lines) if '#' not in line]
    for i in empty[::-1]: # insert in reverse order so indexes still match
        lines[i] = '-' * len(lines[0])

    # expand the map horizontally
    transposed = transpose(lines)
    empty = [i for i, line in enumerate(transposed) if '#' not in line]
    for i in empty[::-1]: # insert in reverse order so indexes still match
        transposed[i] = '-' * len(transposed[0])

    # flip the matrix back to original orientation
    lines = transpose(transposed)
    return lines


lines = open("day11/input.txt", encoding="utf8").readlines()

parts = parse_input(lines)

print("Part 1: ", part2(parts))
print("Part 2: ", part2(parts, 1000000))
