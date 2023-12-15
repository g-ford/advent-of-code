
# ❯ python -m day12.main
# [PERF] parse_input 0.047207 ms
# [PERF] part1 6482.438803 ms
# Part 1:  7221
# [PERF] part2 244.058847 ms
# Part 2:  7139671893722
# [PERF] part1_faster 1.427889 ms
# Part 1 (b):  7221

import functools
import re
from itertools import product

from utils import log_time


def is_valid(spring, groups):
    spring_groups = list(map(len, re.findall(r"#+", spring)))
    return spring_groups == groups


def count_valid(spring, groups):
    chars = ['.', '#']  # Possible replacements for '?'
    replacements = [chars if c == '?' else [c] for c in spring]
    combinations = [''.join(combination) for combination in product(*replacements)]
    return sum(is_valid(c, groups) for c in combinations)


@functools.cache
def count_valid_faster(spring, groups):
    """Use a dynamic programming approach to test each group against the remaining
    spring until we fail or succeed.

    Use a cache to store the results of each combination of spring and groups for
    faster lookups"""

    def calc_hash():
        # Check if the next `group` of characters can all be #s
        sub = spring[:groups[0]].replace('?', '#')

        if sub != '#' * groups[0]:
            # This spring is not big enough to hold the group
            return 0

        # If this is the end of the spring, and this is the last group,
        # we have a valid combination
        if len(spring) == groups[0]:
            if len(groups) == 1:
                return 1
            else:
                return 0

        # Check if the char after the group is a . or ? that can seperate the groups
        if spring[groups[0]] in '.?':
            return count_valid_faster(spring[groups[0]+1:], groups[1:])

        return 0

    def calc_dot():
        # skip this and move on
        return count_valid_faster(spring[1:], groups)

    # First some base case sanity checks
    # If there are no groups left, we can only have dots left in spring
    # (or ? that we assume will be .)
    if not groups:
        if '#' not in spring:
            return 1
        else:
            return 0
    # if there are still groups but no spring left we can't have a valid combination
    if not spring:
        return 0

    next_spring = spring[0]

    if next_spring == '#':
         return calc_hash()

    elif next_spring == '.':
         return calc_dot()

    elif next_spring == '?':
        return calc_hash() + calc_dot()




@log_time
def part1(parts):
    """Brute force all possible combinations of ? and count how many are valid"""
    total = 0
    for p in parts:
        springs, groups = p.strip().split(' ')
        groups = list(map(int, re.findall(r"\d+", groups)))
        total += count_valid(springs, groups)
    return total

@log_time
def part1_faster(parts):
    total = 0
    for p in parts:
        springs, groups = p.strip().split(' ')
        groups = list(map(int, re.findall(r"\d+", groups)))
        total += count_valid_faster(springs, tuple(groups))
    return total

def expand_springs(spring):
    return ((spring + '?') * 5)[0:-1] # remove the last ?

def expand_groups(groups):
    return tuple(groups * 5)


@log_time
def part2(parts):
    """
    This is the same as part 1, but with 5x the input
    """

    total = 0
    for p in parts:
        spring, group = p.strip().split(' ')
        group = list(map(int, re.findall(r"\d+", group)))
        total += count_valid_faster(expand_springs(spring), expand_groups(group))

    return total

@log_time
def parse_input(lines):
    lines = [line.strip() for line in lines]

    return lines


lines = open("day12/input.txt", encoding="utf8").readlines()

parts = parse_input(lines)

print("Part 1: ", part1(parts))
print("Part 2: ", part2(parts))
print("Part 1 (b): ", part1_faster(parts))
