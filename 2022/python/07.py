# flake8: noqa

from python import *
import sys
import numpy as np
from collections import defaultdict
import re

aoc = AdventOfCode("2022", "07", "", new)


def compute(items):
    parent = []
    dirs = defaultdict(int)
    for line in items:

        if line.startswith("$"):
            _, cmd, *value = line.split()
            if cmd == "cd":
                value = value[0]
                if value == "..":
                    value = parent.pop()
                else:
                    parent.append(value)
        else:
            value, name = line.split()
            if value != "dir":
                wd = ""
                for d in parent:
                    suffix = "/" if d != "/" else ""
                    wd += d + suffix
                    dirs[wd] += int(value)
    return dirs


@aoc.part(1)
def part1(items):
    dirs = compute(items)
    s = 0
    for d in dirs:
        if dirs[d] <= 100000:
            s += dirs[d]

    return s


@aoc.part(2)
def part2(items):
    dirs = compute(items)
    candidates = []
    unused = 70000000 - dirs["/"]
    for d in dirs:
        if dirs[d] >= 30000000 - unused:
            candidates.append(dirs[d])

    return sorted(candidates)[0]


if __name__ == "__main__":
    aoc.solve()
