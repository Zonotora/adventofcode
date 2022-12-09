# flake8: noqa

from python import *
import sys
import numpy as np
from collections import defaultdict
import re

aoc = AdventOfCode("2022", "09", "Rope Bridge", new)


def update(h, t):
    p = h - t
    if abs(p.x) <= 1 and abs(p.y) <= 1:
        # ok
        return t
    x, y = h.x, h.y
    if abs(p.x) >= 2:
        x = h.x - 1 if h.x > t.x else h.x + 1
    if abs(p.y) >= 2:
        y = h.y - 1 if h.y > t.y else h.y + 1
    return Point(x, y)


def compute(items, n):
    rope = [Point(0, 0) for _ in range(n)]
    dir = {"R": Point(1, 0), "U": Point(0, 1), "L": Point(-1, 0), "D": Point(0, -1)}
    pos = set()
    for line in items:
        d, v = line.split()
        for _ in range(int(v)):
            rope[0] += dir[d]
            for i in range(1, n):
                rope[i] = update(rope[i - 1], rope[i])
            pos.add((rope[-1].x, rope[-1].y))

    return len(pos)


@aoc.part(1)
def part1(items):
    return compute(items, 2)


@aoc.part(2)
def part2(items):
    return compute(items, 10)


if __name__ == "__main__":
    aoc.solve()
