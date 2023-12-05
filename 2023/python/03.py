# flake8: noqa

from python import *
import sys
import numpy as np
from collections import defaultdict
import re

aoc = AdventOfCode("2023", "03", "", new)


def increase(numbers, symbols, gears, key):
    ii, s, e = key
    value = 0
    for i in range(ii-1, ii+2):
        for j in range(s-1, e+1):
            if (i,j) in symbols:
                if symbols[(i, j)] == "*":
                    gears[(i, j)].append(numbers[key])
                value = numbers[key]
    return value

def calculate(items):
    symbols = {}
    numbers = {}
    gears = defaultdict(list)
    for i, item in enumerate(items):
        matches = re.finditer("[0-9]+", item)
        for m in matches:
            s, e = m.span()
            numbers[(i, s, e)] = int(m.group(0))

        for j, c in enumerate(item):
            if not c.isdigit() and c != ".":
                symbols[(i, j)] = c

    p1 = 0
    p2 = 0
    for key in numbers:
        p1 += increase(numbers, symbols, gears, key)
    for key in gears:
        if len(gears[key]) == 2:
            p2 += gears[key][0] * gears[key][1]

    return p1, p2

@aoc.part(1)
def part1(items):
    return calculate(items)[0]


@aoc.part(2)
def part2(items):
    return calculate(items)[1]


if __name__ == "__main__":
    aoc.solve()
