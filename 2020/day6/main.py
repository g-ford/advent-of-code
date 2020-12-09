from collections import Counter

groups = open('input.txt').read().split("\n\n")

print("Part 1:", sum(len(Counter(g.replace("\n", "").strip())) for g in groups))

sum = 0
for g in groups:
    people = len(g.split())
    ans = Counter(g.replace("\n", "").strip()).items()
    sum += len([1 for c in ans if c[1] == people])

print("Part 2:", sum)
