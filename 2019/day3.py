from operator import itemgetter


def manhatten_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def points_on_path(path):
    current_point = (0, 0)
    points = set()
    travel_distances = {}
    travelled = 0

    for step in path:
        direction = step[0]
        distance = int(step[1:])

        if (direction == 'U'):
            for x in range(distance):
                p = (current_point[0], current_point[1] + x)
                points.add(p)
                travel_distances[p] = travel_distances.get(p, travelled + x)
            current_point = (current_point[0], current_point[1] + distance)

        if (direction == 'D'):
            for x in range(distance):
                p = (current_point[0], current_point[1] - x)
                points.add(p)
                travel_distances[p] = travel_distances.get(p, travelled + x)
            current_point = (current_point[0], current_point[1] - distance)

        if (direction == 'L'):
            for x in range(distance):
                p = (current_point[0] - x, current_point[1])
                points.add(p)
                travel_distances[p] = travel_distances.get(p, travelled + x)
            current_point = (current_point[0] - distance, current_point[1])

        if (direction == 'R'):
            for x in range(distance):
                p = (current_point[0] + x, current_point[1])
                points.add(p)
                travel_distances[p] = travel_distances.get(p, travelled + x)
            current_point = (current_point[0] + distance, current_point[1])

        travelled += distance

    return points, travel_distances


def min_distance(pathA, pathB):
    pointsA, _ = points_on_path(pathA)
    pointsB, _ = points_on_path(pathB)

    crosses = pointsA.intersection(pointsB)
    crosses.remove((0, 0))  # origin doesn't count

    distances = [(manhatten_distance((0, 0), x), x) for x in crosses]

    return min(distances, key=itemgetter(0))[0]


def min_travel(pathA, pathB):
    pointsA, travelA = points_on_path(pathA)
    pointsB, travelB = points_on_path(pathB)

    crosses = pointsA.intersection(pointsB)
    crosses.remove((0, 0))  # origin doesn't count

    distances = [travelA[p] + travelB[p] for p in crosses]

    return min(distances)


if __name__ == "__main__":
    assert(min_distance(['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'],
                        ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']) == 159)
    assert(min_distance(['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'],
                        ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']) == 135)

    assert(min_travel(['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'],
                      ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']) == 610)
    assert(min_travel(['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'],
                      ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']) == 410)

    paths = open('inputs/day3.txt').readlines()
    pathA = paths[0].split(',')
    pathB = paths[1].split(',')

    print("Min Distance:", min_distance(pathA, pathB))
    print("Min Travel:", min_travel(pathA, pathB))
