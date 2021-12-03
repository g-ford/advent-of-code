from operator import ge, lt


def parse_line(l):
    return list(map(int, l.strip()))


def to_dec(l):
    return int("".join(map(str, l)), 2)


input = list(map(parse_line, open('input.txt').readlines()))

transpose = list(zip(*input))
mid = len(input) // 2

gamma = [int(sum(c) > mid) for c in transpose]
epsilon = [abs(x - 1) for x in gamma]


print("Part A: ", to_dec(gamma) * to_dec(epsilon))


def filter_rating(ratings, op, index=0):
    if len(ratings) == 1:
        return ratings[0]

    mid = len(ratings) / 2
    transpose = list(zip(*ratings))[index]
    bit = int(op(sum(transpose), mid))

    filtered = [x for x in ratings if x[index] == bit]
    return filter_rating(filtered, op, index + 1)


o2_filtered = filter_rating(input, ge)
co2_filtered = filter_rating(input, lt)

print("Part B:", to_dec(o2_filtered) * to_dec(co2_filtered))
