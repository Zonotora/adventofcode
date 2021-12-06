# flake8: noqa

from python import *
from collections import Counter, deque

aoc = AdventOfCode("2021", "06", "Lanternfish", commaint)


@aoc.part(1)
def part1(items):
    for j in range(80):
        n = len(items)
        for i in range(n):
            if items[i] == 0:
                items.append(8)
                items[i] = 6
            else:
                items[i] -= 1

    return len(items)


@aoc.part(2)
def part2(items):
    c = Counter(items)
    p = deque([0] * 9)
    for i in range(len(p)):
        p[i] = c[i]

    for i in range(256):
        b = p[0]
        p.rotate(-1)
        p[6] += b
    return sum(p)


if __name__ == "__main__":
    aoc.solve()
