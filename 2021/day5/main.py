from collections import Counter
from utils import log_time


def parse_points(line):
    a, _, b = line.split(' ')

    def points(str):
        return tuple(map(int, str.split(',')))

    return (points(a), points(b))


def gen_points(from_points):
    points = []
    for a, b in from_points:
        if a[0] == b[0]:
            new_points = [(a[0], x)
                          for x in range(min(a[1], b[1]), max(a[1], b[1]) + 1)]
        elif a[1] == b[1]:
            new_points = [(x, a[1])
                          for x in range(min(a[0], b[0]), max(a[0], b[0]) + 1)]
        else:
            if a[0] > b[0]:
                xs = range(a[0], b[0] - 1, -1)
            else:
                xs = range(a[0], b[0] + 1)

            if a[1] > b[1]:
                ys = range(a[1], b[1] - 1, -1)
            else:
                ys = range(a[1], b[1] + 1)
            new_points = list(zip(xs, ys))
        points += new_points

    return points


@log_time
def part_a(input):
    filtered = [x for x in input if x[0][0] == x[1][0] or x[0][1] == x[1][1]]
    counts = Counter(gen_points(filtered))
    overlaps = [k for k, v in counts.items() if v > 1]
    return len(overlaps)


@log_time
def part_b(input):
    counts = Counter(gen_points(input))
    overlaps = [k for k, v in counts.items() if v > 1]
    return len(overlaps)


input = list(map(parse_points, open('day5/input.txt').readlines()))

result_a = part_a(input)
result_b = part_b(input)
print("Part A:", result_a)
print("Part B:", result_b)
