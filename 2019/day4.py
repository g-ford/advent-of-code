from itertools import groupby


def brute(min, max):
    return sum(1 for x in range(min, max+1) if is_valid(str(x)))


def is_valid(x):
    return always_increasing(x) and has_only_double(x)


def always_increasing(x):
    return all(int(x[i]) <= int(x[i+1]) for i in range(5))


def has_double(x):
    return any(x[i] == x[i+1] for i in range(5))


def has_only_double(x):
    return any(len(list(group)) == 2 for _, group in groupby(x))


if __name__ == "__main__":
    print(brute(134792, 675810))
