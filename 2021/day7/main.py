from functools import cache
from utils import log_time


@log_time
def part_a(input):
    least = (float('inf'), float('inf'))
    for x in range(max(input)):
        cost = sum([abs(p - x) for p in input])
        if cost < least[0]:
            least = (cost, x)
    return least


@log_time
def part_b(input):

    # Some fun stats:
    # | Method              | Time      |
    # | Naive sum           | ~15 secs  |
    # | Naive sum + cache   | ~270ms    |
    # | Math                | ~380ms    |
    # | Math + cache        | ~240ms    |
    @cache
    def calc_cost(n):
        # sum a series of integers
        # return sum(range(n + 1))
        return (n * (n+1)) / 2

    least = (float('inf'), float('inf'))
    for x in range(max(input)):
        cost = sum([calc_cost(abs(p - x)) for p in input])
        if cost < least[0]:
            least = (cost, x)
    return least


input = list(map(int, open('day7/input.txt').readlines()[0].split(',')))

result_a = part_a(input)
result_b = part_b(input)
print("Part A:", result_a)
print("Part B:", result_b)
