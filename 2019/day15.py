from intcode import IntCodeComputer, InputInterrupt, OutputInterrupt
from operator import add
import networkx
from copy import deepcopy
import os

direction_movement = {1: (0, 1),    # Norh
                      4: (1, 0),    # East
                      2: (0, -1),   # South
                      3: (-1, 0)}   # West

tiles_icons = {0: '█', 1: ' ', 2: '●', 4: '○'}


def add_tuples(p, v):
    return tuple(map(add, p, v))


def draw(ship_map, path, frontier=[]):
    k = ship_map.keys()
    xs = [kx[0] for kx in k]
    ys = [ky[1] for ky in k]

    x_min = min(xs)
    x_max = max(xs)
    y_min = min(ys)
    y_max = max(ys)
    ship_map[0, 0] = 4

    os.system('clear')
    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            p = ship_map.get((x, y), 0)
            if (x, y) in frontier:
                o = '*'
            elif p != 2 and p != 4 and (x, y) in path:
                o = '.'
            else:
                o = tiles_icons[p]
            print(o, end='')
        print('')


def build_graph(smap, target):
    graph = networkx.Graph()
    graph.add_node((0, 0))

    walkable = [x for x in smap if smap[x] > 0]
    for a in walkable:
        for b in direction_movement.values():
            new_pos = add_tuples(a, b)
            if new_pos in walkable:
                graph.add_edge(a, new_pos)
    return graph


def flood_oxygen(ship, start):
    floodable = {x: 1 for x in ship if ship[x] > 0}
    minutes = -1  # because oxygen is already at the o2 tank
    flooded = {target: 1}
    frontier = [target]

    while frontier:
        new_frontier = []
        for a in frontier:
            flooded[a] = 1
            for b in direction_movement.values():
                z = add_tuples(a, b)
                if z in floodable and z not in flooded:
                    new_frontier.append(z)
        minutes += 1
        #draw(floodable, flooded, new_frontier)
        frontier = new_frontier
    return minutes


if __name__ == "__main__":
    program = list(map(int, open('inputs/day15.txt').read().split(',')))

    c = IntCodeComputer(program)

    ship_map = {}
    ship_map[0, 0] = 4
    frontier = []
    target = None

    # Initial frontier is all directions from origin.
    # Clone the entire IntCodeComputer at each step so that when
    # we return to it, it will continue from the previous state
    for direction in direction_movement:
        frontier.append((
            (0, 0),
            direction,
            deepcopy(c)))

    while len(frontier):
        # oddly pop(0) seems to be slightly faster in practice
        # and definately cooler when visualising
        position, direction, c = frontier.pop(0)

        try:
            c.inputs.append(direction)
            c.run()
        except OutputInterrupt:
            reply = c.outputs[-1]
            test_position = add_tuples(position, direction_movement[direction])
            ship_map[test_position] = reply

            # visualise the search by uncommenting this
            # draw(ship_map, [])

            if reply == 1:
                # found an open space so add all directions from the new space to the frontier
                for d in direction_movement:
                    p = add_tuples(test_position, direction_movement[d])
                    if p not in ship_map:
                        frontier.append((test_position, d, deepcopy(c)))

            if reply == 2:
                target = test_position

    graph = build_graph(ship_map, target)
    shortest = networkx.shortest_path(graph, (0, 0), target)
    flood = networkx.eccentricity(graph, v=target)

    # draw(ship_map, shortest)

    print(f"Shortest path to oxygen is {len(shortest) - 1} commands")
    print(f"Oxygen is flooded in {flood} minutes")
    print(f"My flood took {flood_oxygen(ship_map, target)} minutes")
