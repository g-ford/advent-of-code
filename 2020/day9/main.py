from itertools import permutations


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def find_error(codes, preamble, prev):
    for i in range(len(codes)):
        if i < preamble:
            continue
        perms = permutations(codes[i-prev:i], 2)
        if (not any(sum(p) == codes[i] for p in perms)):
            return i, codes[i]


input = list(map(int, open("input.txt").readlines()))

error = find_error(input, 25, 25)
print("Part 1:", error)


def find_contig(error):
    search = input[:error[0]]
    for i in range(0, len(search)):
        for j in range(i, len(search)):
            c = search[i:j]
            #print("Checking", i, j, sum(c), error[1])
            if (sum(c) == error[1]):
                print("Part 2", min(c) + max(c), (i, sum(c), error[1]))
                return


find_contig(error)
