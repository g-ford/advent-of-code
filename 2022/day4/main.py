def day4(input):
    contained = 0
    overlap = 0
    for pair in input:
        a = set(range(*pair[0]))
        b = set(range(*pair[1]))

        intersect = a.intersection(b)
        if intersect == a or intersect == b:
            contained += 1
        if len(intersect) > 0:
            overlap += 1

    print(f"Contained: {contained}")
    print(f"Overlap: {overlap}")


if __name__ == "__main__":

    def clean(value):
        a, b = value.strip().split(",")
        min_a, max_a = map(int, a.split("-"))
        min_b, max_b = map(int, b.split("-"))
        return (min_a, max_a + 1), (min_b, max_b + 1)  # so range works as inclusive

    input = list(map(clean, open("day4/input.txt").readlines()))

    day4(input)
