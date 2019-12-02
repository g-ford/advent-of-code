

def op1(pointer, program):
    A = program[program[pointer + 1]]
    B = program[program[pointer + 2]]
    C = program[pointer + 3]
    program[C] = A + B
    return False, pointer + 4, program


def op2(pointer, program):
    A = program[program[pointer + 1]]
    B = program[program[pointer + 2]]
    C = program[pointer + 3]
    program[C] = A * B
    return False, pointer + 4, program


def op99(current_pos, program):
    return True, 0, program


def run(program):
    halted = False
    pointer = 0

    opcodes = {
        1: op1,
        2: op2,
        99: op99
    }

    while(not halted):
        opcode = program[pointer]
        halted, pointer, program = opcodes[opcode](pointer, program)
    return program[pointer]


def pairs(max):
    for i in range(max):
        for j in range(max):
            yield i, j


if __name__ == "__main__":
    assert(run([1, 0, 0, 0, 99]) == 2)
    assert(run([2, 4, 4, 5, 99, 0]) == 2)
    assert(run([2, 3, 0, 3, 99]) == 2)
    assert(run([1, 1, 1, 4, 99, 5, 6, 0, 99]) == 30)

    orig_program = list(map(int, open('day2.txt').read().split(',')))

    program = orig_program.copy()
    program[1] = 12
    program[2] = 2
    print("Terminated with: ", run(program))

    max = 99
    for noun, verb in pairs(max):
        program = orig_program.copy()
        program[1] = noun
        program[2] = verb
        if (run(program) == 19690720):
            print("Noun, verb", noun, verb)
            break
