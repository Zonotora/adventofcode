# flake8: noqa

from python import *
import sys
import numpy as np
from collections import defaultdict
import math
import re

aoc = AdventOfCode("2023", "05", "", newnew)

def create(items):
    seeds = list(map(int, items[0].split(":")[1].split()))
    mapping = defaultdict(list)
    undef_mapping = {}
    for line in items[1:]:
        name, *rest = line.split("\n")
        f,_, t = name.split()[0].split("-")
        rest = [[int(i) for i in x.split()] for x in rest]
        for dst, src, l in rest:
            mapping[f].append((dst, src, l))
            undef_mapping[f] = t
    return seeds, mapping, undef_mapping

@aoc.part(1)
def part1(items):
    seeds, mapping, undef_mapping = create(items)
    location = 2**32-1
    for value in seeds:
        key = "seed"
        while key != "location":
            for dst, src, l in mapping[key]:
                if src <= value < src + l:
                    diff = value - src
                    value = dst + diff
                    break
            key = undef_mapping[key]
        location = min(location, value)
    return location


@aoc.part(2)
def part2(items):
    seeds, mapping, undef_mapping = create(items)
    pairs = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]

    location = 2**32-1
    for start_value, r in pairs:
        remaining = r
        while remaining >= 0:
            active = r
            key = "seed"
            value = start_value

            while key != "location":
                for dst, src, l in mapping[key]:
                    if src <= value < src + l:
                        diff = value - src
                        active = min(active, src + l - value)
                        value = dst + diff
                        break
                key = undef_mapping[key]
            location = min(location, value)
            remaining -= active
            start_value += active

    return location


if __name__ == "__main__":
    aoc.solve()
