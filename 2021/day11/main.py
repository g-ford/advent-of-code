from utils import log_time


def neighbours(k, j):
    return [
        (k - 1, j - 1), (k, j - 1), (k + 1, j - 1),
        (k - 1, j),                 (k + 1, j),
        (k - 1, j + 1), (k, j + 1), (k + 1, j + 1),
    ]


def parse_line(l):
    return list(map(int, l.strip()))


@ log_time
def part_a(input):
    step = input[::]

    total_flashes = 0

    for _ in range(100):
        step = [[c + 1 for c in r] for r in step]
        flashing = True
        flashed = []
        while flashing:
            flashing = False
            for i, r in enumerate(step):
                for j, c in enumerate(r):
                    if c > 9 and (i, j) not in flashed:
                        flashing = True
                        flashed.append((i, j))
                        for n in neighbours(i, j):
                            if 0 <= n[0] <= 9 and 0 <= n[1] <= 9:
                                step[n[0]][n[1]] += 1
        total_flashes += len(flashed)

        step = [[0 if c > 9 else c for c in r] for r in step]
    return total_flashes


@ log_time
def part_b(input):
    step = input[::]
    synced = False
    step_count = 0
    while not synced:
        step = [[c + 1 for c in r] for r in step]
        step_count += 1
        flashing = True
        flashed = []
        while flashing:
            flashing = False
            for i, r in enumerate(step):
                for j, c in enumerate(r):
                    if c > 9 and (i, j) not in flashed:
                        flashing = True
                        flashed.append((i, j))
                        for n in neighbours(i, j):
                            if 0 <= n[0] <= 9 and 0 <= n[1] <= 9:
                                step[n[0]][n[1]] += 1
        if len(flashed) == 100:
            synced = True

        step = [[0 if c > 9 else c for c in r] for r in step]
    return step_count


input = list(map(parse_line, open('day11/input.txt').readlines()))


result_a = part_a(input)
result_b = part_b(input)
print("Part A:", result_a)
print("Part B:", result_b)
