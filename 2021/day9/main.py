from utils import log_time


def parse_row(row):
    return list(map(int, list(row.strip())))


def neighbors(matrix, rowNumber, columnNumber, default=None, radius=1):
    return [[matrix[i][j] if i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0]) else default
             for j in range(columnNumber-1-radius, columnNumber+radius)]
            for i in range(rowNumber-1-radius, rowNumber+radius)]


def compass_points(matrix, x, y, default=None):
    return [((i, j), matrix[i][j]) if i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0]) else default
            for i, j in [(x + 1, y), (x-1, y), (x, y-1), (x, y+1)]
            ]


def compass_values(matrix, x, y, default=float('inf')):
    return [matrix[i][j] if i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0]) else default
            for i, j in [(x + 1, y), (x-1, y), (x, y-1), (x, y+1)]
            ]


def find_lows(matrix):
    for i, row in enumerate(matrix):
        for j, v in enumerate(row):
            n = compass_values(input, i, j)
            if v < min(n):
                yield ((i, j), v)


def basin(lp):
    search = set([lp])
    basin = set()
    while len(search) > 0:
        current = search.pop()
        if current:
            (x, y), v = current
            if v != 9:
                basin.add(current)
                search.update([p for p in compass_points(
                    input, x, y) if p not in basin])
    return basin


@ log_time
def part_a(input):
    return sum(p[1] + 1 for p in find_lows(input))


@ log_time
def part_b(input):
    basins = sorted([len(basin(lp))
                    for lp in find_lows(input)], reverse=True)
    return basins[0] * basins[1] * basins[2]


input = list(map(parse_row, open('day9/input.txt').readlines()))

result_a = part_a(input)
result_b = part_b(input)
print("Part A:", result_a)
print("Part B:", result_b)
