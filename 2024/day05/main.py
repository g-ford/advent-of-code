from itertools import permutations
from utils import log_time
import networkx as nx


def is_valid(p, rules):
    for r in rules:
        try:
            if p.index(r[0]) < p.index(r[1]):
                continue
            else:
                return False
        except ValueError:
            continue # this rule doesn't apply to this print
    return True

@log_time
def part1(parts):
    rules, prints = parts

    valid_prints = set()
    invalid_prints = set()
    for p in prints:
        hashable = tuple(p)

        if is_valid(p, rules):
            valid_prints.add(hashable)
        else:
            invalid_prints.add(hashable)

    return sum(p[(len(list(p))-1)//2] for p in valid_prints)


@log_time
def part2(parts):
    # redo part 1 - it's time efficient enough
    rules, prints = parts

    invalid_prints = set()
    for p in prints:
        hashable = tuple(p)

        if not is_valid(p, rules):
            invalid_prints.add(hashable)


    now_valid = []
    for p in invalid_prints:
        # get only the rules that apply to this print
        potential = set(permutations(p, 2))
        applicable = potential.intersection(rules)

        # now make a graph and sort the nodes
        G = nx.DiGraph(applicable)
        now_valid.append(list(nx.topological_sort(G)))

    return sum(p[(len(p)-1)//2] for p in now_valid)



@log_time
def parse_input(lines):
    rules, prints = lines.split("\n\n")
    rules = set(tuple(map(int, line.split("|"))) for line in rules.split("\n"))
    prints = [list(map(int, line.split(","))) for line in prints.split("\n")]
    return rules, prints

lines = open("day05/input.txt", encoding="utf8").read()

parts = parse_input(lines)

print("Part 1: ", part1(parts))
print("Part 2: ", part2(parts))
