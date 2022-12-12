from dataclasses import dataclass


@dataclass
class Node:
    name: str
    type: str
    size: int
    children: list
    parent: None


def calc_size(node: Node):
    if node.type == 'file':
        return node.size or 0
    if len(node.children) > 0:
        node.size = sum(map(calc_size, node.children))
    return node.size


def part1(node: Node, acc=0):
    if node.type == "file":
        return 0
    if len(node.children) > 0:
        acc += sum([part1(c) for c in node.children])
    if node.type == 'dir' and node.size <= 100000:
        return acc + node.size

    return acc


def part2(node):
    total = 70000000
    space = 30000000
    required = space - (total - node.size)
    print("Required:", required)

    def candidate(node, acc=[]):
        if node.type == 'dir' and node.size >= required:
            acc.append(node.size)

        if len(node.children) > 0:
            [candidate(c, acc) for c in node.children]

        return acc

    dirs = candidate(node)
    return sorted(dirs)[0]


def day7_2(input):
    current_node = Node(name='/', type="dir", children=[], size=0, parent=None)
    root_node = current_node
    for command in input[1:]:
        if command.startswith("$ cd "):
            new_dir = command.replace("$ cd ", "")
            if new_dir == "..":
                current_node = current_node.parent
                continue
            new_node = Node(name=new_dir, type="dir", size=0, children=[], parent=current_node)
            current_node.children.append(new_node)
            current_node = new_node

        if command[0].isdigit():
            size, name = command.split()
            current_node.children.append(Node(name=name, type="file", children=[], size=int(size), parent=current_node))

    calc_size(root_node)
    print("Part1: ", part1(root_node))
    print("Part2: ", part2(root_node))


if __name__ == "__main__":

    def clean(value):
        return value.strip()

    input = list(map(clean, open("day7/input.txt").readlines()))

    day7_2(input)
