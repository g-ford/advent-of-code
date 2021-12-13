from utils import log_time
import re


def parse_lines(lines):
    dots = set()
    folds = list()

    p = re.compile('(x|y)=(\d*)')

    def parse_fold(l):
        m = p.search(l)
        folds.append((int(m.group(2)), m.group(1)))

    def parse_dots(l):
        x, y = l.strip().split(',')
        dots.add((int(x), int(y)))

    for line in lines:
        if 'fold' in line:
            parse_fold(line)
        elif ',' in line:
            parse_dots(line)

    return dots, folds


@log_time
def part_a(input):

    dots, folds = input

    for f, dir in folds:
        if dir == 'y':
            for d in dots.copy():
                if d[1] > f:
                    dots.discard(d)
                    x, y = d
                    new_dot = (x, y - ((y-f) * 2))
                    dots.add(new_dot)
        if dir == 'x':
            for d in dots.copy():
                if d[0] > f:
                    dots.discard(d)
                    x, y = d
                    new_dot = (x - ((x - f) * 2), y)
                    dots.add(new_dot)
        return(len(dots))


@log_time
def part_b(input):
    dots, folds = input

    for f, dir in folds:
        if dir == 'y':
            for d in dots.copy():
                if d[1] > f:
                    dots.discard(d)
                    x, y = d
                    new_dot = (x, y - ((y-f) * 2))
                    dots.add(new_dot)
        if dir == 'x':
            for d in dots.copy():
                if d[0] > f:
                    dots.discard(d)
                    x, y = d
                    new_dot = (x - ((x - f) * 2), y)
                    dots.add(new_dot)

    min_x = min(x for (x, y) in dots)
    max_x = max(x for (x, y) in dots)

    min_y = min(y for (x, y) in dots)
    max_y = max(y for (x, y) in dots)

    for y in range(min_y, max_y + 1):
        line = []
        for x in range(min_x, max_x + 1):
            if (x, y) in dots:
                line.append('#')
            else:
                line.append(" ")
        print("".join(line))


input = parse_lines(open('day13/input.txt').readlines())

result_a = part_a(input)
result_b = part_b(input)
print("Part A:", result_a)
print("Part B:", result_b)
