# flake8: noqa

from python import *
import sys
import numpy as np
from collections import defaultdict
import re

aoc = AdventOfCode("2022", "10", "Cathode-Ray Tube", new)


@aoc.part(1)
def part1(items):
    acc = 0
    x = 1
    cycles = 0
    last = 0
    thresholds = [20 + 40 * i for i in range(6)]
    for line in items:
        cmd, *rest = line.split()
        if cmd == "addx":
            last = int(rest[0])
            x += last
            cycles += 2
        else:
            cycles += 1
        if len(thresholds) > 0 and cycles >= thresholds[0]:
            if cmd == "noop":
                acc += thresholds[0] * x
            else:
                acc += thresholds[0] * (x - last)
            del thresholds[0]
    return acc


@aoc.part(2)
def part2(items):
    x = 1
    crt = ""
    out = ""
    pos = 0

    def update(pos, crt, out, x):
        crt += "#" if x - 1 <= pos % 40 <= x + 1 else "."
        pos += 1
        if pos % 40 == 0:
            out += crt + "\n"
            crt = ""
        return pos, crt, out

    for line in items:
        cmd, *rest = line.split()

        if cmd == "addx":
            v = int(rest[0])
            pos, crt, out = update(pos, crt, out, x)
            pos, crt, out = update(pos, crt, out, x)
            x += v
        else:
            pos, crt, out = update(pos, crt, out, x)

    print(out)


if __name__ == "__main__":
    aoc.solve()
