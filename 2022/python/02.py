# flake8: noqa

from python import *
import sys
import numpy as np
from collections import defaultdict

aoc = AdventOfCode("2022", "02", "", new)


@aoc.part(1)
def part1(items):
    s = 0

    mapping = {"A": "X", "B": "Y", "C": "Z"}
    score = {"X": 1, "Y": 2, "Z": 3}
    for item in items:
        [fst, snd] = item.split()
        if mapping[fst] == snd:
            s += score[snd] + 3
        elif (
            snd == "Z"
            and mapping[fst] == "Y"
            or snd == "Y"
            and mapping[fst] == "X"
            or snd == "X"
            and mapping[fst] == "Z"
        ):
            s += score[snd] + 6
        else:
            s += score[snd]

    return s


@aoc.part(2)
def part2(items):
    s = 0

    draw = {"A": 1, "B": 2, "C": 3}
    lose = {"B": 1, "C": 2, "A": 3}
    win = {"C": 1, "A": 2, "B": 3}
    for item in items:
        [fst, snd] = item.split()
        if snd == "X":
            s += lose[fst]
        elif snd == "Y":
            s += draw[fst] + 3
        elif snd == "Z":
            s += win[fst] + 6

    return s


if __name__ == "__main__":
    aoc.solve()
