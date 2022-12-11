
def day6(input, length):
    x = length - 1
    max = len(input)
    while x < max:
        signal = input[x-length:x]
        if len(set(signal)) == length:
            print(f'Found signal {signal} at {x}')
            return
        x += 1
    print("No signal found")


if __name__ == "__main__":

    def clean(value):
        return value.strip()

    input = list(map(clean, open("day6/input.txt").readlines()))

    day6(input[0], 4)
    day6(input[0], 14)
