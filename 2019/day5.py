from intcode import IntCodeComputer
c = IntCodeComputer()

if __name__ == "__main__":
    program = list(map(int, open('inputs/day5.txt').read().split(',')))

    diag = c.run(program.copy(), 1, [])
    print("Part 1:", c.outputs)

    diag = c.run(program.copy(), 5, [])
    print("Part 2:", c.outputs)
