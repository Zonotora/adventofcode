# flake8: noqa

from python import *
import sys
import numpy as np
from collections import defaultdict
import string

aoc = AdventOfCode("2022", "03", "", new)


def prio(item):
    prio1 = {v: i + 1 for i, v in enumerate(string.ascii_lowercase)}
    prio2 = {v: i + 27 for i, v in enumerate(string.ascii_uppercase)}
    if item in prio1:
        return prio1[item]
    elif item in prio2:
        return prio2[item]


@aoc.part(1)
def part1(items):
    s = 0
    for item in items:
        n = len(item) // 2
        same = set(item[:n]) & set(item[n:])
        s += prio(next(iter(same)))

    return s


@aoc.part(2)
def part2(items):
    s = 0
    for i in range(0, len(items), 3):
        same = set(items[i]) & set(items[i + 1]) & set(items[i + 2])
        s += prio(next(iter(same)))

    return s


if __name__ == "__main__":
    aoc.solve()
