from utils import chunk, transpose


def parse_cards(rows):
    # each card is 5 rows with a blank divider
    # you can win on rows or cols
    rows = list(list(map(int, r.strip().split())) for r in rows[1:])
    cols = transpose(rows)
    return list(x for x in rows + cols)


input = open('day4/input.txt').readlines()

numbers_drawn = list(map(int, input[0].strip().split(',')))
cards = list(map(parse_cards, chunk(input[1:], 6)))


def win(numbers_drawn, cards):
    # start with 5 numbers cause you can't win with less
    for i in range(5, len(numbers_drawn)):
        current_nums = numbers_drawn[:i]
        for card in cards:
            for game in card:
                if set(game).issubset(set(current_nums)):
                    return card, current_nums


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


card, nums = win(numbers_drawn, cards)

# assumes there are no duplicates on a game
unmarked = set(n for g in card for n in g if n not in nums)
print("Part A:", sum(unmarked) * nums[-1])

card, nums = lose(numbers_drawn, cards)

# assumes there are no duplicates on a game
unmarked = set(n for g in card for n in g if n not in nums)
print("Part B:", sum(unmarked) * nums[-1])
