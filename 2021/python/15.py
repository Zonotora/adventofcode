# flake8: noqa

from python import *
import networkx as nx

aoc = AdventOfCode("2021", "15", "Chiton", newcharint)


def maze(items, m):
    g = nx.DiGraph()
    n = len(items)
    node = 0
    for ii in range(m):
        for i in range(n):
            for jj in range(m):
                for j in range(n):
                    weight = (items[i][j] + ii + jj - 1) % 9 + 1
                    g.add_node(node, weight=weight)
                    node += 1
    nodes = nx.get_node_attributes(g, 'weight')
    for node in nodes:
        for neighbour in [node + 1, node + n * m, node - 1, node - n * m]:
            if (neighbour not in nodes) or (node % (m * n) == 0 and neighbour == node - 1) or ((node + 1) % (m * n) and neighbour == n + 1):
                continue
            g.add_edge(node, neighbour, weight=nodes[node])
    path = nx.shortest_path(g, 0, n * n * m * m - 1, weight='weight')
    return sum([nodes[p] for p in path[1:]])


@aoc.part(1)
def part1(items):
    return maze(items, 1) - 1 # ?


@aoc.part(2)
def part1(items):
    return maze(items, 5)


if __name__ == "__main__":
    aoc.solve()
