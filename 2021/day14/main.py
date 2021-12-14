from collections import defaultdict
from typing import Counter
from utils import log_time, slide


def parse_line(l):
    return tuple(l.strip().split(' -> '))


def count_polymers(t, rules, rounds):
    """ Naive polymer counting

    Creates the full polymer string by inserting characters according to `rules`. Which grows exponentially.

    For the input of 20 chars, 10 rounds, this gives a final string of 20+19+18+.. which is 19457 chars 
    Doing this for 40 rounds gives 20890720927745 chars at 1 byte per char is ~19Tb.
    I think I will need to download some more RAM.
    """
    current = t
    for _ in range(rounds):
        new_t = [current[0]]
        for a, b in slide(current, 2):
            c = rules[f"{a}{b}"]
            new_t += [c, b]
        current = new_t
    return Counter(current)


def count_polymers_faster(t, ins, rounds):
    """A faster way to count polymer chains

    Keeps track of all sliding pairs in the chain, and for each iteration
    updates the count of the two new pairs created.

    Space is considerably more compact in this version but we do not know the 
    final polymer chain ordering.
    """
    pairs = defaultdict(int)
    for p in slide(t, 2):
        pairs[p] += 1

    for _ in range(rounds):
        next_pairs = defaultdict(int)
        for a, b in list(pairs.keys()):
            c = ins[f"{a}{b}"]
            # for each new pair created update the count by the occurences of the old pair
            # i.e 100 ABs, become 100 AC and BC and need to be updated by 100 each
            next_pairs[f"{a}{c}"] += pairs[f"{a}{b}"]
            next_pairs[f"{c}{b}"] += pairs[f"{a}{b}"]
        pairs = next_pairs

    singles = defaultdict(int)
    # because we are only counting the second character of each pair, we add the first
    # character, which will always be the same first char from the template
    singles[t[0]] += 1
    for k, v in pairs.items():
        singles[k[1]] += v

    return singles


@ log_time
def part_a(template, rules, method=count_polymers):
    c = method(template, rules, rounds=10)

    least = min(c.values())
    most = max(c.values())
    return most - least


@ log_time
def part_b(template, rules):
    c = count_polymers_faster(template, rules, rounds=40)

    least = min(c.values())
    most = max(c.values())
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
