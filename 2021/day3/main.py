from operator import ge, lt
from utils import log_time, to_dec, transpose


def parse_line(l):
    return list(map(int, l.strip()))


@log_time
def part_a(input):
    transposed = transpose(input)
    mid = len(input) // 2

    gamma = [int(sum(c) > mid) for c in transposed]
    epsilon = [abs(x - 1) for x in gamma]
    return to_dec(gamma) * to_dec(epsilon)


def filter_rating(ratings, op, index=0):
    if len(ratings) == 1:
        return ratings[0]

    mid = len(ratings) / 2
    transpose = list(zip(*ratings))[index]
    bit = int(op(sum(transpose), mid))

    filtered = [x for x in ratings if x[index] == bit]
    return filter_rating(filtered, op, index + 1)


@log_time
def part_b(input):
    o2_filtered = filter_rating(input, ge)
    co2_filtered = filter_rating(input, lt)
    return to_dec(o2_filtered) * to_dec(co2_filtered)


input = list(map(parse_line, open('day3/input.txt').readlines()))

result_a = part_a(input)
result_b = part_b(input)
print("Part A:", result_a)
print("Part B:", result_b)
