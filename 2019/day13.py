
from intcode import IntCodeComputer, OutputInterrupt, InputInterrupt
from collections import Counter

tiles_icons = {
    0: " ",
    1: "🧱",
    2: "📦",
    3: "🏓",
    4: "🎾"
}


def cmp(a, b):
    return (a > b)-(a < b)


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def render(tiles):
    max_x = max(tiles.keys(), key=lambda x: x[1])[1]+1
    max_y = max(tiles.keys(), key=lambda x: x[0])[0]+1
    print("Score:", tiles[(0, -1)])
    for y in range(max_y):
        for x in range(max_x):
            print(tiles_icons[tiles[(y, x)]], end="")
        print()


def play(c, show=False):
    paddle_pos = [0, 0]
    ball_pos = [0, 0]
    score = 0
    tiles = {}
    while not c.HALTED:
        try:
            c.run()
        except OutputInterrupt:
            if len(c.outputs) < 3:
                continue
            tile = c.outputs
            c.outputs = []
            tiles[(tile[1], tile[0])] = tile[2]

            if tile[0] == -1:
                score = tile[2]
            if tile[2] == 4:
                ball_pos = tile[-3:]
            if tile[2] == 3:
                paddle_pos = tile[:2]
        except InputInterrupt:
            if show:
                render(tiles)
            c.inputs.append(cmp(ball_pos[0], paddle_pos[0]))

    return score


if __name__ == "__main__":
    program = list(map(int, open('inputs/day13.txt').read().split(',')))

    c = IntCodeComputer(program)

    # part 1
    output = list(chunks(c.run_no_interrupt(), 3))
    tile_counts = Counter([x[2] for x in output])
    print(", ".join(f"{tiles_icons[k]} : {v}" for k, v in tile_counts.items()))

    free_play = [2] + program[1:]
    c = IntCodeComputer(free_play)

    score = play(c)
    print("Final Score: ", score)
