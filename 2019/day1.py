def required_fuel(mass):
    return int(mass / 3) - 2


def fuel_calc(initial_fuel):
    fuel_on_fuel = required_fuel(initial_fuel)
    if (fuel_on_fuel) > 0:
        return fuel_on_fuel + fuel_calc(fuel_on_fuel)
    else:
        return 0


def calc(modules):
    return sum(required_fuel(int(x)) for x in modules)


def calc_with_fuel(modules):
    return sum(fuel_calc(int(x)) for x in modules)


if __name__ == "__main__":
    # part one samples
    assert(required_fuel(12) == 2)
    assert(required_fuel(14) == 2)
    assert(required_fuel(1969) == 654)
    assert(required_fuel(100756) == 33583)

    # part two samples
    assert(fuel_calc(14) == 2)
    assert(fuel_calc(1969) == 966)
    assert(fuel_calc(100756) == 50346)

    modules = open('day1.txt').readlines()
    print("initial fuel", calc(modules))
    print('inc fuel', calc_with_fuel(modules))
