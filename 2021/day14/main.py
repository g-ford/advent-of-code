from collections import defaultdict
from typing import Counter
from utils import log_time, slide


def parse_line(l):
    return tuple(l.strip().split(' -> '))


def count_polymers(t, ins, rounds):
    current = t
    for _ in range(rounds):
        new_t = [current[0]]
        for a, b in slide(current, 2):
            c = ins[f"{a}{b}"]
            new_t += [c, b]
        current = new_t
    return Counter(current)


def count_polymers_faster(t, ins, rounds):
    pairs = defaultdict(int)
    for p in slide(t, 2):
        pairs[p] += 1

    for _ in range(rounds):
        next_pairs = defaultdict(int)
        for a, b in list(pairs.keys()):
            c = ins[f"{a}{b}"]
            next_pairs[f"{a}{c}"] += pairs[f"{a}{b}"]
            next_pairs[f"{c}{b}"] += pairs[f"{a}{b}"]
        pairs = next_pairs

    singles = defaultdict(int)
    singles[t[0]] += 1
    for k, v in pairs.items():
        singles[k[1]] += v

    return singles


@ log_time
def part_a(template, rules, method=count_polymers):
    c = method(template, rules, rounds=10)

    least = c[min(c, key=c.get)]
    most = c[max(c, key=c.get)]
    return most - least


@ log_time
def part_b(template, rules):
    c = count_polymers_faster(template, rules, rounds=40)

    least = c[min(c, key=c.get)]
    most = c[max(c, key=c.get)]
    return most - least


input = list(open('day14/input.txt').readlines())
template = input[0].strip()
rules = dict(map(parse_line, input[2:]))

result_a = part_a(template, rules)
result_a2 = part_a(template, rules, count_polymers_faster)
result_b = part_b(template, rules)
print("Part A:", result_a)
print("Part A2:", result_a2)
print("Part B:", result_b)
