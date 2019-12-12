from itertools import zip_longest
from collections import Counter

if __name__ == "__main__":
    res = (25, 6)
    layer_size = res[0] * res[1]

    pixels = open('inputs/day8.txt').read().strip()
    pixels = list(int(p) for p in pixels)

    layers = zip(*[iter(pixels)] * layer_size)

    counters = [Counter(l) for l in layers]

    min0 = min(counters, key=lambda x: x[0])
    print("Part 1:", min0[1] * min0[2])

    # reset zip iterator
    layers = zip(*[iter(pixels)] * layer_size)
    image = [2] * layer_size
    for l in layers:
        for i, p in enumerate(l):
            if image[i] == 2:  # transparent
                image[i] = p

    rows = zip(*[iter(image)] * res[0])
    for r in rows:
        for p in r:
            if p == 1:
                print('⬜', end='')
            else:
                print(' ', end='')
        print('')
