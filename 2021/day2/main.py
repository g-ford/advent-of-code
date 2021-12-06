
from collections import defaultdict
from utils import log_time


def parse_line(l):
    parts = l.split()
    return (parts[0], int(parts[1]))


@log_time
def part_a(input):
    counter = defaultdict(int)
    for k, v in input:
        counter[k] += v

    horizontal = counter['forward']
    vertical = 0 + counter['down'] - counter['up']
    return horizontal * vertical


@log_time
def part_b(input):
    aim = h = d = 0
    for k, v in input:
        if k == 'forward':
            h += v
            d += aim * v
        if k == 'down':
            aim += v
        if k == 'up':
            aim -= v
    return h * d


input = list(map(parse_line, open('day2/input.txt').readlines()))

result_a = part_a(input)
result_b = part_b(input)

print("Part A:", result_a)
print("Part B:", result_b)
