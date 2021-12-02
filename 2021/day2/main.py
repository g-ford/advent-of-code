
from collections import defaultdict


def parse_line(l):
    parts = l.split()
    return (parts[0], int(parts[1]))


input = list(map(parse_line, open('input.txt').readlines()))

counter = defaultdict(int)
for k, v in input:
    counter[k] += v

horizontal = counter['forward']
vertical = 0 + counter['down'] - counter['up']
print("Part A:", horizontal * vertical)

aim = h = d = 0
for k, v in input:
    if k == 'forward':
        h += v
        d += aim * v
    if k == 'down':
        aim += v
    if k == 'up':
        aim -= v

print("Part B:", h * d)
