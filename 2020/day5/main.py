import string

num_rows = 128
num_seats = 8


def find_bsp(length, top, bottom, code):
    space = list(range(length))
    for c in code:
        if c == bottom:
            space = space[:len(space)//2]
        if c == top:
            space = space[len(space)//2:]
    return space[0]


def find_row(code):
    return find_bsp(num_rows, "B", "F", code)


def find_col(code):
    return find_bsp(num_seats, "R", "L", code)


def seat_id(code):
    row, col = find_row(code[:7]), find_col(code[7:])
    return (row * 8 + col, row, col)


# sanity check with examples from AoC
assert(find_bsp(num_rows, "B", "F", "BFFFBBF") == 70)
assert(find_bsp(num_rows, "B", "F", "FFFBBBF") == 14)
assert(find_bsp(num_rows, "B", "F", "BBFFBBF") == 102)
assert(find_bsp(num_seats, "R", "L", "RLR") == 5)
assert(find_bsp(num_seats, "R", "L", "RRR") == 7)
assert(find_bsp(num_seats, "R", "L", "RLL") == 4)

print("Part 1:", max(seat_id(l)[0] for l in open('input.txt').readlines()))

sorted_ids = sorted(seat_id(l) for l in open('input.txt').readlines())

for i, s in enumerate(sorted_ids):
    if (sorted_ids[i+1][0] != s[0]+1):
        print("Part 2:", s[0]+1, s, sorted_ids[i+1])
        break

# and after all this I realised it was just binary - :shrug:

print(int("BFFFBBF".replace("B", "1").replace("F", "0"), 2))
print(int("RLR".replace("R", "1").replace("L", "0"), 2))
