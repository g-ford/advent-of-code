from utils import log_time
input = list(map(int, open('day1/input.txt').readlines()))


def slide(seq, window):
    for i in range(len(seq) - window + 1):
        yield seq[i: i + window]


@log_time
def part_a():
    partA = 0
    for i in range(1, len(input)):
        if input[i] > input[i-1]:
            partA = partA + 1
    return partA


@log_time
def part_b():
    sums = [sum(x) for x in slide(input, 3)]
    partB = 0
    for i in range(1, len(sums)):
        if sums[i] > sums[i-1]:
            partB = partB + 1

    return partB


result_a = part_a()
result_b = part_b()
print("Part A:", result_a)
print("Part B:", result_b)
