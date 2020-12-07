from itertools import permutations
from  math import prod

input = list(map(int, open('input.txt').readlines()))

perms = permutations(input, 2);

sums = ((a + b, (a, b)) for (a, b) in perms)
for s in sums:
    if s[0] == 2020:
        print("Part 1:", prod(s[1]))
        break


perms3 = permutations(input, 3);

sums3 = ((a + b + c, (a, b, c)) for (a, b, c) in perms3)
for s in sums3:
    if s[0] == 2020:
        print("Part 2:", prod(s[1]))
        break