# flake8: noqa

from typing import Collection
from python import *
import math

aoc = AdventOfCode("2021", "05", "Hydrothermal Venture", new)


@aoc.part(1)
def part1(items):
    positions = {}
    for line in items:
        line = line.split(" -> ")
        [sx, sy] = list(map(int, line[0].split(",")))
        [ex, ey] = list(map(int, line[1].split(",")))
        if sx == ex or sy == ey:
            for x in range(min(sx, ex), max(sx, ex) + 1):
                for y in range(min(sy, ey), max(sy, ey) + 1):
                    positions[(x, y)] = positions.get((x, y), 0) + 1

    collision = 0
    for key in positions:
        if positions[key] >= 2:
            collision += 1
    return collision


@aoc.part(2)
def part2(items):
    positions = {}
    for line in items:
        line = line.split("->")
        [sx, sy] = list(map(int, line[0].strip().split(",")))
        [ex, ey] = list(map(int, line[1].strip().split(",")))
        if sx == ex or sy == ey:
            for x in range(min(sx, ex), max(sx, ex) + 1):
                for y in range(min(sy, ey), max(sy, ey) + 1):
                    positions[(x, y)] = positions.get((x, y), 0) + 1
        elif abs(sx - ex) == abs(sy - ey):
            x = sx if sx < ex else ex
            k = int((ey - sy) / (ex - sx))
            y = max(sy, ey) if k < 0 else min(sy, ey)

            for i in range(abs(ex - sx) + 1):
                key = (x + i, y + i * k)
                positions[key] = positions.get(key, 0) + 1
    collision = 0
    for key in positions:
        if positions[key] >= 2:
            collision += 1
    return collision


if __name__ == "__main__":
    aoc.solve()
