# flake8: noqa

from python import *
import sys
import numpy as np
from collections import defaultdict, deque
import string
import re

aoc = AdventOfCode("2022", "12", "", new)

elevation = {c: v for v, c in enumerate(string.ascii_lowercase)}
elevation = {"S": 0, "E": elevation["z"], **elevation}


def end(items):
    for i in range(len(items)):
        for j in range(len(items[i])):
            if items[i][j] == "E":
                return i, j


def parse(items):
    e = end(items)
    q = deque()
    q.append(e)
    dist = [[sys.maxsize for _ in range(len(items[i]))] for i in range(len(items))]
    dist[e[0]][e[1]] = 0
    seen = set([e])

    while len(q) > 0:
        i, j = q.popleft()
        ns = vhneighbours(items, i, j)
        for x, y in ns:
            current = items[i][j]
            neighbor = items[y][x]
            if (y, x) not in seen and elevation[current] <= elevation[neighbor] + 1:
                dist[y][x] = dist[i][j] + 1
                q.append((y, x))
                seen.add((y, x))
    return dist


@aoc.part(1)
def part1(items):
    dist = parse(items)
    for i in range(len(items)):
        for j in range(len(items[i])):
            if items[i][j] == "S":
                return dist[i][j]


@aoc.part(2)
def part2(items):
    dist = parse(items)
    best = sys.maxsize
    for i in range(len(items)):
        for j in range(len(items[i])):
            if items[i][j] == "a":
                best = min(best, dist[i][j])
    return best


if __name__ == "__main__":
    aoc.solve()
