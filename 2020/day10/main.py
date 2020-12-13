from collections import Counter, defaultdict

adaptors = sorted(list(map(int, open("input.txt").readlines())) + [0])
adaptors.append(adaptors[-1] + 3)

diffs = []
for i in range(len(adaptors)-1):
    diffs.append(adaptors[i+1] - adaptors[i])

c = Counter(diffs)
print("Part 1:", (c[1]) * (c[3]), c)

total_jolts = defaultdict(int)
total_jolts[0] = 1  # the wall outlet
for a in adaptors:
    total_jolts[a] += total_jolts[a-1] + total_jolts[a-2] + total_jolts[a-3]


print("Part 2:", total_jolts[adaptors[-1]])
