from utils import log_time
from queue import PriorityQueue


@log_time
def parse_input(lines):
    return [list(map(int, l.strip())) for l in lines]


def search(start, end, grid):
    """ Uses Dijkstra's algo to search  """
    grid_y = len(input) - 1
    grid_x = len(input[0]) - 1

    def neighbours(x, y):
        return [p for p in [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]
                if 0 <= p[0] <= grid_x and 0 <= p[1] <= grid_y]

    frontier = PriorityQueue()
    visited = {start}
    frontier.put((0, start))

    while frontier:
        cost, pos = frontier.get()

        if pos == end:
            return cost

        for n in neighbours(*pos):
            if n not in visited:
                x, y = n
                n_cost = grid[x][y]
                frontier.put((cost + n_cost, n))
                visited.add(n)


def search2(start, end, grid, tiles=5):
    """ Still uses Dijkstra but calculates the cost based on mapping back into the 
    original grid space."""
    grid_y = len(input)
    grid_x = len(input[0])

    def neighbours(x, y):
        return [p for p in [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]
                if 0 <= p[0] <= (grid_x * tiles) - 1 and 0 <= p[1] <= (grid_y * tiles) - 1]

    frontier = PriorityQueue()
    visited = {start}
    frontier.put((0, start))

    while frontier:
        cost, pos = frontier.get()

        if pos == end:
            return cost

        for n in neighbours(*pos):
            if n not in visited:
                x, y = n
                # cost is the original tile cost plus the number of tiles over
                # and number of tiles down
                n_cost = grid[x % grid_x][y % grid_y] + \
                    (x // grid_x) + (y // grid_y)

                if (n_cost) > 9:
                    n_cost = n_cost % 9

                frontier.put((cost + n_cost, n))
                visited.add(n)


@ log_time
def part_a(input):
    grid_y = len(input) - 1
    grid_x = len(input[0]) - 1

    return search((0, 0), (grid_x, grid_y), input)


@ log_time
def part_b(input):
    grid_y = len(input) * 5
    grid_x = len(input[0]) * 5

    return search2((0, 0), (grid_x - 1, grid_y - 1), input)


input = parse_input(open('day15/input.txt').readlines())

result_a = part_a(input)
result_b = part_b(input)
print("Part A:", result_a)
print("Part B:", result_b)
