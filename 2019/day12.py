from operator import add
from itertools import permutations
from math import gcd
from functools import reduce
import time


class Moon():
    def __init__(self, position, velocity=(0, 0, 0)):
        self.position = position
        self.velocity = velocity

    def gravity_influence(self, other_moons):
        for m in other_moons:
            if m != self:
                self.velocity = add_tuples(
                    self.velocity,
                    gravity(self.position, m.position))

    def update_postion(self):
        self.position = add_tuples(self.position, self.velocity)

    def __repr__(self):
        return f"pos = <x ={self.position[0]:>3}, y ={self.position[1]:>3}, z ={self.position[2]:>3}>, " + \
               f"vel = <x ={self.velocity[0]:>3}, y ={self.velocity[1]:>3}, z ={self.velocity[2]:>3}>\n"


def gravity_p(a, b):
    if a == b:
        return 0
    if a < b:
        return 1
    else:
        return -1


def gravity(a, b):
    return (gravity_p(a[0], b[0]),
            gravity_p(a[1], b[1]),
            gravity_p(a[2], b[2]))


def add_tuples(p, v):
    return tuple(map(add, p, v))


def step(moons):
    for m in moons:
        m.gravity_influence(moons)
    for m in moons:
        m.update_postion()
    return moons


def energy(moons):
    total = 0
    for m in moons:
        pot = sum(map(abs, m.position))
        kin = sum(map(abs, m.velocity))
        total += (pot * kin)
    return total


def axis_period(moons, axis):
    # store the initial state of all moons position on axis
    # the assumption here is that the initial state will be the period boundary
    initial_p = [m.position[axis] for m in moons]
    initial_v = [m.velocity[axis] for m in moons]
    counter = 0
    while True:
        moons = step(moons)
        counter += 1
        if [m.position[axis] for m in moons] == initial_p and [m.velocity[axis] for m in moons] == initial_v:
            return counter


def lcms(numbers):
    return reduce(lcm, numbers)


def lcm(a, b):
    return (a * b) // gcd(a, b)


if __name__ == "__main__":
    moons = [
        Moon((-1, 0, 2), (0, 0, 0)),
        Moon((2, -10, -7), (0, 0, 0)),
        Moon((4, -8, 8), (0, 0, 0)),
        Moon((3, 5, -1), (0, 0, 0))
    ]

    for _ in range(10):
        moons = step(moons)
    assert(energy(moons) == 179)

    periods = [axis_period(moons, i) for i in range(3)]
    assert(lcms(periods) == 2772)

    # didn't bother with parsing the input this time
    # just hand encoded the values
    moons = [
        Moon((6, -2, -7), (0, 0, 0)),
        Moon((-6, -7, -4), (0, 0, 0)),
        Moon((-9, 11, 0), (0, 0, 0)),
        Moon((-3, -4, 6), (0, 0, 0))
    ]
    m2 = moons.copy()

    # part 1
    for _ in range(1000):
        moons = step(moons)
    print("Energy after 1000", energy(moons))

    # part 2
    # people smarter than me figured out the axis and lcm approach
    periods = [axis_period(m2, i) for i in range(3)]
    print("Period", lcms(periods))
