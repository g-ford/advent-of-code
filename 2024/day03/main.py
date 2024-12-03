from utils import log_time
import re

@log_time
def part1(parts):
    """Sum all the products together"""
    return sum(a * b for a, b in parts)


@log_time
def part2(parts):
    """Sum all the products together, but only if we are in a 'do()' block"""
    summing = True
    result = 0
    for op in parts:
        if op[0] == "do()":
            summing = True
        elif op[0] == "don't()":
            summing = False
        elif summing: # assume it is a mul() operation
            result += int(op[1]) * int(op[2])
    return result


@log_time
def parse_input(lines):
    """Parse the input into a list of tuples of ints"""
    ops = re.findall(r"mul\((\d+),(\d+)\)", lines)
    return [(int(a), int(b)) for a, b in ops]


@log_time
def parse_input2(lines):
    """Parse the input into a list of operations and arguments"""
    ops = re.findall(r"(mul\((\d+),(\d+)\)|don't\(\)|do\(\))", lines)
    return ops

lines = open("day03/input.txt", encoding="utf8").read()
parts = parse_input(lines)
parts2 = parse_input2(lines)

print("Part 1: ", part1(parts))
print("Part 2: ", part2(parts2))
