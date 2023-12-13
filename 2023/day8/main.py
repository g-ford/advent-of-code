
# ❯ python -m day8.main
# [PERF] parse_input 0.861883 ms
# [PERF] part1 2.302885 ms
# Part 1:  17141
# [PERF] part2 14.541149 ms
# Part 2:  10818234074807

import math
import re
from collections import namedtuple

from utils import log_time

node = namedtuple("Node", ["name", "left", "right"])

@log_time
def part1(instructions, tree):
    current = tree['AAA']
    steps = 0

    while current.name != 'ZZZ':
        if instructions[steps % len(instructions)] == 'L':
            current = tree[current.left]
        else:
            current = tree[current.right]
        steps += 1

    return steps

@log_time
def part2(instructions, tree):
    starting = [n for n in tree.values() if n.name[2] == 'A']
    steps = 0

    loops = []
    for n in starting:
        current = n
        steps = 0

        while not current.name[2] == 'Z':
            if instructions[steps % len(instructions)] == 'L':
                current = tree[current.left]
            else:
                current = tree[current.right]
            steps += 1
        loops.append(steps)

    return math.lcm(*loops)



@log_time
def parse_input(lines):
    instructions = lines[0].strip()

    nodes = {}
    for row in lines[2:]:
       name, left, right = re.findall(r"\w+", row)
       nodes[name] = node(name, left, right)
    return instructions, nodes


lines = open("day8/input.txt", encoding="utf8").readlines()

instructions, tree = parse_input(lines)

print("Part 1: ", part1(instructions, tree))
print("Part 2: ", part2(instructions, tree))
