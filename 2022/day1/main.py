from itertools import groupby


def day1(input):
    elves = [list(g) for k, g in groupby(input, key=bool) if k]

    totals = sorted(list(sum(calories) for calories in elves), reverse=True)

    print(f"Most calories: {totals[0]}")
    print(f"Top 3: {sum(totals[:3])}")


if __name__ == "__main__":

    def clean(value):
        value = value.strip()
        if not value:
            return False
        return int(value.strip())

    input = list(map(clean, open("day1/input.txt").readlines()))

    day1(input)
