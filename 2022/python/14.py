# flake8: noqa

from python import *
import sys
import numpy as np
from collections import defaultdict
import re

aoc = AdventOfCode("2022", "14", "", new)


def parse(items):
    occupied = set()
    for line in items:
        points = [Point(*tuple(map(int, l.split(",")))) for l in line.split("->")]

        for i in range(1, len(points)):
            d = points[i] - points[i - 1]
            for j in range(max(abs(d.x), abs(d.y)) + 1):
                occupied.add(
                    (
                        points[i - 1].x if d.x == 0 else points[i - 1].x + j * sign(d.x),
                        points[i - 1].y if d.y == 0 else points[i - 1].y + j * sign(d.y),
                    )
                )
    return occupied


def tick(s, occupied, fall):
    dy = s.y + 1
    if (s.x, dy) in occupied and (s.x + 1, dy) in occupied and (s.x - 1, dy) in occupied:
        # rest
        occupied.add((s.x, s.y))
        s = Point(500, 0)
        fall = 0
    elif (s.x, dy) in occupied and (s.x + 1, dy) in occupied:
        # left empty
        s += Point(-1, 1)
    elif (s.x, dy) in occupied and (s.x - 1, dy) in occupied:
        # right empty
        s += Point(1, 1)
    elif (s.x, dy) in occupied:
        # both empty
        s += Point(-1, 1)
    else:
        # all empty
        s += Point(0, 1)
        fall += 1
    return s, fall


@aoc.part(1)
def part1(items):
    occupied = parse(items)

    rocks = len(occupied)
    s = Point(500, 0)
    fall = 0
    while True:
        s, fall = tick(s, occupied, fall)
        if fall > 1000:
            break

    return len(occupied) - rocks


@aoc.part(2)
def part2(items):
    occupied = parse(items)
    floor_y = max(occupied, key=lambda x: x[1])[1] + 2
    d = 1000
    for i in range(-d, d):
        occupied.add((500 + i, floor_y))

    rocks = len(occupied)
    s = Point(500, 0)
    while True:
        s, _ = tick(s, occupied, 0)
        if (500, 0) in occupied:
            break
    return len(occupied) - rocks


if __name__ == "__main__":
    aoc.solve()
