import numpy as np

def day9(input):
    knots = [(0,0) for _ in range(10)]
    visited = [set() for _ in range(10)]

    delta = {
        'R': (1,0),
        'L': (-1,0),
        'U': (0,1),
        'D': (0,-1),
    }

    tail_move = {
        (0,0): (0, 0),  # underneath

        (1,0): (0, 0),  # Heading right
        (2,0): (1, 0),

        (-1,0): (0, 0),  # Heading left
        (-2,0): (-1, 0),

        (0,1): (0, 0),  # Heading up
        (0,2): (0, 1),

        (0,-1): (0, 0),  # Heading down
        (0,-2): (0, -1),

        (1,1): (0, 0), # Heading diagnal up right
        (1,2): (1, 1),
        (2,1): (1, 1),
        (2,2): (1, 1),

        (-1,1): (0, 0), # Heading diagnal up left
        (-1,2): (-1, 1),
        (-2,1): (-1, 1),
        (-2,2): (-1, 1),

        (1,-1): (0, 0), # Heading diagnal down right
        (1,-2): (1, -1),
        (2,-1): (1, -1),
        (2,-2): (1, -1),

        (-1,-1): (0, 0), # Heading diagnal down left
        (-1,-2): (-1, -1),
        (-2,-1): (-1, -1),
        (-2,-2): (-1, -1),
    }

    for dir, step in input:
        for _ in range(step):
            # first move the head
            knots[0] = tuple(np.add(knots[0], delta[dir]))
            visited[0].add(knots[0])

            # then drag the tail around
            for i, knot in enumerate(knots[1:]):
                diff = tuple(np.subtract(knots[i], knots[i+1]))
                n = tuple(np.add(knots[i+1], tail_move[diff]))
                knots[i+1] = n
                visited[i+1].add(n)

    print(f"Part 1: Tail visited: {len(visited[1])} (13, 6026)")
    print(f"Part 1: Tail visited: {len(visited[-1])} (36, ??)")


if __name__ == "__main__":

    def clean(value):
        return value[0], int(value.strip()[2:])

    input = list(map(clean, open("day9/input.txt").readlines()))
    day9(input)
