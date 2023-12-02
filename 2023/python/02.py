# flake8: noqa

from python import *
import sys
import numpy as np
from collections import defaultdict
import re

aoc = AdventOfCode("2023", "02", "", new)

def calculate(items):
    valid = {"red": 12, "green": 13, "blue": 14}
    p1 = 0
    p2 = 0
    for line in items:
        min_number = {"red": 0, "green": 0, "blue": 0}
        id_, bag = line.split(":")
        i = int(id_.split()[1])
        sets = bag.split(";")
        possible = True
        for cubes in sets:
            cubes = [c.strip().split() for c in cubes.split(",")]
            for cnt, color in cubes:
                if int(cnt) > valid[color]:
                    possible = False
                min_number[color] = max(min_number[color], int(cnt))

        if possible:
            p1 += i
        power = 1
        for cube in min_number:
            power *= min_number[cube]
        p2 += power

    return p1, p2

@aoc.part(1)
def part1(items):
    return calculate(items)[0]
    


@aoc.part(2)
def part2(items):
    return calculate(items)[1]



if __name__ == "__main__":
    aoc.solve()
