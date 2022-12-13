def count(t, r, step, i):
    """
    Count the number of 'scenic' trees near tree `t`

    `r` is the set of trees to compare - either a row or column
    `step` is the direction to search and should 1 or -1
    `i` is the position of the x|y that we are looking for

    Interestingly, apparently elves can see over trees but can't look up
    If a tree is blocked by a larger tree that it still smaller than `t` then
    we can still see it. e.g `t` being a tree of height 5 and `r` a set
    of 4341 would count as 4
    """
    if step < 0:
        over = list(reversed(r[:t[i]]))
    else:
        over = r[t[i]+1:len(r)]

    count = 0
    for s in over:
        if s[2] >= t[2]:
            return count + 1
        count += 1
    return count


def countRow(t, r, step):
    return count(t, r, step, 1)


def countCol(t, r, step):
    return count(t, r, step, 0)


def day8(input):
    visible = set()
    all_trees = set()
    max_y = len(input)
    max_x = len(input[0])

    for x in range(max_x):
        for y in range(max_y):
            # on first pass we know that trees on the edge are visible
            if x == 0 or y == 0 or x == max_x - 1 or y == max_y - 1 :
                visible.add((x, y, input[x][y]))
            all_trees.add((x, y, input[x][y]))

    # We do part 2 first as we don't care about trees on the edge
    # and we have that set now before we start adding other visible
    # trees to it
    scores = []
    for tree in sorted(all_trees - visible):
        row = sorted([t for t in all_trees if t[0] == tree[0]])
        col = sorted([t for t in all_trees if t[1] == tree[1]])

        r = countRow(tree, row, 1)
        l = countRow(tree, row, -1)
        u = countCol(tree, col, -1)
        d = countCol(tree, col, 1)

        scores.append(r * l * u * d)
    print("Part2: ", f"Max scenic: {max(scores)}")

    for tree in sorted(all_trees):
        if tree not in visible:
            row = [t for t in all_trees if t[1] == tree[1]]
            col = [t for t in all_trees if t[0] == tree[0]]
            # North
            if all([t[2] < tree[2] for t in row if t[0] < tree[0]]):
                visible.add(tree)
                continue

            # south
            if all([t[2] < tree[2] for t in row if t[0] > tree[0]]):
                visible.add(tree)
                continue

            # east
            if all([t[2] < tree[2] for t in col if t[1] < tree[1]]):
                visible.add(tree)
                continue

            # west
            if all([t[2] < tree[2] for t in col if t[1] > tree[1]]):
                visible.add(tree)
                continue

    print("Part1: ", f"Visible: {len(visible)}")


if __name__ == "__main__":

    def clean(value):
        return list(map(int, (x for x in value.strip())))

    input = list(map(clean, open("day8/input.txt").readlines()))
    day8(input)
