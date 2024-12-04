from utils import log_time, rotate_matrix_45_degress, transpose


@log_time
def part1(parts):
    total = sum(s.count("XMAS") for s in parts)
    total += sum(s.count("SAMX") for s in parts)

    transposed = transpose(parts[:])
    total += sum("".join(s).count("XMAS") for s in transposed)
    total += sum("".join(s).count("SAMX") for s in transposed)

    diagsA = rotate_matrix_45_degress(parts[:])

    total += sum(s.count("XMAS") for s in diagsA)
    total += sum(s.count("SAMX") for s in diagsA)

    diagsB = rotate_matrix_45_degress(list(reversed(parts[:])))

    total += sum(s.count("XMAS") for s in diagsB)
    total += sum(s.count("SAMX") for s in diagsB)

    return total


@log_time
def part2(parts):
    count = 0

    # M.M  M.S  S.M  S.S
    # .A.  .A.  .A.  .A.
    # S.S  M.S  S.M  M.M
    valid = ["MMSS", "MSMS", "SSMM", "SMSM"]

    for i in range(1, len(parts)-1):
        for j in range(1, len(parts[0])-1):
            if parts[i][j] == "A":
                corners = parts[i-1][j-1] + parts[i-1][j+1] + parts[i+1][j-1] + parts[i+1][j+1]
                if corners in valid:
                    count += 1
    return count



@log_time
def parse_input(lines):
    return lines.split("\n")


lines = open("day04/input.txt", encoding="utf8").read()

parts = parse_input(lines)

print("Part 1: ", part1(parts))
print("Part 2: ", part2(parts))
