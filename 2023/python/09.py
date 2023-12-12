# flake8: noqa

from python import *
import sys
import numpy as np
from math import lcm
from collections import defaultdict, Counter
import math
import re

aoc = AdventOfCode("2023", "09", "", new)

def diff(sequence):
    ret = []
    for [x1, x2] in  each_cons(sequence, 2):
        ret.append(x2 - x1)
    return ret

def calculate(items, part):
    items = [[int(x) for x in seq.split() ] for seq in items]
    s = 0
    index = -1 if part == 1 else 0
    direction = 1 if part == 1 else -1
    for sequence in items:
        history = [sequence]
        sequence =  diff(sequence)
        history.append(sequence)
        while not all([x == 0 for x in sequence]):
            sequence =  diff(sequence)
            history.append(sequence)

        history = list(reversed(history))
        for i in range(1, len(history)):
            history[i][index] = history[i][index] + history[i - 1][index] * direction
        s += history[-1][index]
    return s


@aoc.part(1)
def part1(items):
    return calculate(items, 1)


@aoc.part(2)
def part2(items):
    return calculate(items, 2)

if __name__ == "__main__":
    aoc.solve()
