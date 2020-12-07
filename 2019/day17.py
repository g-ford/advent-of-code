from intcode import IntCodeComputer, InputInterrupt, OutputInterrupt
from operator import add
from time import sleep

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def add_tuples(p, v):
    return tuple(map(add, p, v))


def renderMap(amap):
    min_y = min(y for (x, y) in amap)
    max_y = max(y for (x, y) in amap)
    min_x = min(x for (x, y) in amap)
    max_x = max(x for (x, y) in amap)
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            print(chr(amap[x, y]), end='')
        print('')


def renderArray(arr):
    for x in arr:
        print(chr(x), end='', sep='')


def arrayToMap(arr):
    amap = {}
    x = y = 0
    bot_position = (0, 0)
    for p in arr:
        if p == 10:
            y += 1
            x = 0
            continue

        if p in [ord('<'), ord('>'), ord('^'), ord('v')]:
            bot_position = (x, y)
            p = 35
        amap[(x, y)] = p
        x += 1
    return amap, bot_position


def findIntersections(amap):
    intersections = []
    for k, v in amap.items():
        neighbours = [add_tuples(k, d) for d in dirs]
        if v == 35 and all(amap.get(k2, None) == 35 for k2 in neighbours):
            intersections.append(k)
    return intersections


def str_to_incode(string):
    p = string.split(',')
    code = []
    for x in p:
        try:
            code.append(ord(x))
        except:
            code.append(int(x))
        code.append(ord(','))
    # replace last comma with new line
    code[-1] = ord("\n")
    return code


if __name__ == "__main__":
    program = list(map(int, open('inputs/day17.txt').read().split(',')))

    c = IntCodeComputer(program)

    initial_map = c.run_no_interrupt()
    amap, bot_position = arrayToMap(initial_map)
    intersections = findIntersections(amap)

    print("Alignment", sum(x * y for x, y in intersections))

    main = "C,A,A,B,B,C,C,A,A,B"
    A = "R,12,R,4,L,12"
    B = "R,12,R,4,L,6,L,8,L,8"
    C = "L,12,R,4,R,4"
    display = "y"

    codes = list(map(str_to_incode, [main, A, B, C, display]))

    c2 = IntCodeComputer([2] + program[1:])
    loop = 0
    while not c2.HALTED:
        try:
            c2.run_no_interrupt()
        except InputInterrupt:
            print("Render ", loop)
            renderArray(c2.outputs)
            print("IN", codes[loop])
            c2.inputs = codes[loop]
            loop += 1

    # dust = c2.run_no_interrupt()
    # print("Dust", dust)
    # renderArray(dust)
