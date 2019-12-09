from collections.abc import Iterable


def flatten(l):
    for el in l:
        if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el


def find_path(a, b, dag, path=None):
    """ Blatently 'borrowed' from https://www.python-course.eu/graphs_python.php """
    if path == None:
        path = []
    path = path + [a]
    if a == b:
        return path
    if a not in dag:
        return None
    for vertex in dag[a]:
        if vertex not in path:
            extended_path = find_path(vertex,
                                      b,
                                      dag,
                                      path)
            if extended_path:
                return extended_path
    return None


def find_all_paths(dag):
    paths = [find_path('COM', x, dag) for x in dag.keys()]
    return len(list(x for x in flatten(paths) if x != 'COM'))


def create_paths(inputs):
    """Create an adjancency list of orbitor -> orbitee

    With the restriction that each object only orbits one other, this could/should
    have been a simple map, which might have made things easier
    """
    objects = {}
    for line in inputs:
        try:
            a, b = line.split(')')
            objects.setdefault(a, []).append(b)
            objects.setdefault(b, [])
        except:
            print(line)
    return objects


def transfers(dag, x, y):
    """Find the number of transfers between two objects

    Finds the number of unique bodies between the two paths and counts them as transfers."""
    a = set(find_path('COM', x, dag))
    b = set(find_path('COM', y, dag))

    diff = b.symmetric_difference(a)
    return len(diff) - 2


if __name__ == "__main__":
    test_dag = create_paths("""COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
""".splitlines())
    assert(find_all_paths(test_dag) == 42)
    test_dag = create_paths("""COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN
""".splitlines())
    assert(transfers(test_dag, "SAN", "YOU") == 4)

    inputs = open('inputs/day6.txt').read().splitlines()
    dag = create_paths(inputs)

    print("Total Orbits", find_all_paths(dag))
    print("SAN-YOU", transfers(dag, 'YOU', 'SAN'))
