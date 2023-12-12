
import math
import re

from utils import log_time


def find_win_range(race):
    """Calculate the min time to hold and max time to hold and return the difference"""

    # Holding a button increases the velocity by 1 each tick
    # So we need to find x(T - x) > D where T is the time and D is the distance
    # Solving for x https://www.wolframalpha.com/input?i=solve+for+x%3A+x%28T+-+x%29+%3E+D
    # We get (T - sqrt(T^2 - 4D)) / 2  <  x  <  (T + sqrt(T^2 - 4D)) / 2
    T = race[0]
    D = race[1]

    # Lower end
    a = (T - math.sqrt(T**2 - 4*D)) / 2
    # We need to find the next full tick higher than a
    if a.is_integer():
        a += 1
    else:
        a = math.ceil(a)

    # Upper end
    b = (T + math.sqrt(T**2 - 4*D)) / 2
    # We need to find the next full tick lower than b
    if b.is_integer():
        b -= 1
    else:
        b = math.floor(b)

    return b - a + 1 # +1 because we need to include the last tick

@log_time
def part1(races):
    return math.prod(map(find_win_range, races))

@log_time
def part2(race):
    return find_win_range(race)


@log_time
def parse_input(lines):
    times = list(map(int, re.findall(r"(\d+)", lines[0])))
    distances = list(map(int, re.findall(r"(\d+)", lines[1])))
    return zip(times, distances)

@log_time
def parse_input_once_race(lines):
    times = list(re.findall(r"(\d+)", lines[0]))
    distances = list(re.findall(r"(\d+)", lines[1]))
    time = int("".join(times))
    distance = int("".join(distances))
    return time, distance


lines = open("day6/input.txt", encoding="utf8").readlines()
races = list(parse_input(lines))
once_race = parse_input_once_race(lines)

print("Part 1: ", part1(races))
print("Part 2: ", part2(once_race))
