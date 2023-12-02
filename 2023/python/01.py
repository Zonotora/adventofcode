# flake8: noqa

from python import *
import sys
import numpy as np
from collections import defaultdict
import re

aoc = AdventOfCode("2023", "01", "", new)

def calibrate(s):
    res = ""
    for c in s:
        if c.isdigit():
            res += c
            break
    for c in reversed(s):
        if c.isdigit():
            res += c
            break
    return int(res)

def real_calibrate(s):
    pattern = r"([0-9]|one|two|three|four|five|six|seven|eight|nine)"
    matches = re.finditer(f'(?=({pattern}))', s)
    matches = [match.group(1) for match in matches]
    mapping = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    res = ""
    res += str(mapping.index(matches[0]) + 1) if matches[0] in mapping else matches[0]
    res += str(mapping.index(matches[-1]) + 1) if matches[-1] in mapping else matches[-1]
    return int(res)


@aoc.part(1)
def part1(items):
    res = 0
    for s in items:
        res += calibrate(s)
    return res
    


@aoc.part(2)
def part2(items):
    res = 0
    for s in items:
        res += real_calibrate(s)
    return res



if __name__ == "__main__":
    aoc.solve()
