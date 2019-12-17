from intcode import IntCodeComputer, InputInterrupt, OutputInterrupt
from collections import defaultdict, deque
from operator import add


def paint(program, start_color):
    state = defaultdict(int)
    state[(0, 0)] = start_color
    c = IntCodeComputer(program=program)
    current_pos = (0, 0)
    heading = deque([(1, 0), (0, 1), (-1, 0), (0, -1)])

    while not c.HALTED:
        try:
            c.run()
        except InputInterrupt:
            c.inputs.append(state[current_pos])
        except OutputInterrupt:
            if len(c.outputs) < 2:
                continue
            paint, turn = c.outputs
            c.outputs = []
            state[current_pos] = paint
            if turn == 0:
                heading.rotate(-1)
            else:
                heading.rotate()
            current_pos = tuple(map(add, current_pos, heading[0]))
    return state


def visualise(state):
    xs = [x[0] for x in state.keys()]
    ys = [x[1] for x in state.keys()]

    for x in range(min(xs), max(xs)+1):
        for y in range(min(ys), max(ys)+1):
            if state[(x, y)] == 1:
                print('⬜', end='')
            else:
                print(' ', end='')
        print('')


if __name__ == "__main__":
    program = list(map(int, open('inputs/day11.txt').read().split(',')))

    state = paint(program, 0)
    print("Painted", len(state.keys()))

    # For me, this comes out upside down
    # I think I have my headings and rotations right...?
    visualise(paint(program, 1))
