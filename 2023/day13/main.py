# ❯ python -m day13.main
# [PERF] parse_input 0.068903 ms
# [PERF] part1 5.541086 ms
# Part 1:  31956
# [PERF] part2 5.600929 ms
# Part 2:  37617

from utils import log_time, transpose


def find_reflection(map, diff=0):
    """Find the reflection point in the map.

    The reflection point may not be in the middle and may be horizontal or vertical.

    Returns a tuple of (vertical reflection, horizontal reflection)"""

    def reflect(map):  # first try to find a vertical reflection
        limit = len(map)
        for i in range(1, limit):
            if sum(stringdiff(*p) for p in zip(reversed(map[:i]), map[i:])) == diff:
                return i
        return 0

    return reflect(map), reflect(transpose(map))


def stringdiff(a, b):
    """Count the number of differences between two strings of equal length"""
    return sum(a != b for a, b in zip(a, b))


@log_time
def part1(parts):
    reflections = [find_reflection(map) for map in parts]

    return sum(r[0] * 100 for r in reflections) + sum(r[1] for r in reflections)


@log_time
def part2(parts):
    reflections = [find_reflection(map, diff=1) for map in parts]

    return sum(r[0] * 100 for r in reflections) + sum(r[1] for r in reflections)


@log_time
def parse_input(lines):
    return [b.split("\n") for b in lines.split("\n\n")]


lines = open("day13/input.txt", encoding="utf8").read()

parts = parse_input(lines)

print("Part 1: ", part1(parts))
print("Part 2: ", part2(parts))
