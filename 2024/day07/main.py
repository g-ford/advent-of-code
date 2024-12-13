from dataclasses import dataclass
from itertools import product
from typing import List
from utils import log_time
from operator import add, mul


def can_be_valid(op, allowed_ops = [add, mul]):

    gaps = len(op.inputs) - 1

    # get possible combinations of operations to fill the gaps
    possible = product(allowed_ops, repeat=gaps)

    for p in possible:
        # apply the operations to the inputs reducing the inputs to a single value
        accum = op.inputs[0]
        for i, f in enumerate(p):
            accum = f(accum, op.inputs[i+1])
            if accum > op.result:
                break
        if accum == op.result:
            #print(op.inputs, p, op.result)
            return True

    return False


@dataclass
class Operation:
    result: int
    inputs: List[int]

@log_time
def part1(ops):
    return sum(op.result for op in ops if can_be_valid(op))

def concat(a, b):
    return int(f"{a}{b}")

@log_time
def part2(ops):
    return sum(op.result for op in ops if can_be_valid(op, allowed_ops=[add, mul, concat]))


@log_time
def parse_input(lines):
    ops = []
    for line in lines.split("\n"):
        parts = line.split(": ")
        result = int(parts[0])
        inputs = list(map(int, parts[1].split(" ")))
        ops.append(Operation(result, inputs))

    return ops



lines = open("day07/input.txt", encoding="utf8").read()

ops = parse_input(lines)

print("Part 1: ", part1(ops))
print("Part 2: ", part2(ops))
