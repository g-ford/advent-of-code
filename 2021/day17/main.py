from utils import log_time
import re


@ log_time
def part_a(x_min, x_max, y_min, y_max):
    # I am sure there is way to calculate this, but let's do it the fun way :)

    def simulate(x, y):
        tx, ty = (0, 0)
        max_ty = 0

        while True:
            tx += x
            ty += y
            x = max(0, x-1)
            y -= 1
            max_ty = max(max_ty, ty)

            if x_min <= tx <= x_max and y_min <= ty <= y_max:
                # hit the target
                return max_ty
            if tx > x_max or ty < y_min:
                return None  # failed to hit the target area

    sims = []
    # best guess for range - can't be faster than x_max otherwise we overshoot on the first step
    # can't be faster than y_min otherwise we will overshoot once we get back to y=0 because whatever speed
    # we go up, we must come down at that speed
    for x in range(x_max, 0, -1):
        for y in range(abs(y_min), y_min - 1, -1):
            s = simulate(x, y)
            if s is not None:
                sims.append(s)
    return (max(sims), len(sims))


input = open('day17/input.txt').read()
m = re.search("x=(\d*?)..(\d*?), y=(-?\d+?)..(-?\d+)$", input)
x_min = int(m.group(1))
x_max = int(m.group(2))
y_min = int(m.group(3))
y_max = int(m.group(4))

result_a, result_b = part_a(x_min, x_max, y_min, y_max)

print("Part A:", result_a)
print("Part B:", result_b)
