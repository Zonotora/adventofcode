# flake8: noqa

from python import *
import sys
import numpy as np
from collections import defaultdict, Counter
import math
import re

aoc = AdventOfCode("2023", "07", "", new)


def kind(hand, part):
    cnt = Counter(hand)
    wildcards = 0
    if "J" in cnt:
        wildcards = cnt["J"]

    if part == 2:
        del cnt["J"]

    k = -2
    if 5 in cnt.values(): # five of a kind
        k = 5
    elif 4 in cnt.values(): # four of a kind
        k = 4
    elif 2 in cnt.values() and 3 in cnt.values(): # full house
        k = 3
    elif 3 in cnt.values(): # three of a kind
        k = 2
    elif len(list(filter(lambda x: x == 2, cnt.values()))) == 2: # two pair
        k =  1
    elif 2 in cnt.values(): # one pair
        k =  0
    elif len(cnt) > 0: # high card
        k = -1

    if part == 1:
        return k

    for w in range(wildcards):
        assert k <= 5, (k, w, hand)
        if 0 <= k <= 2:
            k += 2
        else:
            k += 1

    return k

def equal(hand, part):
    if part == 1:
        mapping = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    else:
        mapping = {"T": 10, "J": 1, "Q": 12, "K": 13, "A": 14}
    return tuple([kind(hand, part)] + [mapping[c] if c in mapping else int(c) for c in hand])

def create(items, part):
    hands = []
    for line in items:
        hand, bid = line.split()
        hands.append((hand, int(bid), equal(hand, part)))
    return hands

def calculate(items, part=1):
    hands = create(items, part)
    sorted_hands = sorted(hands, key=lambda h: h[2])
    res = 0
    for rank, (_, bid, _) in enumerate(sorted_hands):
        res += (rank + 1) * bid
    return res

@aoc.part(1)
def part1(items):
    return calculate(items)

@aoc.part(2)
def part2(items):
    return calculate(items, part=2)

if __name__ == "__main__":
    aoc.solve()