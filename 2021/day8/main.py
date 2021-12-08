from functools import cache
from typing import Counter
from utils import log_time
from pprint import pprint
from itertools import permutations


def parse_row(row):
    parts = row.split('|')
    return tuple(p.split() for p in parts)


@log_time
def part_a(input):
    all_1478 = [n for a, b in input for n in b if len(n) in [2, 4, 3, 7]]
    return len(all_1478)


@log_time
def part_b(input):
    sum = 0
    for patterns, output in input:
        a = ''
        b = ''
        c = ''
        d = ''
        e = ''
        f = ''
        g = ''

        # Frequecy of segements
        # 1 = [    c     f  ]
        # 0 = [a b c   e f g]
        # 2 = [a   c d e   g]
        # 3 = [a   c d   f g]
        # 5 = [a b   d   f g]
        # 4 = [  b c d   f  ]
        # 6 = [a b   d e f g]
        # 7 = [a   c     f  ]
        # 8 = [a b c d e f g]
        # 9 = [a b c d   f g]
        #      8 6 8 7 4 9 7

        # 1 - 7 = a
        one = [set(list(p)) for p in patterns if len(p) == 2][0]
        seven = [set(list(p)) for p in patterns if len(p) == 3][0]
        four = [set(list(p)) for p in patterns if len(p) == 4][0]
        a = (seven - one).pop()

        frequencies = Counter([s for p in patterns for s in list(p)])
        for s, v in frequencies.items():
            if v == 8 and s != a:
                c = s
            if v == 6:
                b = s
            if v == 4:
                e = s
            if v == 9:
                f = s
            if v == 7:
                if s in four:
                    d = s
                else:
                    g = s

        mapping = {
            "0": next(p for p in patterns if set(list(p)) == set([a, b, c, e, f, g])),
            "1": next(p for p in patterns if len(p) == 2),
            "2": next(p for p in patterns if set(list(p)) == set([a, c, d, e, g])),
            "3": next(p for p in patterns if set(list(p)) == set([a, c, d, f, g])),
            "4": next(p for p in patterns if len(p) == 4),
            "5": next(p for p in patterns if set(list(p)) == set([a, b, d, f, g])),
            "6": next(p for p in patterns if set(list(p)) == set([a, b, d, e, f, g])),
            "7": next(p for p in patterns if len(p) == 3),
            "8": next(p for p in patterns if len(p) == 7),
            "9": next(p for p in patterns if set(list(p)) == set([a, b, c, d, f, g]))
        }

        def sorted_str(s):
            return "".join(sorted(list(s)))

        inv_map = {sorted_str(v): k for k, v in mapping.items()}
        sum += int("".join([inv_map[sorted_str(x)] for x in output]))
    return sum


@log_time
def part_b_bruteforce(input):
    summed = 0
    normal_numbers = {
        "abcefg": "0", "cf": "1", "acdeg": "2", "acdfg": "3", "bcdf": "4",
        "abdfg": "5", "abdefg": "6", "acf": "7", "abcdefg": "8", "abcdfg": "9"}

    # get all possible variations of 8
    # and use that to make tranlation tables
    trans_tables = [str.maketrans("abcdefg", "".join(perm))
                    for perm in permutations("abcdefg")]

    for patterns, output in input:
        for trans in trans_tables:
            translated = ["".join(sorted(n.translate(trans)))
                          for n in patterns]
            if all(t in normal_numbers for t in translated):
                computed = ["".join(sorted(o.translate(trans)))
                            for o in output]
                summed += int("".join(normal_numbers[x] for x in computed))
                break  # roughly halves run time :)
    return summed


input = list(map(parse_row, open('day8/input.txt').readlines()))

result_a = part_a(input)
result_b = part_b(input)
result_b2 = part_b_bruteforce(input)
print("Part A:", result_a)
print("Part B:", result_b)
print("Part B2:", result_b2)
