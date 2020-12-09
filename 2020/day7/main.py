
import networkx as nx
import re

rules = open('input.txt').readlines()
dag = nx.DiGraph()

print("Rule count:", len(rules))

for r in rules:
    n1 = re.search("(.*?) bags contain", r).groups()[0]
    n2 = re.findall("(\d)\s(.*?) bags?[\.,]", r)
    for n in n2:
        dag.add_weighted_edges_from([(n1, n[1], int(n[0]))])

pre = list(nx.algorithms.dag.ancestors(dag, "shiny gold"))
print("Part 1:", len(pre))

inside = list(nx.dfs_postorder_nodes(
    dag, "shiny gold"))

for node in inside:
    dag.nodes[node]["weight"] = sum(
        (dag.nodes[n]["weight"] + 1) * v["weight"] for (n, v) in dag[node].items())


print("Part 2:", dag.nodes["shiny gold"]["weight"])
