import re


def byr(line):
    m = re.search('byr:(\d{4})', line)
    return m is not None and (1920 <= int(m.groups()[0]) <= 2002)


def iyr(line):
    m = re.search('iyr:(\d{4})', line)
    return m is not None and (2010 <= int(m.groups()[0]) <= 2020)


def eyr(line):
    m = re.search('eyr:(\d{4})', line)
    return m is not None and (2020 <= int(m.groups()[0]) <= 2030)


def hgt(line):
    m = re.search('hgt:(\d{2,3})(in|cm)', line)
    if m and m.groups() and len(m.groups()) == 2:
        val, unit = m.groups()
        return (unit == "in" and 59 <= int(val) <= 76) or (unit == "cm" and 150 <= int(val) <= 193)
    return False


def hcl(line):
    m = re.search('hcl:#[0-9a-f]{6}(\s|$)', line)
    return m is not None


def ecl(line):
    m = re.search('ecl:(amb|blu|brn|gry|grn|hzl|oth)(\s|$)', line)
    return m is not None


def pid(line):
    m = re.search("pid:\d{9}(\s|$)", line)
    return m is not None


required = [('byr', byr), ("iyr", iyr), ("eyr", eyr),
            ("hgt", hgt), ("hcl", hcl), ("ecl", ecl), ("pid", pid)]


lines = open('input.txt').read().split("\n\n")


def p1(lines):
    valid = 0
    for line in lines:
        if (all(re.search(code, line) for (code, _) in required)):
            valid += 1
    return valid


def p2(lines):
    valid = 0
    for line in lines:
        if (all(re.search(code, line) and val(line)
                for (code, val) in required)):
            valid += 1
    return valid


print("Part 1:", p1(lines))
print("Part 2:", p2(lines))
