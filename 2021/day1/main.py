input = list(map(int, open('input.txt').readlines()))

partA = 0
for i in range(1, len(input)):
    if input[i] > input[i-1]:
        partA = partA + 1

print("Part A:", partA)


def slide(seq, window):
    for i in range(len(seq) - window + 1):
        yield seq[i: i + window]


sums = [sum(x) for x in slide(input, 3)]
partB = 0
for i in range(1, len(sums)):
    if sums[i] > sums[i-1]:
        partB = partB + 1

print("Part B:", partB)
