# flake8: noqa

from python import *
import sys
import numpy as np
from collections import defaultdict
from itertools import permutations
import re

aoc = AdventOfCode("2022", "25", "", new)


def compute(line):
    s = 0
    n = len(line)
    for i, c in enumerate(line):
        s += ("=-012".index(c) - 2) * (5 ** (n - i - 1))
    return s


def encode(x):
    s = ""
    while x > 0:
        s += "=-012"[(x + 2) % 5]
        x = round(x / 5)
    return s[::-1]


@aoc.part(1)
def part1(items):
    ans = 0
    for line in items:
        ans += compute(line)
    return encode(ans)


@aoc.part(2)
def part2(items):
    return 0


if __name__ == "__main__":
    aoc.solve()
