# ❯ python -m day13.main
# [PERF] parse_input 0.068903 ms
# [PERF] part1 0.268936 ms
# Part 1:  31956
# [PERF] part2 0.001192 ms
# Part 2:  None

from utils import log_time, transpose


def find_reflection(map):
    """Find the reflection point in the map.

    The reflection point may not be in the middle and may be horizontal or vertical."""

    def reflect(map):# first try to find a vertical reflection
        limit = len(map) -1
        for i in range(0, limit):
            # Check each side of the reflection matches until we hit a boundary or fail
            a = i
            b = i+1
            while True:
                if map[a] != map[b] or a < 0 or b > limit:
                    # print("Reflection Failed", i, a, b)
                    break
                if a == 0 or b == limit:
                    # print("Boundary", i, a, b)
                    return i + 1
                a -= 1
                b += 1
        return 0

    return reflect(map), reflect(transpose(map))

@log_time
def part1(parts):
    reflections = [find_reflection(map) for map in parts]

    return sum(r[0] * 100 for r in reflections) + sum(r[1] for r in reflections)

@log_time
def part2(parts):
    pass

@log_time
def parse_input(lines):
    return [b.split("\n") for b in lines.split("\n\n")]




lines = open("day13/input.txt", encoding="utf8").read()

parts = parse_input(lines)

print("Part 1: ", part1(parts))
print("Part 2: ", part2(parts))
