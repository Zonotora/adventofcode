# flake8: noqa

from python import *

aoc = AdventOfCode("2021", "07", "", commaint)


@aoc.part(1)
def part1(items):
    smin = 9999999999
    for i in range(max(items)):
        s = 0
        for item in items:
            s += abs(item - i)
        smin = min(smin, s)
    return smin


@aoc.part(2)
def part2(items):
    smin = 9999999999
    for i in range(max(items)):
        s = 0
        for item in items:
            sm = sum(range(abs(item - i) + 1))
            s += abs(sm)
        smin = min(smin, s)
    return smin


if __name__ == "__main__":
    aoc.solve()
