from utils import log_time


@ log_time
def part_a(input):
    points = {
        ")": 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    score = []
    for row in input:
        st = []
        for c in row.strip():
            if c == '(':
                st.append(')')
            elif c == '{':
                st.append('}')
            elif c == '[':
                st.append(']')
            elif c == '<':
                st.append('>')
            else:
                x = st.pop()
                if c != x:
                    score += [points[c]]
                    break
    return sum(score)


@ log_time
def part_b(input):
    points = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
    }

    scores = []
    for row in input:
        valid = True
        st = []
        score = 0
        for c in row.strip():
            if c == '(':
                st.append(')')
            elif c == '{':
                st.append('}')
            elif c == '[':
                st.append(']')
            elif c == '<':
                st.append('>')
            else:
                x = st.pop()
                if c != x:
                    valid = False
                    break

        if valid:
            for a in st[::-1]:
                score *= 5
                score += points[a]
            scores.append(score)

    return sorted(scores)[(len(scores)) // 2]


input = list(open('day10/input.txt').readlines())

result_a = part_a(input)
result_b = part_b(input)
print("Part A:", result_a)
print("Part B:", result_b)
