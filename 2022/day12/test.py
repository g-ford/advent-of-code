import networkx as nx
import numpy as np

def tuple_add(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])

with open('day12/input.txt') as f:
    height_map = np.array([[ord(x) for x in line.strip()] for line in f.readlines()]).astype(np.byte)

start = tuple(np.argwhere(height_map == ord('S'))[0])
end = tuple(np.argwhere(height_map == ord('E'))[0])
# replace start and end
height_map[start] = ord('a')
height_map[end] = ord('z')
all_elements = {tuple(x) for x in np.transpose(height_map.nonzero())}
all_directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

G = nx.DiGraph()

for e in all_elements:
    current_height = height_map[e]
    for d in all_directions:
        test_location = tuple_add(e, d)
        if test_location in all_elements and height_map[test_location] - current_height <= 1:
            G.add_edge(e, test_location)

print(G)
r1 = nx.shortest_path_length(G, start, end)
print(r1)


r2 = min((l, n) for n, l in nx.single_target_shortest_path_length(G, end) if height_map[n] == ord('a'))
print(r2)
