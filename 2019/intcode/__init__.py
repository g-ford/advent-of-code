import logging

MODE_IMMEDIATE = "1"
MODE_POSTIONAL = "0"
MODE_RELATIVE = "2"


class InputInterrupt(Exception):
    pass


class OutputInterrupt(Exception):
    pass


class IntCodeComputer:

    def __init__(self, program=[], inputs=[]):
        self.program = dict(enumerate(program.copy()))
        self.inputs = inputs
        self.outputs = []
        self.HALTED = False
        self.current_instruction = 0
        self.relative_base = 0
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
            9: self.rel,
            99: self.halt
        }

    def value_at(self, pointer, mode):
        return self.program.get(self.index_at(pointer, mode), 0)

    def index_at(self, pointer, mode):
        if mode == MODE_RELATIVE:
            return self.relative_base + self.program.get(pointer, 0)
        if mode == MODE_POSTIONAL:
            return self.program.get(pointer, 0)
        if mode == MODE_IMMEDIATE:
            return pointer

    def pad_modes(self, pointer, no_args):
        return str(self.program[pointer]).zfill(no_args + 2)[: -2]

    def add(self, pointer):
        modes = self.pad_modes(pointer, 3)
        A = self.value_at(pointer+1, modes[2])
        B = self.value_at(pointer+2, modes[1])
        C = self.index_at(pointer + 3, modes[0])

        self.program[C] = A + B
        self.logger.debug("ADD %d %d %d", A, B, C)
        self.current_instruction += 4

    def mul(self, pointer):
        modes = self.pad_modes(pointer, 3)
        A = self.value_at(pointer+1, modes[2])
        B = self.value_at(pointer+2, modes[1])
        C = self.index_at(pointer + 3, modes[0])

        self.program[C] = A * B
        self.logger.debug("MUL %d %d %d", A, B, C)
        self.current_instruction += 4

    def rel(self, pointer):
        modes = self.pad_modes(pointer, 2)
        A = self.value_at(pointer+1, modes[1])

        self.logger.debug("REL %d '%d", A, self.relative_base + A)
        self.relative_base += A
        self.current_instruction += 2

    def mov(self, pointer):
        if len(self.inputs) == 0:
            self.logger.debug(self.inputs)
            raise InputInterrupt

        inp = self.inputs.pop(0)
        modes = self.pad_modes(pointer, 1)
        v = self.index_at(pointer+1, modes[0])

        self.program[v] = inp
        self.logger.debug("MOV %d %d '%s", inp, v, modes[0])
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
        modes = self.pad_modes(pointer, 3)
        A = self.value_at(pointer+1, modes[2])
        B = self.value_at(pointer+2, modes[1])
        C = self.index_at(pointer + 3, modes[0])

        self.logger.debug("CMP %d %d %d", A, B, C)

        if A < B:
            self.program[C] = 1
        else:
            self.program[C] = 0

        self.current_instruction += 4

    def eq(self, pointer):
        modes = self.pad_modes(pointer, 3)
        A = self.value_at(pointer+1, modes[2])
        B = self.value_at(pointer+2, modes[1])
        C = self.index_at(pointer + 3, modes[0])

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

    def run_no_interrupt(self, input_val=[]):
        while not self.HALTED:
            try:
                self.run(input_val)
            except OutputInterrupt:
                pass
        return self.outputs
