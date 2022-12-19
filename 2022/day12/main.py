import networkx as nx
import numpy as np

START = ord('S')
END = ord('E')
START_REPLACE = ord('a') - 1
END_REPLACE = ord('z') + 1


def tuple_add(t1, t2):
    return tuple(np.add(t1, t2))


def get_neighbours(node):
    neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    return [tuple_add(node, n) for n in neighbours]


def grid_to_graph(grid):
    g = nx.DiGraph()
    start_node = end_node = None

    # convert the grid to a cell list for ease of traversal
    cells = [tuple(x) for x in np.transpose(grid.nonzero())]

    for cell in cells:
        v = grid[cell]

        # special case start and end node
        # eyballed that the END will follow a Z
        if v == START:
            print("Replaceing start")
            v = START_REPLACE
            start_node = cell
            grid[cell] = v

        if v == END:
            print("Replacing end")
            v = END_REPLACE
            end_node = cell
            grid[cell] = v

        for n in get_neighbours(cell):
            if n in cells:
                test = grid[n]
                if abs(test - v) <= 1:
                    # print("Adding", node, n)
                    g.add_edge(cell, n)

    return g, start_node, end_node


def day12(graph, grid):
    g, start, end = graph
    print(g)
    print(start, end)
    path = nx.shortest_path_length(g, start, end)
    print("Part 1: ", path)
    print("Part 2: ")


if __name__ == "__main__":

    def clean(value):
        return [ord(x) for x in value.strip()]

    grid = np.array(list(map(clean, open("day12/input.txt").readlines())))
    graph = grid_to_graph(grid)

    day12(graph, grid)
