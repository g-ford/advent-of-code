from collections import defaultdict
from utils import log_time

def print_grid(cells, size, travelled, position):
    print ("-" * size[1])
    for i in range(size[0]):
        for j in range(size[1]):
            if (i, j) in cells:
                print("#", end="")
            elif (i, j) in travelled:
                print("X", end="")
            elif (i, j) == (position[0], position[1]):
                print(position[2], end="")
            else:
                print(".", end="")
        print()
    print ("-" * size[1])

@log_time
def part1(parts):
    cells, position, size = parts

    _, _, travelled = test_for_loop(cells, position, size)
    #print_grid(cells, size, travelled, position)

    # There is still an off by one error here
    # if we run off the right or bottom it is too many
    # if we run off the left or top it is too few
    return len(list(travelled))


def test_for_loop(cells, position, size):
    # create an obstruction map for each row and coll
    obs_by_row = defaultdict(list)
    obs_by_col = defaultdict(list)
    for c in cells:
        obs_by_row[c[0]].append(c[1])
        obs_by_col[c[1]].append(c[0])


    # keep track of the turns. If we hit a turn twice we are in a loop
    path = []
    travelled = set()
    while 0 <= position[0] < size[0] and 0 <= position[1] < size[1]:
    #for _ in range(20):
        path.append(position)

        if position[2] == "^":
            blockade = max((x for x in obs_by_col[position[1]] if x < position[0]), default=-2)
            travelled.update((x, position[1]) for x in range(max(blockade + 1, 0), position[0]))
            position = (blockade + 1, position[1], ">")
        elif position[2] == ">":
            blockade = min((x for x in obs_by_row[position[0]] if x > position[1]), default=size[0]+1)
            travelled.update(set((position[0], x) for x in range(position[1] + 1, min(blockade, size[0]))))
            position = (position[0], blockade - 1, "v")
        elif position[2] == "v":
            blockade = min((x for x in obs_by_col[position[1]] if x > position[0]), default=size[1]+1)
            travelled.update(set((x, position[1]) for x in range(position[0] + 1, min(blockade, size[1]))))
            position = (blockade - 1, position[1], "<")
        elif position[2] == "<":
            blockade = max((x for x in obs_by_row[position[0]] if x < position[1]), default=-2)
            travelled.update(set((position[0], x) for x in range(max(blockade + 1, 0), position[1])))
            position = (position[0], blockade + 1, "^")
        if position in path:
            return True, path, travelled

    return False, path, travelled

@log_time
def part2(parts):
    cells, position, size = parts

    # recalculate the path from part1
    _, _, travelled = test_for_loop(cells, position, size)

    # brute force by checking putting a blockade on each point on the path travelled
    tests = (test_for_loop(cells[:] + [(p[0], p[1])], position, size) for p in set(travelled))
    loops = sum(1 for l, _, _ in tests if l)

    return loops


@log_time
def parse_input(lines):
    cells = []
    poistion = None
    size = (len(lines.split("\n")), len(lines.split("\n")[0]))
    for i, line in enumerate(lines.split("\n")):
        for j, cell in enumerate(line):
            if cell == "#":
                cells.append((i, j))
            elif cell in ["^", ">", "v", "<"]:
                poistion = (i, j, cell)
    return cells, poistion, size


lines = open("day06/input.txt", encoding="utf8").read()
parts = parse_input(lines)

print("Part 1: ", part1(parts))
print("Part 2: ", part2(parts))
