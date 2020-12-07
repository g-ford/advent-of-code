
def parseTreeLine(line):
    line = line.strip()  # need to get rid of new line *sigh
    return [0 if x == '.' else 1 for x in line]


tree_map = list(map(parseTreeLine, open('input.txt').readlines()))


def treesInSlope(tree_map, slope=3, step=1):
    trees = 0
    row_len = len(tree_map[0])
    for i, row in enumerate(tree_map):
        if step == 1 or i % step == 0:
            r_i = (slope*i//step) % row_len
            trees += row[r_i]
    return trees


print("Part 1:", treesInSlope(tree_map))

s1 = treesInSlope(tree_map, 1)
s3 = treesInSlope(tree_map, 3)
s5 = treesInSlope(tree_map, 5)
s7 = treesInSlope(tree_map, 7)
s1_2 = treesInSlope(tree_map, 1, 2)

print("Part 2:", s1, s3,  s5,  s7,  s1_2)
print("Part 2:", s1 * s3 * s5 * s7 * s1_2)
