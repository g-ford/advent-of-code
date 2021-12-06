from utils import chunk, transpose, log_time


def parse_cards(rows):
    # each card is 5 rows with a blank divider
    # you can win on rows or cols
    rows = list(list(map(int, r.strip().split())) for r in rows[1:])
    cols = transpose(rows)
    return list(x for x in rows + cols)


@log_time
def win(numbers_drawn, cards):
    # start with 5 numbers cause you can't win with less
    for i in range(5, len(numbers_drawn)):
        current_nums = numbers_drawn[:i]
        for card in cards:
            for game in card:
                if set(game).issubset(set(current_nums)):
                    return card, current_nums


@log_time
def lose(numbers_drawn, cards):
    loser = ()
    winners = []
    for i in range(5, len(numbers_drawn)):
        current_nums = numbers_drawn[:i]
        for card in cards:
            if card not in winners:
                for game in card:
                    if set(game).issubset(set(current_nums)):
                        loser = card, current_nums
                        winners.append(card)
    return loser


@log_time
def calc_score(result):
    card, nums = result
    unmarked = set(n for g in card for n in g if n not in nums)
    return sum(unmarked) * nums[-1]


input = open('day4/input.txt').readlines()

numbers_drawn = list(map(int, input[0].strip().split(',')))
cards = list(map(parse_cards, chunk(input[1:], 6)))

result_a = calc_score(win(numbers_drawn, cards))
result_b = calc_score(lose(numbers_drawn, cards))
print("Part A:", result_a)
print("Part B:", result_b)
