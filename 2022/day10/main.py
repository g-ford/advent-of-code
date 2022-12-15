def simulate(inst, cycles, x=1):
    strengths = []
    clock = 1
    for i in inst:
        if clock in cycles:
            strengths.append(clock * x)
        if clock >= max(cycles):
            return strengths
        if i == "noop":
            clock += 1
        else:
            if clock + 1 in cycles:
                strengths.append((clock + 1) * x)
            clock += 2
            x += int(i.split()[1])


def draw(instructions):
    screen = [[" " for y in range(40)] for x in range(6)]

    # turn instructions into cycles
    inst = []
    for i in instructions:
        # an add counts as two cycles so we just split the instruction
        inst += i.split()

    sprite_loc = 1
    row = 1
    clock = 0
    for cmd in inst:
        if clock > 39:
            clock = 0
            row += 1

        if abs(clock - sprite_loc) <= 1:
            # the sprite is 3 wide, so if the cycle and sprite line up
            # + or - 1 we blat to the screen
            screen[row-1][clock] = '█'

        if cmd != 'addx' and cmd != 'noop':
            sprite_loc += int(cmd)

        clock += 1

    return screen


def print_screen(screen):
    for row in screen:
        print("".join(row))


def day9(input):
    s = simulate(input, [20, 60, 100, 140, 180, 220])
    print("Part 1: ", sum(s))
    print("Part 2: ", print_screen(draw(input)))


if __name__ == "__main__":

    def clean(value):
        return value.strip()

    input = list(map(clean, open("day10/input.txt").readlines()))
    day9(input)
