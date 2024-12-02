from utils import log_time


def is_safe2(report):
    gaps = [j-i for i, j in zip(report[:-1], report[1:])]
    if not (all(val > 0 for val in gaps) or all(val < 0 for val in gaps)):
        #print("Not safe, direction change ", report, gaps)
        return False
    if not (all(0 < gap < 4 for gap in gaps) or all(-4 < gap < 0 for gap in gaps)):
        #print("Not safe, gap: ", report, gaps)
        return False

    return True


def is_safe_with_dampener(report):
    """ Brute force solution to check if a report is safe with a level removed """

    # I feel like there should be a way to check if there is only one case of a gap of 0 or negative
    # then it is still safe. Any gaps larger than 4 will always be unsafe

    if is_safe2(report):
        return True

    for i in range(len(report)):
        if is_safe2(report[:i] + report[i+1:]):
            return True


@log_time
def part1(reports):
    results = list(map(is_safe2, reports))
    return sum(results)


@log_time
def part2(reports):
    return sum(1 for report in reports if is_safe_with_dampener(report))


@log_time
def parse_input(lines):
    """Separate each line into a list of ints"""
    return [list(map(int, line.split())) for line in lines.split("\n")]


lines = open("day02/input.txt", encoding="utf8").read()

parts = parse_input(lines)

print("Part 1: ", part1(parts))
print("Part 2: ", part2(parts))
