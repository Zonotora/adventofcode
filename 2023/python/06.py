# flake8: noqa

from python import *
import sys
import numpy as np
from collections import defaultdict
import math
import re

aoc = AdventOfCode("2023", "06", "", new)

def calculate(time, record):
    res = 1
    for i in range(len(time)):
        count = 0
        for t in range(time[i]):
            left = time[i] - t
            if t * left > record[i]:
                count += 1
        res *= count

    return res

@aoc.part(1)
def part1(items):
    [time, record] = [list(map(int, x.split(":")[1].split())) for x in items]
    return calculate(time, record)


@aoc.part(2)
def part2(items):
    time, record = [[int("".join(x.split(":")[1].split()))] for x in items]
    return calculate(time, record)

if __name__ == "__main__":
    aoc.solve()
