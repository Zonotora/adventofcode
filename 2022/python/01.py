# flake8: noqa

from python import *
import sys
import numpy as np
from collections import defaultdict

aoc = AdventOfCode("2022", "01", "Calorie Counting", newnewint)


def calories(items):
    total = []
    for item in items:
        s = sum(item)
        total.append(s)
    return total


@aoc.part(1)
def part1(items):
    total = calories(items)
    return max(total)


@aoc.part(2)
def part2(items):
    total = calories(items)
    return sum(sorted(total)[-3:])


if __name__ == "__main__":
    aoc.solve()
