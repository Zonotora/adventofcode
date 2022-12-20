# flake8: noqa

from python import *
import sys
import numpy as np
from collections import defaultdict
import re

aoc = AdventOfCode("2022", "17", "", identity)

# rocks = [["####"], [" # ", "###", " # "], ["  #", "  #", "###"], ["#", "#", "#", "#"], ["##", "##"]]

rocks = [
    [Point(0, 0), Point(1, 0), Point(2, 0), Point(3, 0)],
    [Point(1, 2), Point(0, 1), Point(1, 1), Point(2, 1), Point(1, 0)],
    [Point(2, 2), Point(2, 1), Point(0, 0), Point(1, 0), Point(2, 0)],
    [Point(0, 3), Point(0, 2), Point(0, 1), Point(0, 0)],
    [Point(0, 1), Point(1, 1), Point(0, 0), Point(1, 0)],
]


class Rock:
    def __init__(self, p, index) -> None:
        self.shape = rocks[index]
        self.p = p
        self.colliding = False

    def __str__(self) -> str:
        return f"{self.shape}"

    def move(self, rocks: set[Point], other: Point):
        p = self.p + other
        if other.y == 0:
            for s in self.shape:
                s = Point(p.x + s.x, p.y + s.y)
                if s.x < 0 or s.x > 6 or s in rocks:
                    return None
        else:
            for s in self.shape:
                s = Point(p.x + s.x, p.y + s.y)
                if s.y <= 0 or s in rocks:
                    self.colliding = True

                    for s in self.shape:
                        s = Point(self.p.x + s.x, self.p.y + s.y)
                        rocks.add(s)
                    t = max(rocks, key=lambda x: x.y)
                    return t.y
        self.p = p


def print_rocks(rocks):
    y1 = 0
    y2 = max(rocks, key=lambda r: r.y).y if len(rocks) > 0 else 0

    S = [[0 for _ in range(9)] for _ in range(y2 - y1 + 1)]

    for r in rocks:
        S[r.y][r.x] = 1

    s_tot = []
    for i in range(y2 - y1 + 1):
        s = ""
        for j in range(-1, 8):
            if i == 0 and (j == -1 or j == 7):
                s += "+"
            elif i == 0:
                s += "-"
            elif j == -1 or j == 7:
                s += "|"
            elif S[i][j] == 1:
                s += "#"
            else:
                s += "."
        s_tot.append(s)
    s_tot.reverse()
    print("\n".join(s_tot))


def signature(rocks, y):
    return frozenset(map(lambda r: (r.x, y - r.y), filter(lambda r: y - r.y <= 30, rocks)))


@aoc.part(1)
def part1(items):
    air = 0
    i = 0
    rocks = set()
    y = 0
    for i in range(2022):
        r = Rock(Point(2, y + 4), i % 5)
        while not r.colliding:
            a = items[air % len(items)]
            if a == "<":
                r.move(rocks, Point(-1, 0))
            else:
                r.move(rocks, Point(1, 0))
            new_y = r.move(rocks, Point(0, -1))
            if new_y is not None:
                y = new_y
            air += 1

    return y


@aoc.part(2)
def part2(items):
    air = 0
    i = 0
    rocks = set()
    signatures = {}
    y = 0
    t = 0
    height = 0
    threshold = 1_000_000_000_000
    while t < threshold:
        r = Rock(Point(2, y + 4), t % 5)
        while not r.colliding:
            a = items[air]
            if a == "<":
                r.move(rocks, Point(-1, 0))
            else:
                r.move(rocks, Point(1, 0))
            new_y = r.move(rocks, Point(0, -1))
            if new_y is not None:
                y = new_y
            air = (air + 1) % len(items)

        s = (air % len(items), t % 5, signature(rocks, y))
        if t >= 2022 and s in signatures:
            old_y, old_t = signatures[s]
            dt = t - old_t
            dy = y - old_y
            times = (threshold - t) // dt
            height += times * dy
            t += times * dt

        signatures[s] = (y, t)
        t += 1

    return y + height


if __name__ == "__main__":
    aoc.solve()
