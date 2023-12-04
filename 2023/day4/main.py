# ❯ python -m day4.main
# [PERF] parse_game 1.235008 ms
# [PERF] part1 0.179768 ms
# Part 1: 26914
# [PERF] part2 0.329971 ms
# Part 2: 13080971
# [PERF] part2_slow 10731.673002 ms
# Part 2: 13080971


from dataclasses import dataclass

from utils import log_time


@dataclass
class Game:
    id: int
    winning: set
    played: set


def parse(line, k):
    _, nums = line.split(":")
    winning, played = nums.split("|")
    winning = set(int(n) for n in winning.split(" ") if n)
    played = set(int(n) for n in played.split(" ") if n)
    return Game(k, winning, played)


@log_time
def part1(games):
    """Calculate the points of each winning game
    Points are calculated as 1 point for the first game and doulbed for each
    successive game. So 1, 2, 4, 8, 16, ... 2 ** (number of games won - 1)"""

    def calc_game_value(g):
        won = g.winning & g.played
        if won:
            return 2 ** (len(g.winning & g.played) - 1)
        return 0

    return sum(calc_game_value(g) for g in games)


@log_time
def part2(games):
    """Count the total number of tickets scratched

    Each winning ticket wins the next n tickets in the list (from it's original
    position)"""
    counted = [[game, 1] for game in games]

    # we go through each game, and each time it wins we add the current number of
    # games to the next n games that won
    # if we have 10 copies of game 10, that matches 4 numbers
    # then we add 10 to games, 11, 12, 13, 14 as we know we have 10 more winning
    # copies of game 10 to add to it
    for current, game in enumerate(games):
        won = game.winning & game.played
        if won:
            for next in range(game.id + 1, game.id + len(won) + 1):
                counted[next][1] += counted[current][1]

    return sum(c[1] for c in counted)


@log_time
def part2_slow(games):
    """Count the total number of tickets scratched

    Each winning ticket wins the next n tickets in the list (from it's original
    position)"""
    orig = games[:]
    working = games[:]
    scratched = []

    # This was my original solution, but it's quite slow. I think I tried to solved
    # for a different case where you could win previous games so we have to  work
    # the queue rather than just suming up as the faster method does.
    while True:
        if len(working) == 0:
            break

        g = working.pop(0)
        won = len(g.winning & g.played)
        scratched.append(g)
        working = orig[g.id + 1 : g.id + won + 1] + working[:]

    return len(scratched)


@log_time
def parse_game(lines):
    return [parse(l, k) for k, l in enumerate(lines)]


lines = [l.strip() for l in open("day4/input.txt", encoding="utf8").readlines()]

games = parse_game(lines)
print("Part 1:", part1(games))
print("Part 2:", part2(games))
print("Part 2:", part2_slow(games))
