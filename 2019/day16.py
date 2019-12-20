from itertools import cycle, accumulate
from collections import deque
base_pattern = [0, 1, 0, -1]


def fft(integers):
    output = []
    for i, n in enumerate(integers):
        # repeat pattern elementwise based on the postion in the list
        def pattern():
            yield from cycle(item for item in base_pattern for _ in range(i+1))

        p = pattern()
        # throw away the first one
        next(p)

        # multiply elements with pattern and sum all elements
        total = sum(x * y for x, y in zip(integers, p))

        # only keep the tens digit
        output.append(abs(total) % 10)

    return output


if __name__ == "__main__":
    string = open('inputs/day16.txt').read()
    integers = list(map(int, string))

    iterations = 100

    # x = integers
    # for _ in range(iterations):
    #     x = fft(x)
    # print("Result ", *x[:8], sep="")

    offset = int(string[:7])
    print("Offset ", offset, sep="")
    l = 10000 * len(integers) - offset
    i = cycle(reversed(integers))
    arr = [next(i) for _ in range(l)]
    # Repeatedly take the partial sums mod 10
    for _ in range(100):
        arr = [n % 10 for n in accumulate(arr)]
    print("".join(str(i) for i in arr[-1:-9:-1]))
