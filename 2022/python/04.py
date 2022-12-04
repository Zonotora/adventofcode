# flake8: noqa

from python import *
import sys
import numpy as np
from collections import defaultdict

aoc = AdventOfCode("2022", "04", "", new)


@aoc.part(1)
def part1(items):
    s = 0
    for item in items:
        pairs = item.split(",")
        ran = []
        for p in pairs:
            fst, snd = list(map(int, p.split("-")))
            ran.append(fst)
            ran.append(snd)
        if ran[0] >= ran[2] and ran[1] <= ran[3] or ran[0] <= ran[2] and ran[1] >= ran[3]:
            s += 1

    return s


@aoc.part(2)
def part2(items):
    s = 0
    for item in items:
        pairs = item.split(",")
        ran = []
        for p in pairs:
            fst, snd = list(map(int, p.split("-")))
            ran.append(fst)
            ran.append(snd)
        if (
            ran[1] >= ran[2]
            and ran[0] <= ran[2]
            or ran[0] <= ran[3]
            and ran[1] >= ran[3]
            or ran[0] >= ran[2]
            and ran[1] <= ran[3]
            or ran[0] <= ran[2]
            and ran[1] >= ran[3]
        ):
            s += 1

    return s


if __name__ == "__main__":
    aoc.solve()
