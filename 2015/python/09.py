# flake8: noqa

from python import *
from itertools import permutations
from collections import defaultdict
import numpy as np
import sys

aoc = AdventOfCode("2021", "09", "", new)


def compute(items, shortest):
    edges = []
    for line in items:
        parts = line.split()
        edge = Edge(parts[0], parts[2], int(parts[4]))
        edges.append(edge)

    g = Graph(edges)
    vertices = g.vertices
    mapping = {v: i for i, v in enumerate(vertices)}
    adj = g.adj
    perm = permutations(vertices)

    total_dist = sys.maxsize if shortest else 0
    for p in perm:
        dist = 0
        prev = p[0]
        for c in p[1:]:
            f = mapping[prev]
            t = mapping[c]
            dist += adj[f][t]
            prev = c

        total_dist = min(total_dist, dist) if shortest else max(total_dist, dist)
    return total_dist


@aoc.part(1)
def part1(items):
    return compute(items, True)


@aoc.part(2)
def part2(items):
    return compute(items, False)


if __name__ == "__main__":
    aoc.solve()
