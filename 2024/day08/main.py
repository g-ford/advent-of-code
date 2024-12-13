from collections import defaultdict
from itertools import combinations
from utils import log_time


def print_map(antinode_map, MAX_X, MAX_Y):
    for i in range(MAX_X):
        for j in range(MAX_Y):
            if (i, j) in antinode_map:
                print("#", end="")
            else:
                print(".", end="")
        print()

@log_time
def part1(parts, with_freq=False):
    size = complex(*parts[1])
    MAX_X = int(size.real)
    MAX_Y = int(size.imag)
    MIN_X = MIN_Y = 0

    antannae_map = defaultdict(list)
    for cell in parts[0]:
        antannae_map[cell[1]].append(cell[0])

    antinode_map = set()
    for _, cells in antannae_map.items():
        cells = [complex(*c) for c in cells]
        pairs = combinations(cells, 2)
        for a, b in pairs:
            diff = a - b

            new_a = a + diff
            new_b = b - diff

            new_points = [new_a, new_b]

            for new_point in new_points:
                if MIN_X <= new_point.real < MAX_X and MIN_Y <= new_point.imag < MAX_Y:
                    antinode_map.add((int(new_point.real), int(new_point.imag)))

            if with_freq:
                # add all the antanea as anitnodes
                antinode_map.add((int(a.real), int(a.imag)))
                antinode_map.add((int(b.real), int(b.imag)))

                # and then keep moving by diff until we reach an edge
                while MIN_X <= new_a.real < MAX_X and MIN_Y <= new_a.imag < MAX_Y:
                    antinode_map.add((int(new_a.real), int(new_a.imag)))
                    new_a += diff
                while MIN_X <= new_b.real < MAX_X and MIN_Y <= new_b.imag < MAX_Y:
                    antinode_map.add((int(new_b.real), int(new_b.imag)))
                    new_b -= diff


    # print_map(antinode_map, MAX_X, MAX_Y)
    return len(antinode_map)


@log_time
def part2(parts):
    return part1(parts, with_freq=True)


@log_time
def parse_input(lines):
    cells = []
    size = (len(lines.split("\n")), len(lines.split("\n")[0]))
    for i, line in enumerate(lines.split("\n")):
        for j, cell in enumerate(line):
            if cell != ".":
                cells.append(((i, j), cell))
    return cells, size



lines = open("day08/input.txt", encoding="utf8").read()

parts = parse_input(lines)

print("Part 1: ", part1(parts))
print("Part 2: ", part2(parts))
