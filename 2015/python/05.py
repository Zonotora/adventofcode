# flake8: noqa

from python import *
from collections import defaultdict

aoc = AdventOfCode("2021", "05", "", new)

vowels = "aeiou"
forbidden = ["ab", "cd", "pq", "xy"]


@aoc.part(1)
def part1(items):
    s = 0
    for item in items:
        v = 0
        f = True
        double = False
        for c in item:
            if c in vowels:
                v += 1

        for c in each_cons(item, 2):
            if c in forbidden:
                f = False
            if c[0] == c[1]:
                double = True

        if v >= 3 and f and double:
            s += 1

    return s


@aoc.part(2)
def part2(items):
    s = 0
    for item in items:
        combinations = dict()
        twice = False
        double = False

        pairs = each_cons(item, 2)
        combinations[pairs[0]] = 1
        for i in range(1, len(pairs)):
            c = pairs[i]
            if c not in combinations:
                combinations[c] = 1
                continue
            if pairs[i] == pairs[i - 1]:
                continue
            combinations[c] += 1
            if combinations[c] > 1:
                twice = True

        for c in each_cons(item, 3):
            if c[0] == c[2]:
                double = True
                break

        if twice and double:
            s += 1

    return s


if __name__ == "__main__":
    aoc.solve()
