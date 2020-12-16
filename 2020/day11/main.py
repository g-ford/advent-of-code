# game of aritport seats

from collections import defaultdict, namedtuple
from time import sleep

OCCUPIED = "#"
FLOOR = "."
SEAT = "L"
Seat = namedtuple("Seat", ["x", "y", "status"])


input = open('input.txt').readlines()
board_width = len(input[0].strip())
intial_board = [Seat(x, y, status)
                for x, row in enumerate(input)
                for y, status in enumerate(row.strip())]

max_x = max(c.x for c in intial_board) + 1
max_y = max(c.y for c in intial_board) + 1


def neighbours(cell, board):
    for x in range(cell.x - 1, cell.x + 2):
        for y in range(cell.y - 1, cell.y + 2):
            if (x, y) != (cell.x, cell.y):
                yield (x, y)


def non_empty_neighbours(cell, board):
    for x in range(-1, 2):
        for y in range(-1, 2):
            i = 1
            while 0 <= cell.x + i * x < max_x and 0 <= cell.y + i * y < max_y and not x == y == 0:
                tx = cell.x + i * x
                ty = cell.y + i * y
                if Seat(tx, ty, FLOOR) not in board:
                    yield (tx, ty)
                    break
                i += 1


def count_neighbours(board, neighbour_test):
    neighbour_counts = defaultdict(int)
    for seat in board:
        if seat.status == OCCUPIED:
            for neighbour in neighbour_test(seat, board):
                neighbour_counts[neighbour] += 1
    return neighbour_counts


def print_board(board):
    out = ""
    for c in board:
        if c.y == 0:
            out += "\n"
        out += c.status
    return out


def iterate(board, max_neighbours=4, neighbour_test=neighbours):
    next = []
    counts = count_neighbours(board, neighbour_test)
    for cell in board:
        if cell.status == FLOOR:
            next.append(cell)
        elif (cell.x, cell.y) not in counts:
            next.append(Seat(cell.x, cell.y, OCCUPIED))
        elif counts[(cell.x, cell.y)] >= max_neighbours:
            next.append(Seat(cell.x, cell.y, SEAT))
        else:
            next.append(cell)
    return next, board


def part1(b):
    while True:
        b, old = iterate(b)
        #print("\033[2J\033[1;1H" + print_board(b))
        if b == old:
            break
    return sum(1 for x in b if x.status == OCCUPIED)


def part2(b):
    while True:
        b, old = iterate(b, 5, non_empty_neighbours)
        if b == old:
            break
    return sum(1 for x in b if x.status == OCCUPIED)


print("Part 1:", part1(intial_board), "occupied")

# This is suuuuuper slow....
print("Part 2:", part2(intial_board), "occupied")
