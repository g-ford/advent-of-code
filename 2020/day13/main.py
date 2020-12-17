input = open("input.txt").readlines()

min = int(input[0])
buses = [(int(x), i) for i, x in enumerate(input[1].split(',')) if x != 'x']


def part1(start):
    next = start
    while True:
        for bus in buses:
            if next % bus[0] == 0:
                return (next - start) * bus[0]
        next += 1


def part2(buses):
    t, step = 0, 1
    for bus_id, mins in buses:
        # check to see if bus is departing at current time
        # moving forward by each step by the current lcm
        while (t + mins) % bus_id != 0:
            t += step
        # as all the buses are prime we can merely multiply to get the next lcm
        step *= bus_id
    return t


print("Part 1:", part1(min))
print("Part 2:", part2(buses))
