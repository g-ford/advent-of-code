MODE_IMMEDIATE = "1"
MODE_POSTIONAL = "0"


class IntCodeComputer:
    def __init__(self):
        self.program = []
        self.inputs = None
        self.outputs = []
        self.HALTED = False

    def value_at(self, pointer, mode):
        value = self.program[pointer]
        if mode == MODE_IMMEDIATE:
            return value
        return self.program[value]

    def pad_modes(self, pointer, no_args):
        return str(self.program[pointer]).zfill(no_args + 2)[: -2]

    def add(self, pointer):
        modes = self.pad_modes(pointer, 2)
        A = self.value_at(pointer+1, modes[1])
        B = self.value_at(pointer+2, modes[0])
        C = self.program[pointer + 3]
        self.program[C] = A + B
        return pointer + 4

    def mul(self, pointer):
        modes = self.pad_modes(pointer, 2)
        A = self.value_at(pointer+1, modes[1])
        B = self.value_at(pointer+2, modes[0])
        C = self.program[pointer + 3]
        self.program[C] = A * B
        return pointer + 4

    def mov(self, pointer):
        self.program[self.program[pointer+1]] = self.inputs
        return pointer + 2

    def pop(self, pointer):
        modes = self.pad_modes(pointer, 2)
        A = self.value_at(pointer+1, modes[1])
        self.outputs.append(A)
        return pointer + 2

    def halt(self, pointer):
        self.HALTED = True
        return 0

    def jnz(self, pointer):
        modes = self.pad_modes(pointer, 2)
        test = self.value_at(pointer+1, modes[1])
        if test != 0:
            return self.value_at(pointer+2, modes[0])
        return pointer+3

    def jz(self, pointer):
        modes = self.pad_modes(pointer, 2)
        test = self.value_at(pointer+1, modes[1])
        if test == 0:
            return self.value_at(pointer+2, modes[0])
        return pointer+3

    def cmp(self, pointer):
        modes = self.pad_modes(pointer, 2)
        A = self.value_at(pointer+1, modes[1])
        B = self.value_at(pointer+2, modes[0])
        C = self.program[pointer + 3]

        if A < B:
            self.program[C] = 1
        else:
            self.program[C] = 0

        return pointer + 4

    def eq(self, pointer):
        modes = self.pad_modes(pointer, 2)
        A = self.value_at(pointer+1, modes[1])
        B = self.value_at(pointer+2, modes[0])
        C = self.program[pointer + 3]

        if A == B:
            self.program[C] = 1
        else:
            self.program[C] = 0

        return pointer + 4

    def run(self, program, inputs=None, outputs=[]):
        self.program = program
        self.inputs = inputs
        self.outputs = outputs
        self.HALTED = False
        pointer = 0

        opcodes = {
            1: self.add,
            2: self.mul,
            3: self.mov,
            4: self.pop,
            5: self.jnz,
            6: self.jz,
            7: self.cmp,
            8: self.eq,
            99: self.halt
        }

        while(not self.HALTED):
            opcode = int(str(program[pointer])[-2:])
            pointer = opcodes[opcode](pointer)
        return program[pointer]
