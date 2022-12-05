def chunk(seq, n):
    for i in range(0, len(seq), n):
        yield seq[i : i + n]


def priority(char):
    p = ord(char) - ord("a") + 1
    if p < 1:
        # this is an uppercase
        # which is lower than lowercase in the ord
        return ord(char) - ord("A") + 26 + 1
    return p


def find_common_item(row):
    # split row in two
    a = set(row[: len(row) // 2])
    b = set(row[len(row) // 2 :])
    return a.intersection(b).pop()  # should only be one


def find_badge(group):
    result = set(group[0]).intersection(*group[1:])
    return result.pop()


def day3(input):
    commons = list(find_common_item(row) for row in input)
    total = sum(map(priority, commons))
    print(f"Part 1: {total}")

    badges = list(find_badge(group) for group in chunk(input, 3))
    total = sum(map(priority, badges))
    print(f"Part 2: {total}")


if __name__ == "__main__":

    def clean(value):
        return value.strip()

    input = list(map(clean, open("day3/input.txt").readlines()))

    day3(input)
