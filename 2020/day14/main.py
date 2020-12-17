import re
from itertools import product


def parse(l):
    if "mask = " in l:
        mask = l.strip().replace("mask = ", "")
        return ["m", [(i, v) for i, v in enumerate(mask)]]

    m = re.match(r"mem\[(\d*)\] = (\d*)$", l)
    return [int(i) for i in m.groups()]


def apply_mask(value, mask):
    as36 = "{0:036b}".format(value)
    # in part 1 we ignore the X
    for m in [m2 for m2 in mask if m2[1] != "X"]:
        as36 = as36[:m[0]] + m[1] + as36[m[0]+1:]
    return int(as36, 2)


def apply_mask2(address, mask):
    as36 = "{0:036b}".format(address)

    # first replace all the non-zeros
    for m in [m2 for m2 in mask if m2[1] != "0"]:
        as36 = as36[:m[0]] + m[1] + as36[m[0]+1:]

    # make in `format` format
    as36 = as36.replace('X', '{}')

    # create a set of 0,1 replacements
    replacements = product((0, 1), repeat=as36.count('{}'))

    # now we run a bunch of formats
    return [as36.format(*r) for r in replacements]

    # the format trick is considerably faster than my initial attempt below
    # with all its multi-loop amazingness
    addresses = set()
    addresses.add(as36)

    while any(True for a in addresses if "X" in a):
        for a in addresses.copy():
            removed = False
            for i, m in enumerate(a):
                if m == "X":
                    addresses.add(a[:i] + "0" + a[i+1:])
                    addresses.add(a[:i] + "1" + a[i+1:])
                    removed = True
            if removed:
                addresses.remove(a)

    return addresses


def run(program):
    register = {}
    mask = {}
    for instruction in program:
        if instruction[0] == "m":
            mask = instruction[1]
        else:
            register[instruction[0]] = apply_mask(instruction[1], mask)

    return register


def run2(program):
    register = {}
    mask = {}
    for instruction in program:
        if instruction[0] == "m":
            mask = instruction[1]
        else:
            for r in apply_mask2(instruction[0], mask):
                register[r] = instruction[1]

    return register


program = [parse(l) for l in open("input.txt").readlines()]
print("Part 1:", sum(run(program).values()))
print("Part 2:", sum(run2(program).values()))
