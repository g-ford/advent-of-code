LOSE = 0
DRAW = 3
WIN = 6


ROCK = 1
PAPER = 2
SCISSORS = 3


def calc_round_p1(opp, me):
    if opp == me:
        return DRAW + me

    if opp == ROCK and me == PAPER:
        return WIN + me
    if opp == PAPER and me == SCISSORS:
        return WIN + me
    if opp == SCISSORS and me == ROCK:
        return WIN + me

    return LOSE + me


def calc_round_p2(opp, me):
    SHOULD_LOSE = 1
    SHOULD_DRAW = 2
    SHOULD_WIN = 3

    if me == SHOULD_DRAW:
        return DRAW + opp

    if me == SHOULD_WIN:
        if opp == ROCK:
            return WIN + PAPER
        if opp == PAPER:
            return WIN + SCISSORS
        if opp == SCISSORS:
            return WIN + ROCK

    if me == SHOULD_LOSE:
        if opp == ROCK:
            return LOSE + SCISSORS
        if opp == PAPER:
            return LOSE + ROCK
        if opp == SCISSORS:
            return LOSE + PAPER


def day2(rounds):
    results = list(calc_round_p1(opp, me) for (opp, me) in rounds)
    print(f"Total score p1: {sum(results)}")

    results = list(calc_round_p2(opp, me) for (opp, me) in rounds)
    print(f"Total score p2: {sum(results)}")


if __name__ == "__main__":

    def clean(value):
        opponent = ROCK
        me = ROCK

        if value[0] == "B":
            opponent = PAPER
        if value[0] == "C":
            opponent = SCISSORS

        if value[2] == "Y":
            me = PAPER
        if value[2] == "Z":
            me = SCISSORS

        return (opponent, me)

    input = list(map(clean, open("day2/input.txt").readlines()))

    day2(input)
