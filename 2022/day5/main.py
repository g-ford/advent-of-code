from collections import deque
from itertools import groupby
from copy import deepcopy


def transpose(l_2d):
    return [list(x) for x in zip(*l_2d)]


def convert_to_stacks(init):
    def col_to_stack(col):
        return [x for x in col if x.strip()]

    def pad_rows(rows):
        N = max([len(c) for c in rows])
        x = [r.ljust(N) for r in rows[:-1]]
        return reversed(x)

    stacks = []
    for col in transpose(pad_rows(init)):
        if any(c.isalpha() for c in col):
            stacks.append(col_to_stack(col))

    return stacks


def move(stacks, instruction):
    parts = instruction.split(' ')
    amount = int(parts[1])
    source = int(parts[3]) - 1
    dest = int(parts[5]) - 1

    for _ in range(amount):
        stacks[dest].append(stacks[source].pop())

def move2(stacks, instruction):
    parts = instruction.split(' ')
    amount = int(parts[1]) * -1
    source = int(parts[3]) - 1
    dest = int(parts[5]) - 1

    stacks[dest] += stacks[source][amount:]
    stacks[source] = stacks[source][:amount]


def day5(initial_stack, moves):
    stacks = convert_to_stacks(initial_stack)
    stacks2 = deepcopy(stacks)

    for m in moves:
        move(stacks, m)

    tops = [s[-1] for s in stacks]
    print("Part 1:", "".join(tops))

    for m in moves:
        move2(stacks2, m)

    tops = [s[-1] for s in stacks2]
    print("Part 2:", "".join(tops))


if __name__ == "__main__":

    def clean(value):
        return value.replace("\n", "")

    input = list(map(clean, open("day5/input.txt").readlines()))
    initial_stack, moves = [list(group) for key, group in groupby(input, key=bool) if key]

    day5(initial_stack, moves)
