# ❯ python -m day2.main
# [PERF] parse_games 0.468016 ms
# [PERF] part1 0.051737 ms
# Part 1: 2685
# [PERF] part2 0.252008 ms
# Part 2: 83707

import math

from utils import log_time


@log_time
def part1(games, max_colours):
    """Find which games are possible given the max colours
    Return the sum of the game ids that are possible"""

    impossible = []
    for game, rounds in games:
        for n, color in rounds:
            if n > max_colours[color]:
                impossible.append(game)
                break
    # Maybe  not the best way to get this but I tested accumulating
    # impossible and possible count with `+=` and it was roughly equivalant
    # within 0.001 ms so 🤷
    return sum(g for g, _ in games) - sum(impossible)


@log_time
def part2(games):
    """Calculate the total power of all games

    The power of a game is the product of the minimum number of each color that
    would satisfy all rounds

    Total power is the sum of the power of all games
    """
    powers = []
    for game_id, rounds in games:
        min_colors = {}
        for n, color in rounds:
            min_colors[color] = max(min_colors.get(color, 0), n)
        powers.append((game_id, min_colors))
    return sum(math.prod(v for v in min_colors.values()) for _, min_colors in powers)


@log_time
def parse_games(lines):
    """Convert lines to a list of games"""
    return [to_game(line.strip()) for line in lines]


def to_game(line):
    """Convert line to a Game of rounds"""
    game, rounds = line.split(":")
    game = int(game.replace("Game ", ""))

    rounds = rounds.split(";")
    r = []
    for round in rounds:
        shown = round.split(",")
        for show in shown:
            # Each round starts with a space, int, space, color name
            # So split on space and discard the first empty option
            _, n, color = show.split(" ")
            r.append((int(n), color))
    return (game, r)


lines = open("day2/input.txt", encoding="utf8").readlines()
games = parse_games(lines)

print("Part 1:", part1(games, {"red": 12, "green": 13, "blue": 14}))
print("Part 2:", part2(games))
