from math import ceil
from collections import defaultdict


def parse_reactions(inp):
    "I'm sure there is a more 'elegant' way to do this with regex but then I would have two problems"
    reactions = {}
    for line in inp.splitlines():
        left, right = line.split(' => ')

        l_parts = left.split(", ")
        parsed_left = []
        for p in l_parts:
            q, el = p.split(' ')
            parsed_left.append((int(q), el))

        rq, rel = right.split(' ')
        reactions[rel] = (int(rq), parsed_left)
    return reactions


def ore(el, q, reactions):
    requirements = {el: q}
    to_produce = [el]

    while to_produce:
        for e in to_produce:
            quantity, subel = reactions[e]
            multiplier = ceil(requirements[e] / quantity)

            for q1, e1 in subel:
                requirements[e1] = requirements.get(e1, 0) + (multiplier * q1)

            requirements[e] -= multiplier * quantity
        to_produce = [
            e for e in requirements if requirements[e] > 0 and e != "ORE"]

    return requirements['ORE']


if __name__ == "__main__":
    reactions = parse_reactions("""10 ORE => 10 A
1 ORE => 1 B
7 A, 1 B => 1 C
7 A, 1 C => 1 D
7 A, 1 D => 1 E
7 A, 1 E => 1 FUEL""")

    assert(ore("FUEL", 1, reactions) == 31)

    reactions = parse_reactions("""9 ORE => 2 A
8 ORE => 3 B
7 ORE => 5 C
3 A, 4 B => 1 AB
5 B, 7 C => 1 BC
4 C, 1 A => 1 CA
2 AB, 3 BC, 4 CA => 1 FUEL""")

    assert(ore("FUEL", 1, reactions) == 165)

    reactions = parse_reactions("""157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT""")

    assert(ore("FUEL", 1, reactions) == 13312)

    reactions = parse_reactions(open('inputs/day14.txt').read())
    ore_per_fuel = ore("FUEL", 1, reactions)
    print("ORE per FUEL:", ore("FUEL", 1, reactions))

    # because some elements are over-produced we can't just use this as the answer
    low = 1e12 // ore_per_fuel  # we now we can produce at least his much
    high = low * 2  # educated guess
    loops = 0
    while high - low > 1:
        loops += 1
        mid = (high + low) // 2
        if ore("FUEL", mid, reactions) <= 1e12:
            low = mid
        else:
            high = mid

    print("Fuel from 1e12 ORE:", low, f"(Took {loops} loops)")
    print(
        f"That's an extra {low - (1e12 // ore_per_fuel)} from the left overs")
