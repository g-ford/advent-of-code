from copy import deepcopy


def parseIns(line):
    # op, value
    return [line[:3], int(line[4:].strip())]


instructions = list(map(parseIns, open('input.txt').readlines()))


def run(instructions):
    acc = 0
    seen = set()
    pointer = 0
    while True:
        if (pointer >= len(instructions)):
            # print("End of code detected")
            return acc, False

        if (pointer in seen):
            # print("Loop detected")
            return acc, True
        else:
            seen.add(pointer)

        ins = instructions[pointer]
        if(ins[0] == "acc"):
            acc += ins[1]

        # of course rotate goes in the wrong direction :)
        # so we have to invert the sign
        if (ins[0] == "jmp"):
            pointer += ins[1]
        else:
            pointer += 1


print("Part 1:", run(instructions))

print(instructions)
for i in range(len(instructions)):
    candidate = deepcopy(instructions)
    if candidate[i][0] == "jmp":
        candidate[i][0] = "nop"
    elif candidate[i][0] == "nop":
        candidate[i][0] = "jmp"
    else:
        continue

    result = run(candidate)
    if (not result[1]):
        print("Part 2:", i, result)
        break
