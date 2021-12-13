from collections import defaultdict
from utils import log_time
from dataclasses import dataclass


def can_visit_a(n, path):
    if n.isupper():
        return True
    else:
        return n not in path


def can_visit_b(n, path):
    if n.isupper():
        return True
    else:
        if n not in path:
            return True

        elif n not in ['start', 'finish']:
            small = [x for x in path if x.islower() and x not in [
                'start', 'end']]

            return len(small) == len(set(small))
        return False


def find_paths(nodes, start, end, can_visit, path=[]):
    path = path + [start]
    if start == end:
        return [path]

    paths = []
    for n in nodes[start]:
        if can_visit(n, path):
            newpaths = find_paths(nodes, n, end, can_visit, path)
            paths += newpaths
    return paths


@ log_time
def part_a(nodes):
    paths = find_paths(nodes, 'start', 'end', can_visit_a)
    return paths


@ log_time
def part_b(nodes):
    paths = find_paths(nodes, 'start', 'end', can_visit_b)
    return paths


input = list(open('day12/input.txt').readlines())
nodes = defaultdict(set)
for l in input:
    a, b = l.strip().split('-')
    nodes[a].add(b)
    nodes[b].add(a)

result_a = part_a(nodes)
result_b = part_b(nodes)
print("Part A:", len(result_a))
print("Part B:", len(result_b))
