# flake8: noqa

from python import *
import sys
import numpy as np
from collections import defaultdict
import re

aoc = AdventOfCode("2022", "06", "Tuning Trouble", identity)


def compute(items, n):
    for i in range(len(items) - n + 1):
        unique = set()
        for j in range(i, i + n):
            unique.add(items[j])
        if len(unique) == n:
            return i + n


@aoc.part(1)
def part1(items):
    return compute(items, 4)


@aoc.part(2)
def part2(items):
    return compute(items, 14)


if __name__ == "__main__":
    aoc.solve()
