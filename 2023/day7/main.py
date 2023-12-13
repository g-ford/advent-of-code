
# ❯ python -m day7.main
# [PERF] parse_input 3.356218 ms
# [PERF] part1 0.540733 ms
# Part 1:  253603890
# [PERF] parse_input2 3.251076 ms
# [PERF] part1 0.484943 ms
# Part 2:  253630098

from collections import Counter, namedtuple
from operator import attrgetter

from utils import log_time

Hand = namedtuple("Hand", ["cards", "bid", "rank"])

def hand_rank(hand, joker=None):
    cards = Counter(hand)
    jokers = cards[joker] if joker else 0
    del cards[joker]
    cards = cards.most_common()

    rank = 0 # high card

    if cards == [] and jokers == 5: # special case for all jokers
        rank = 6
    elif cards[0][1] + jokers == 5: # five of a kind
        rank = 6
    elif cards[0][1] + jokers == 4: # four of a kind
        rank = 5
    elif cards[0][1] + jokers == 3 and cards[1][1] == 2: # full house
        rank = 4
    elif cards[0][1] + jokers == 3: # three of a kind
        rank = 3
    elif cards[0][1] == 2 and cards[1][1] + jokers == 2: # two pair
        rank = 2
    elif cards[0][1] + jokers == 2: # one pair
        rank = 1
    return rank

def hand_value(hand, rank):
    return [rank.index(c) for c in hand]


@log_time
def part1(hands):
    hands = sorted(hands, key=attrgetter("rank"))
    winnings = []
    for i, h in enumerate(hands):
        winnings.append(h.bid * (i + 1))

    return sum(winnings)

@log_time
def part2(lines):
   return 0


@log_time
def parse_input(lines):
    rank = "23456789TJQKA"
    return [Hand(line[:5], int(line[5:]), (hand_rank(line[:5]), hand_value(line[:5], rank))) for line in lines]

@log_time
def parse_input2(lines):
    joker_rank = "J23456789TQKA"
    return [Hand(line[:5], int(line[5:]), (hand_rank(line[:5], joker='J'), hand_value(line[:5], joker_rank))) for line in lines]

lines = open("day7/input.txt", encoding="utf8").readlines()

print("Part 1: ", part1(parse_input(lines)))
print("Part 2: ", part1(parse_input2(lines)))
