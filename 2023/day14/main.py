# ❯ python -m day14.main
# [PERF] parse_input 0.012875 ms
# [PERF] part1 1.069784 ms
# Part 1:  109424
# We have a cycle at index 109 last seen at 100
# Jumping to 1000000000
# [PERF] part2 331.737757 ms
# Part 2:  102509

from typing import Sequence
from utils import log_time, rotate90, transpose
from rich import print


def roll_column(col):
    """ Roll the column north(ish)"""

    # Convert to list so we can roll them
    col = [c for c in col]

    # For each rock (O) move it as far left as possible until it hits a non-empty space ()
    # print("Before roll", col)
    for i in range(1, len(col)):
       if col[i] == "O":
            j = i - 1
            while j >= 0 and col[j] == ".":
                j -= 1
            col[i] = "."
            col[j+1] = "O"
    # print("After roll", col)
    return col

def tilt (parts) -> Sequence[Sequence[str]]:
    # We transpose from rows to cols, roll the cols, then transpose it back
    return transpose([roll_column(c) for c in transpose(parts)])


def calc_weight(parts):
    """ Calculate the weight of a column """
    # Weight is the sum of the index + 1 of each rock (O) in the column
    # so we have to transpose from rows to cols first
    # When calculateing the weight, we reverse the column so the index is it's weight
    cols = transpose(parts)
    return sum(sum(i + 1  for i, c in enumerate(reversed(col)) if c == "O") for col in cols)


def cycle(parts):
    """ Cycle the parts """

    # roll north, west, south, east, which is convienently the way transpose goes :)
    # print("Before cycle", parts)
    for _ in range(4):
        parts = rotate90(tilt(parts))

    # print("After cycle", parts)
    return parts



@log_time
def part1(parts):
    """ Calculate the load when rolling everything north """
    return calc_weight(tilt(parts))


@log_time
def part2(parts):
    CYCLES = 1000000000
    """ Calculate the load after 1000000000 cycles"""
    states = []
    found_cycle = None
    i = 0
    final_state = None
    while i <= CYCLES:
        parts = cycle(parts)
        if parts in states and not found_cycle:
            print(f"We have a cycle at index {i} last seen at {states.index(parts)}")

            # now we know the cycle length, and where we are in the cycle, we need to find the state at 1000000000
            remainder = CYCLES - i
            cycle_length = i - states.index(parts)
            num_loops = remainder // cycle_length

            # jump to almost the end
            i = i + (num_loops * cycle_length)
            print("Jumping to", i)

            # and now we proceed to the end of the max iterations from here
            found_cycle = True
        states.append(parts)
        i += 1

    return calc_weight(states[-2]) # 🤷‍♂️

@log_time
def parse_input(lines):
    return [l.strip() for l in lines.split("\n")]


lines = open("day14/input.txt", encoding="utf8").read()

parts = parse_input(lines)

print("Part 1: ", part1(parts))
print("Part 2: ", part2(parts))
