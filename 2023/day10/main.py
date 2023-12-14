# ❯ python -m day10.main
# [PERF] parse_input 2.204180 ms
# [PERF] part1 58.413982 ms
# Part 1:  6682
# [PERF] part1 56.318998 ms
# [PERF] part2 57.867050 ms
# Part 2:  353

import networkx as nx
from utils import compass_neighbours, log_time


def is_connected(node, nodes, coord, neighbour):
    try:
        if node == '.' or nodes[neighbour] == '.':
            return False

        if node == '|':
            if neighbour[0] - coord[0] == 1:
                # Heading south
                if nodes[neighbour] in "|LJS":
                    return True
            elif neighbour[0] - coord[0] == -1:
                # Heading north
                if nodes[neighbour] in "|F7S":
                    return True
            return False

        if node == '-':
            if neighbour[1] - coord[1] == 1:
                # Heading east
                if nodes[neighbour] in "-7JS":
                    return True
            elif neighbour[1] - coord[1] == -1:
                # Heading west
                if nodes[neighbour] in "-FSL":
                    return True
            return False

        if node == 'L':
            if neighbour[0] - coord[0] == -1:
                # Heading north
                if nodes[neighbour] in "|7FS":
                    return True
            elif neighbour[1] - coord[1] == 1:
                # Heading east
                if nodes[neighbour] in "-J7S":
                    return True
            return False

        if node == 'J':
            if neighbour[0] - coord[0] == -1:
                # Heading north
                if nodes[neighbour] in "|7FS":
                    return True
            elif neighbour[1] - coord[1] == -1:
                # Heading west
                if nodes[neighbour] in "-FSL":
                    return True
            return False

        if node == '7':
            if neighbour[0] - coord[0] == 1:
                # Heading south
                if nodes[neighbour] in "|LJS":
                    return True
            elif neighbour[1] - coord[1] == -1:
                # Heading west
                if nodes[neighbour] in "-FLS":
                    return True
            return False

        if node == 'F':
            if neighbour[0] - coord[0] == 1:
                # Heading south
                if nodes[neighbour] in "|LJS":
                    return True
            elif neighbour[1] - coord[1] == 1:
                # Heading east
                if nodes[neighbour] in "-J7S":
                    return True
            return False

        # Probably not needed as we should get the edges from the other nodes
        if node == 'S':
            if neighbour[0] - coord[0] == 1:
                # Heading south
                if nodes[neighbour] in "|LJ":
                    return True
            elif neighbour[0] - coord[0] == -1:
                # Heading north
                if nodes[neighbour] in "|F7":
                    return True
            elif neighbour[1] - coord[1] == 1:
                # Heading east
                if nodes[neighbour] in "-J7":
                    return True
            elif neighbour[1] - coord[1] == -1:
                # Heading west
                if nodes[neighbour] in "-FL":
                    return True
            return False

        return False
    except KeyError:
        return False

    raise ValueError('Huh')

@log_time
def part1(parts):
    nodes, start = parts

    g = nx.Graph()
    for coord, node in nodes.items():
        for neighbour in compass_neighbours(*coord):
            if is_connected(node, nodes, coord, neighbour):
                g.add_edge(coord, neighbour)

    loop = sorted(nx.cycle_basis(g, start), key=len)

    # The furhest length will be halfway around, or half the nodes in the loop
    return len(loop[-1]) // 2, loop[-1]

@log_time
def part2(parts):
    # https://en.wikipedia.org/wiki/Pick%27s_theorem
    # Picks theorm says area = i + b/2 - 1 where i is the number of internal points and b is the number of
    # boundary points so i = area - b/2 + 1
    # the boundary points are the number of nodes in the loop from part 1
    # to find the area we use the shoelace formula
    # A = 1/2 * sum(x_i * y_i+1 - x_i+1 * y_i)
    # https://en.wikipedia.org/wiki/Shoelace_formula

    b, loops = part1(parts)


    area = 0
    loops.append(loops[0]) # allow the last point to wrap around
    for i in range(len(loops) - 1):
        area += loops[i][0] * loops[i + 1][1] - loops[i + 1][0] * loops[i][1]

    return abs(area) // 2 - b + 1

@log_time
def parse_input(lines):
    nodes = {}
    start = None
    for r, row in enumerate(lines):
        for c, col in enumerate(row):
            nodes[(r, c)] = col
            if col == "S":
                start = (r, c)

    return nodes, start


lines = open("day10/input.txt", encoding="utf8").readlines()

parts = parse_input(lines)

print("Part 1: ", part1(parts)[0])
print("Part 2: ", part2(parts))
