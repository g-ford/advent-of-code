import logging

MODE_IMMEDIATE = "1"
MODE_POSTIONAL = "0"


class InputInterrupt(Exception):
    pass


class OutputInterrupt(Exception):
    pass


class IntCodeComputer:

    def __init__(self, program=[], inputs=[]):
        self.program = program.copy()  # isolate this computers memory
        self.inputs = inputs
        self.outputs = []
        self.HALTED = False
        self.current_instruction = 0
        self.logger = logging.getLogger(self.__class__.__name__)

        self.opcodes = {
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
        self.logger.debug("ADD %d %d %d", A, B, C)
        self.current_instruction += 4

    def mul(self, pointer):
        modes = self.pad_modes(pointer, 2)
        A = self.value_at(pointer+1, modes[1])
        B = self.value_at(pointer+2, modes[0])
        C = self.program[pointer + 3]
        self.program[C] = A * B
        self.logger.debug("MUL  %d %d %d", A, B, C)
        self.current_instruction += 4

    def mov(self, pointer):
        if len(self.inputs) == 0:
            raise InputInterrupt

        inp = self.inputs.pop(0)
        self.program[self.program[pointer+1]] = inp
        self.logger.debug("MOV %d %d", inp, self.program[pointer+1])
        self.current_instruction += 2

    def pop(self, pointer):
        modes = self.pad_modes(pointer, 2)
        A = self.value_at(pointer+1, modes[1])
        self.outputs.append(A)
        self.logger.debug("POP %d '%d", pointer + 1, A)
        self.current_instruction += 2
        raise OutputInterrupt

    def halt(self, pointer):
        self.HALTED = True
        self.logger.debug('HALT')
        return 0

    def jnz(self, pointer):
        modes = self.pad_modes(pointer, 2)
        test = self.value_at(pointer+1, modes[1])

        if test != 0:
            self.logger.debug("JNZ %d %d 'jumped", test, self.value_at(
                pointer+2, modes[0]))
            self.current_instruction = self.value_at(pointer+2, modes[0])
            return
        self.logger.debug("JNZ %d %d 'not jumped", test, self.value_at(
            pointer+2, modes[0]))
        self.current_instruction += 3

    def jz(self, pointer):
        modes = self.pad_modes(pointer, 2)
        test = self.value_at(pointer+1, modes[1])

        if test == 0:
            self.logger.debug("JZ %d %d 'jumped", test,
                              self.value_at(pointer+2, modes[0]))
            self.current_instruction = self.value_at(pointer+2, modes[0])
            return
        self.logger.debug("JZ %d %d 'not jumped", test,
                          self.value_at(pointer+2, modes[0]))
        self.current_instruction += 3

    def cmp(self, pointer):
        modes = self.pad_modes(pointer, 2)
        A = self.value_at(pointer+1, modes[1])
        B = self.value_at(pointer+2, modes[0])
        C = self.program[pointer + 3]

        self.logger.debug("CMP %d %d %d", A, B, C)

        if A < B:
            self.program[C] = 1
        else:
            self.program[C] = 0

        self.current_instruction += 4

    def eq(self, pointer):
        modes = self.pad_modes(pointer, 2)
        A = self.value_at(pointer+1, modes[1])
        B = self.value_at(pointer+2, modes[0])
        C = self.program[pointer + 3]

        self.logger.debug("EQ %d %d %d", A, B, C)

        if A == B:
            self.program[C] = 1
        else:
            self.program[C] = 0

        self.current_instruction += + 4

    def run(self, input_val=[]):
        self.inputs.extend(input_val)
        while(not self.HALTED):
            opcode = self.program[self.current_instruction] % 100
            op_function = self.opcodes[opcode]
            op_function(self.current_instruction)
        return self.outputs
