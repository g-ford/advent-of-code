from math import atan2, pi
from collections import defaultdict


def parse_map(lines):
    asteroids = []
    for y, l in enumerate(lines):
        for x, c in enumerate(l):
            if c == "#":
                asteroids.append((x, y))
    return asteroids


def manhatten_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def angle(p1, p2):
    """Angle as radians with 0 at 12 o'clock"""
    return atan2(p2[0] - p1[0], p1[1] - p2[1]) % (2 * pi)


def angles(base, asteroids):
    return (angle(base, a)
            for a in asteroids
            if a != base)


def visible_count(base, asteroids):
    return len(set(angles(base, asteroids)))


def all_visibile(asteroids):
    return ((a, visible_count(a, asteroids)) for a in asteroids)


def best_base(asteroids):
    return max(all_visibile(asteroids), key=lambda x: x[1])


def destroy_order(base, asteroids):
    asteroid_map = defaultdict(list)
    for a in asteroids:
        if a != base:
            deg = angle(base, a)
            asteroid_map[deg].append((manhatten_distance(a, base), a))
            asteroid_map[deg] = sorted(asteroid_map[deg], key=lambda x: x[0])

    return asteroid_map


def vaporise(num, asteroids):
    if num < len(asteroids):
        keys = sorted(asteroids.keys())
        return asteroids[keys[num - 1]][0]

    # each iteration through keys will pop the first asteroid
    # in that line of sight only
    killed = 0
    while True:
        for p in sorted(asteroids.keys()):
            killed += 1
            x = asteroids[p].pop(0)
            print("Killed", killed, x, p, asteroids[p])
            if killed == num:
                return x

            # if there are no more asteroids in this line of sight
            # remove it so the next rotation skips through
            if len(asteroids[p]) == 0:
                del asteroids[p]


if __name__ == "__main__":
    asteroids = parse_map(open('inputs/day10.txt').readlines())

    base = best_base(asteroids)
    print("Best Base", base)
    print(vaporise(200, destroy_order(base[0], asteroids)))
