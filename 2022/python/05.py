# flake8: noqa

from python import *
import sys
import numpy as np
from collections import defaultdict
import re

aoc = AdventOfCode("2022", "05", "Supply Stacks", new)


def process(items):
    n_bins = len(re.findall(r"\d+", items[8]))
    bins = [[] for _ in range(n_bins)]
    for i in range(7, -1, -1):
        item = items[i]
        k = 0
        for j in range(1, len(item), 4):
            if item[j] != " ":
                bins[k].append(item[j])
            k += 1
    return bins


def compute(bins):
    s = ""
    for i in range(len(bins)):
        s += bins[i][-1]
    return s


@aoc.part(1)
def part1(items):
    bins = process(items)

    for i, item in enumerate(items):
        if i > 9:
            cnt, f, t = map(int, re.findall("[0-9]+", item))
            for i in range(cnt):
                v = bins[f - 1].pop()
                bins[t - 1].append(v)

    return compute(bins)


@aoc.part(2)
def part2(items):
    bins = process(items)

    for i, item in enumerate(items):
        if i > 9:
            cnt, f, t = map(int, re.findall("[0-9]+", item))
            vs = []
            for i in range(cnt):
                v = bins[f - 1].pop()
                vs.append(v)

            vs.reverse()
            bins[t - 1].extend(vs)

    return compute(bins)


if __name__ == "__main__":
    aoc.solve()
