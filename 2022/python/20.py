# flake8: noqa

from python import *
import sys
import numpy as np
from collections import defaultdict
import re

aoc = AdventOfCode("2022", "20", "", newint)


def move(l):
    for i in range(len(l)):
        for k, (j, value) in enumerate(l):
            if j == i:
                item = l.pop(k)
                if (k + value) % len(l) == 0:
                    l.append(item)
                else:
                    l.insert((k + value) % len(l), item)
                break
    return l


def sum(l):
    items = [value for _, value in l]
    index = items.index(0)
    s = 0
    for k in [1000, 2000, 3000]:
        s += items[(index + k) % len(items)]
    return s


@aoc.part(1)
def part1(items):
    l = list(enumerate(items))
    move(l)
    return sum(l)


@aoc.part(2)
def part2(items):
    key = 811589153
    items = [key * value for value in items]
    l = list(enumerate(items))
    for _ in range(10):
        move(l)
    return sum(l)


if __name__ == "__main__":
    aoc.solve()
