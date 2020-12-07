
input = open('input.txt').readlines()


def getParts(line):
    pattern, password = line.split(':')
    password = password.strip()

    range, letter = pattern.split()
    min, max = map(int, range.split('-'))
    return min, max, letter, password


def isValid(line):
    min, max, letter, password = getParts(line)
    return min <= password.count(letter) <= max


def isValid2(line):
    min, max, letter, password = getParts(line)
    count = [password[min-1] == letter, password[max-1] == letter]
    return sum(count) == 1


# input = ["1-3 a: abcde",
#          "1-3 b: cdefg",
#          "2-9 c: ccccccccc"
#          ]

print("Part 1: Valid count: ", sum(isValid(x) for x in input))
print("Part 2: Valid count: ", sum(isValid2(x) for x in input))
