# python -m day1.main

from utils import log_time


def calibrate(inputTxt):
    """Sum the first and last digits as a single two digit number"""
    return sum(int(x[0] + x[-1]) for x in inputTxt)


def only_digits(value):
    """Remove all non numeric characters"""
    value = value.strip()
    return list(x for x in value.strip() if x.isnumeric())


def only_digits2(value):
    """Remove all non numeric characters after replacing words with numbers"""
    value = value.strip()
    for i, n in enumerate(
        ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    ):
        # This replaces the word with the word + the number  + word so that
        # subsequent replacements can use the start/tail end of the word
        value = value.replace(n, n + str(i + 1) + n)

    return only_digits(value)


@log_time
def part1():
    inputTxt = list(map(only_digits, open("day1/input.txt").readlines()))
    print("Part 1:", calibrate(inputTxt))


@log_time
def part2():
    inputTxt2 = list(
        map(only_digits2, open("day1/input.txt", encoding="utf8").readlines())
    )
    print("Part 2:", calibrate(inputTxt2))


part1()
part2()
