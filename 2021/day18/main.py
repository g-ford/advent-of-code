from utils import log_time
from itertools import permutations


class Num:
    def __init__(self, left=None, right=None, parent=None, value=None):
        self.left = left
        self.right = right
        self.value = value
        self.parent = parent

    def __repr__(self) -> str:
        if self.right is None and self.left is None:
            return str(self.value)

        return f'[{self.left},{self.right}]'

    def magnitude(self):
        if self.value is not None:
            return self.value

        return 3 * self.left.magnitude() + 2 * self.right.magnitude()

    def reduce(self):
        while self._explode() or self._split():
            continue

    def _split(self):
        if self.value and self.value >= 10:
            v = self.value
            self.left = Num(parent=self, value=v // 2)
            self.right = Num(parent=self, value=(v + 1) // 2)
            self.value = None
            return True

        if self.left is not None:
            s = self.left._split()
            if s:
                return True

        if self.right is not None:
            s = self.right._split()
            if s:
                return True

        return False

    def _explode(self):
        def ex(node, depth=4):
            if depth == 0 and node.value == None:
                return node

            if node.left is not None:
                l = ex(node.left, depth - 1)
                if l:
                    return l

            if node.right is not None:
                r = ex(node.right, depth - 1)
                if r:
                    return r

        e = ex(self)
        if e is not None:
            l = e._next_left()
            r = e._next_right()

            if l is not None:
                l.value += e.left.value

            if r is not None:
                r.value += e.right.value

            e.left = None
            e.right = None
            e.value = 0
            return True
        return False

    def _next_left(self):
        if self.parent is None:
            return None

        if self == self.parent.left:
            return self.parent._next_left()

        n1 = self.parent.left
        while n1.right is not None:
            n1 = n1.right
        return n1

    def _next_right(self):
        if self.parent is None:
            return None

        if self == self.parent.right:
            return self.parent._next_right()

        n1 = self.parent.right
        while n1.left is not None:
            n1 = n1.left
        return n1

    def __add__(self, right):
        r = Num(left=self, right=right)
        self.parent = r
        right.parent = r
        r.reduce()
        return r


def string_to_tree(string):
    def parse_string(string):
        if string[0] != '[':
            return Num(value=int(string))

        b = 0
        for i in range(1, len(string)):
            if string[i] == '[':
                b += 1
            elif string[i] == ']' or b == 0:
                b -= 1
                if b <= 0:
                    return Num(left=parse_string(string[1:i+1]), right=parse_string(string[i+2:-1]))

    def reparent(num):
        while num.left != None and num.left.parent == None:
            num.left.parent = num
            reparent(num.left)
        while num.right != None and num.right.parent == None:
            num.right.parent = num
            reparent(num.right)

    tree = parse_string(string)
    reparent(tree)
    return tree


@ log_time
def part_a(input):
    r = string_to_tree(input[0])
    for l in input[1:]:
        r = r + string_to_tree(l)
    return r.magnitude()


@ log_time
def part_b(input):
    mags = [(string_to_tree(a) + string_to_tree(b)).magnitude()
            for a, b in permutations(input, 2)]
    return max(mags)


input = [l.strip() for l in open('day18/input.txt').readlines()]

result_a = part_a(input)
result_b = part_b(input)
print("Part A:", result_a)
print("Part B:", result_b)
