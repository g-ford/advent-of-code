from utils import log_time

input = list(map(int, open('day6/input.txt').readlines()[0].split(',')))


@log_time
def run_sim(fish, days):
    for _ in range(days):
        new_fish = []
        babies = 0
        for f in fish:
            if f == 0:
                new_fish.append(6)
                babies += 1
            else:
                new_fish.append(f - 1)
        fish = new_fish + ([8] * babies)
    return len(fish)


@log_time
def run_sim2(fish, days):
    ages = [0] * 9

    # Initial state
    for f in fish:
        ages[f] += 1

    for _ in range(days):
        ages = ages[1:] + ages[:1]
        ages[6] += ages[8]

    return sum(ages)


result_a = run_sim(input, 80)
result_b = run_sim2(input, 256)
print("Part A:", result_a)
print("Part B:", result_b)
