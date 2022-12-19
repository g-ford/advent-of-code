from copy import deepcopy
from dataclasses import dataclass
from itertools import groupby
import math
from operator import mul, add
from typing import Callable


@dataclass
class Monkey:
    name: str
    items: list[int]
    operation: tuple[Callable, int]
    rule: int
    true: int
    false: int
    inspections: int = 0


def input_to_monkey(lines) -> Monkey:
    ops = {"+": add, "*": mul}  # this is all that seems to be in the input

    name = lines[0][:-1]
    items = list(map(int, lines[1].replace('Starting items: ', '').split(', ')))
    operation_parts = lines[2].replace('Operation: new = old', '').split()
    # special case for `old * old`
    # there doesn't seem to be any other special cases (at least in
    # my input)
    if (operation_parts[1] == 'old'):
        operation = (pow, 2)
    else:
        operation = (ops[operation_parts[0]], int(operation_parts[1]))
    rule = int(lines[3].replace('Test: divisible by ', ''))
    true = int(lines[4].replace('If true: throw to monkey ', ''))
    false = int(lines[5].replace('If false: throw to monkey ', ''))

    return Monkey(name=name, items=items, operation=operation, rule=rule, true=true, false=false)


def parse(input: list[str]) -> list[Monkey]:
    return list(map(input_to_monkey, [list(g) for k, g in groupby(input, key=bool) if k]))


def count_inspections(state: list[Monkey], rounds: int, worry=3) -> list[int]:
    lcm = math.lcm(*(m.rule for m in state))

    for r in range(rounds):
        for m in state:
            for item in m.items:
                m.inspections += 1
                x = (m.operation[0](item, m.operation[1]) // worry)
                if x % m.rule == 0:
                    state[m.true].items.append(x % lcm)
                else:
                    state[m.false].items.append(x % lcm)
            m.items = []

        # print("Round", r)
        # for m in state:
        #     print(m.name, m.items)

    return [m.inspections for m in state]


def day11(initial_state: list[Monkey]):
    initial_state2 = deepcopy(initial_state)
    part1 = count_inspections(initial_state, rounds=20, worry=3)
    print("Part 1: ", mul(*sorted(part1, reverse=True)[:2]))
    part2 = count_inspections(initial_state2, rounds=10000, worry=1)
    print("Part 2: ", mul(*sorted(part2, reverse=True)[:2]))


if __name__ == "__main__":

    def clean(value):
        return value.strip()

    input = list(map(clean, open("day11/input.txt").readlines()))
    initial_state = parse(input)
    day11(initial_state)
