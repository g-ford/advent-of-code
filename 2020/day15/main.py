from collections import defaultdict


def play(starting, iterations=2020):
    heard = defaultdict(list)
    for i, n in enumerate(starting):
        heard[n].append(i)

    last = starting[-1]
    for i in range(len(starting), iterations):
        if len(heard[last]) == 1:
            last = 0
        else:
            last = heard[last][-1] - heard[last][-2]
        heard[last].append(i)
    return last


print("Part 1:", play([14, 8, 16, 0, 1, 17], 2020))
print("Part 2:", play([14, 8, 16, 0, 1, 17], 30000000))
