# flake8: noqa

from python import *
import sys
import numpy as np
from collections import defaultdict
import math
import re

aoc = AdventOfCode("2023", "04", "", new)


def calculate(items):
    scores = []
    for line in items:
        id_, cards = line.split(":")
        winning, my = [x.strip().split() for x in cards.split("|")]
        score = 0
        for m in my:
            if m in winning:
                if score == 0:
                    score = 1
                else:
                    score *=2
        scores.append(score)
    return scores

@aoc.part(1)
def part1(items):
    return sum(calculate(items))

@aoc.part(2)
def part2(items):
    scores = calculate(items)
    cards = list(map(lambda _: 1, scores))
    for i in range(len(scores)):
        if scores[i] == 0:
            continue
        cnt = int(math.log2(scores[i])) + 1

        for j in range(i+1, i+cnt+1):
            cards[j] += cards[i]

    return sum(cards)



if __name__ == "__main__":
    aoc.solve()
