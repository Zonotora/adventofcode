# flake8: noqa

from python import *
import sys
import numpy as np
from collections import defaultdict
import re
from itertools import takewhile

aoc = AdventOfCode("2022", "08", "", new)


def check(items, i, j):
    c = all([items[k][j] < items[i][j] for k in range(i)])
    c |= all([items[k][j] < items[i][j] for k in range(i + 1, len(items))])
    c |= all([items[i][k] < items[i][j] for k in range(j)])
    c |= all([items[i][k] < items[i][j] for k in range(j + 1, len(items[0]))])
    return c


def compute(items, i, j):
    t = [items[k][j] < items[i][j] for k in range(i - 1, -1, -1)]
    b = [items[k][j] < items[i][j] for k in range(i + 1, len(items))]
    l = [items[i][k] < items[i][j] for k in range(j - 1, -1, -1)]
    r = [items[i][k] < items[i][j] for k in range(j + 1, len(items[0]))]
    ret = 1
    for item in [t, b, l, r]:
        s = 0
        for pred in item:
            s += 1
            if not pred:
                break

        ret *= s

    return ret


@aoc.part(1)
def part1(items):
    s = 0
    for i in range(len(items)):
        for j in range(len(items[i])):
            s += check(items, i, j)
    return s


@aoc.part(2)
def part2(items):
    s = 0
    for i in range(len(items)):
        for j in range(len(items[i])):
            s = max(s, compute(items, i, j))
    return s


if __name__ == "__main__":
    aoc.solve()
