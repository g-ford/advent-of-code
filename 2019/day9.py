from intcode import IntCodeComputer
import logging
import sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
if __name__ == "__main__":
    p = [109, 1, 204, -1, 1001, 100, 1, 100,
         1008, 100, 16, 101, 1006, 101, 0, 99]
    c = IntCodeComputer(p)
    assert(c.run_no_interrupt() == p)

    c = IntCodeComputer([1102, 34915192, 34915192, 7, 4, 7, 99, 0])
    assert(len(str(c.run_no_interrupt()[0])) == 16)

    c = IntCodeComputer([104, 1125899906842624, 99])
    assert(c.run_no_interrupt()[0] == 1125899906842624)

    program = list(map(int, open('inputs/day9.txt').read().split(',')))

    logger.info("Running BOOST test mode")
    c = IntCodeComputer(program, [1])
    c.run_no_interrupt()
    print("BOOST Keycode", c.outputs[0])

    logger.info("Running BOOST sensor mode")
    c = IntCodeComputer(program, [2])
    c.run_no_interrupt()
    print("BOOST coordinates", c.outputs[0])
