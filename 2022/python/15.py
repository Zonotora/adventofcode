# flake8: noqa

from python import *
import sys
import numpy as np
from collections import defaultdict
import re

aoc = AdventOfCode("2022", "15", "", new)


@aoc.part(1)
def part1(items):
    beacons = set()

    y = 2000000
    interval = Interval()
    for line in items:
        sx, sy, bx, by = list(map(int, (re.findall(r"[-]?\d+", line))))
        beacons.add((bx, by))
        dx = abs(sx - bx)
        dy = abs(sy - by)
        ny = abs(y - sy)
        if ny < 0:
            continue
        nx = dx + dy - ny
        if sx - nx > sx + nx:
            continue
        interval.add(sx - nx, sx + nx)

    return interval.sum()


@aoc.part(2)
def part2(items):
    invalid = defaultdict(lambda: Interval())
    for line in items:
        sx, sy, bx, by = list(map(int, (re.findall(r"[-]?\d+", line))))
        dx = abs(sx - bx)
        dy = abs(sy - by)
        n = dx + dy
        for y in range(-n, n + 1):
            nx = n - abs(y)
            ny = sy + y
            invalid[ny].add(sx - nx, sx + nx)

    threshold = 4000000
    for key in invalid:
        interval = invalid[key].parts
        if int(key) < 0 or int(key) > threshold or len(interval) == 1:
            continue

        keep = False
        for i in range(1, len(interval)):
            _, ex = interval[i - 1]
            sx, _ = interval[i]
            if ex + 1 != sx:
                keep = True
        if not keep:
            continue

        x = interval[0][1] + 1
        return 4000000 * x + int(key)


if __name__ == "__main__":
    aoc.solve()
