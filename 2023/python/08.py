# flake8: noqa

from python import *
import sys
import numpy as np
from math import lcm
from collections import defaultdict, Counter
import math
import re

aoc = AdventOfCode("2023", "08", "", newnew)

def create(items):
    instructions = items[0]
    steps = items[1].split("\n")
    mapping = {}
    for s in steps:
        m = re.search("([A-Z0-9]+) = \(([A-Z0-9]+), ([A-Z0-9]+)\)", s)
        mapping[m.group(1)] = (m.group(2), m.group(3))
    return instructions, mapping

@aoc.part(1)
def part1(items):
    instructions, mapping = create(items)

    count = 0
    current = "AAA"
    i = 0
    while True:
        key = instructions[i % len(instructions)]
        index = 0 if key == "L" else 1
        current = mapping[current][index]
        count += 1
        if current == "ZZZ":
            return count
        i += 1

@aoc.part(2)
def part2(items):
    instructions, mapping = create(items)
    count = 0
    current = []
    for key in mapping:
        if key[-1] == "A":
            current.append(key)

    i = 0
    cycles = [0] * len(current)
    while True:
        key = instructions[i % len(instructions)]
        index = 0 if key == "L" else 1

        for j in range(len(current)):
            if cycles[j] == 0 and current[j][-1] == "Z":
                cycles[j] = i

            current[j] = mapping[current[j]][index]

        if all([x > 0 for x in cycles]):
            return lcm(*cycles)

        count += 1
        if all([key[-1] == "Z" for key in current]):
            return count
        i += 1
    return 0

if __name__ == "__main__":
    aoc.solve()