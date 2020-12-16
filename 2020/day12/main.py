
from copy import deepcopy
import numpy as np
import math


def parse(l):
    return [l[0], int(l[1:])]


gps_ = list(map(parse, open("input.txt").readlines()))

pos = [0, 0, 90]  # E, N, deg
deg_to_card = {
    0: "N",
    90: "E",
    180: "S",
    270: "W"
}


def rotate(p, origin=(0, 0), degrees=0):
    # Yay to StackOverflow coding
    angle = np.deg2rad(degrees)
    R = np.array([[np.cos(angle), -np.sin(angle)],
                  [np.sin(angle),  np.cos(angle)]])
    o = np.atleast_2d(origin)
    p = np.atleast_2d(p)
    return np.squeeze((R @ (p.T-o.T) + o.T).T)


def part1(gps):
    pos = [0, 0, 90]
    for move in gps.copy():
        if move[0] == "F":
            move[0] = deg_to_card[pos[2]]

        if move[0] == "N":
            pos[1] += move[1]
        if move[0] == "S":
            pos[1] -= move[1]
        if move[0] == "E":
            pos[0] += move[1]
        if move[0] == "W":
            pos[0] -= move[1]

        if move[0] == "R":
            pos[2] = (pos[2] + move[1]) % 360
        if move[0] == "L":
            pos[2] = (pos[2] + 360 - move[1]) % 360

    return abs(pos[0]) + abs(pos[1])


def part2(gps):
    pos = [0, 0, 90]
    waypoint = [10, 1]

    for move in gps:
        if move[0] == "F":
            pos[0] += waypoint[0] * move[1]
            pos[1] += waypoint[1] * move[1]

        if move[0] == "N":
            waypoint[1] += move[1]
        if move[0] == "S":
            waypoint[1] -= move[1]
        if move[0] == "E":
            waypoint[0] += move[1]
        if move[0] == "W":
            waypoint[0] -= move[1]

        if move[0] == "R":
            waypoint = rotate(waypoint, degrees=move[1] * -1)
        if move[0] == "L":
            waypoint = rotate(waypoint, degrees=move[1])

    return math.ceil(abs(pos[0]) + abs(pos[1]))


print("Print part 1:", part1(deepcopy(gps_)))
print("Print part 2:", part2(gps_))
