# flake8: noqa

from python import *

aoc = AdventOfCode("2021", "02", "", new)


@aoc.part(1)
def part1(items):
    s = 0
    for line in items:
        [l, w, h] = list(map(int, line.split("x")))
        s += 2 * l * w + 2 * w * h + 2 * h * l
        a = sorted([l, w, h])
        s += a[0] * a[1]
    return s


@aoc.part(2)
def part2(items):
    s = 0
    for line in items:
        [l, w, h] = list(map(int, line.split("x")))
        a = sorted([l, w, h])
        s += a[0] + a[0] + a[1] + a[1]
        s += l * w * h
    return s


if __name__ == "__main__":
    aoc.solve()
