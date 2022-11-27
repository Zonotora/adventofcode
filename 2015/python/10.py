# flake8: noqa

from python import *
import sys
import numpy as np
from collections import defaultdict

aoc = AdventOfCode("2021", "10", "", identity)


def compute(items):
    cnt = []
    current = None
    for c in items:
        if current is None:
            current = (c, 1)
        elif current[0] == c:
            current = (c, current[1] + 1)
        else:
            cnt.append(current)
            current = (c, 1)
    if current is not None:
        cnt.append(current)

    s = ""
    for c, v in cnt:
        s += f"{v}{c}"

    return s


@aoc.part(1)
def part1(items):
    for _ in range(40):
        items = compute(items)
    return len(items)


@aoc.part(2)
def part2(items):
    for _ in range(50):
        items = compute(items)
    return len(items)


if __name__ == "__main__":
    aoc.solve()
