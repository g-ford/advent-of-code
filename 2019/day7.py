from intcode import IntCodeComputer, InputInterrupt, OutputInterrupt
from itertools import permutations
import logging
logging.basicConfig(level=logging.INFO)


def max_sequence(program, phases):
    return max(run_with_phases(program, x)
               for x in permutations(phases))


def run_with_phases(program, phases):
    amplifiers = [IntCodeComputer(program, [phase]) for phase in phases]

    amplifiers[0].inputs.append(0)
    no_amps = len(amplifiers)

    i = -1
    while amplifiers[-1].HALTED == False:
        i = (i+1) % no_amps
        while True:
            try:
                amp = amplifiers[i]
                amp.run()
                break
            except OutputInterrupt:
                amplifiers[(i+1) % no_amps].inputs.append(amp.outputs[-1])
                continue
            except InputInterrupt:
                break

    return amplifiers[-1].outputs[-1]


if __name__ == "__main__":

    assert(max_sequence([3, 15, 3, 16, 1002, 16, 10, 16, 1,
                         16, 15, 15, 4, 15, 99, 0, 0], range(5)) == 43210)
    assert(max_sequence([3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23,
                         101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0], range(5)) == 54321)

    program = list(map(int, open('inputs/day7.txt').read().split(',')))
    print("Max single phase", max_sequence(program, range(5)))

    assert(max_sequence([3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26,
                         27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5], range(5, 10)) == 139629729)
    assert(max_sequence([3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55, 1005, 55, 26, 1001, 54,
                         -5, 54, 1105, 1, 12, 1, 53, 54, 53, 1008, 54, 0, 55, 1001, 55, 1, 55, 2, 53, 55, 53, 4,
                         53, 1001, 56, -1, 56, 1005, 56, 6, 99, 0, 0, 0, 0, 10], range(5, 10)) == 18216)

    print("Max looped phase", max_sequence(program, range(5, 10)))
