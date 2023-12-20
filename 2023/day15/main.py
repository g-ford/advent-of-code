# ❯ python -m day15.main
# [PERF] parse_input 0.012875 ms
# [PERF] part1 1.489878 ms
# Part 1:  508498
# [PERF] part2 2.802134 ms
# Part 2:  279116

from collections import defaultdict
import re
from utils import log_time
from rich import print


def str_hash(plain):
    """ Calculate the hash of a string """
    hash = 0
    for c in plain:
        hash += ord(c)
        hash = hash * 17
        hash = hash % 256
    return hash

def focus_power(boxes):
    """ Calculate the power of the focus """

    def box_power(box_num, box):
        power = 0
        for slot_num, (label, lens) in enumerate(box.items()):
            power += (1 + box_num) * (1 + slot_num) * lens
        return power

    power = 0
    for k, box in boxes.items():
        power += box_power(k, box)
    return power

@log_time
def part1(parts):
    return sum(str_hash(p.strip()) for p in parts[0].split(","))


@log_time
def part2(parts):
    instructions = re.findall(r"(\w+)([-=])(\d+)?", parts[0])
    boxes = defaultdict(dict)

    for s, op, num in instructions:
        box = str_hash(s)

        if op == "-":
            try:
                del boxes[box][s]
            except KeyError:
                pass
        if op == "=":
            boxes[box][s] = int(num)

    return focus_power(boxes)


@log_time
def parse_input(lines):
    return [line.strip() for line in lines.splitlines()]


lines = open("day15/input.txt", encoding="utf8").read()

parts = parse_input(lines)

print("Part 1: ", part1(parts))
print("Part 2: ", part2(parts))
