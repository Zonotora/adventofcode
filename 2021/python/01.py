# flake8: noqa

from python import *

aoc = AdventOfCode("2021", "01", "Sonar Sweep", newint)


@aoc.part(1)
def part1(items):
    cnt = 0
    for i in range(len(items) - 1):
        if items[i + 1] > items[i]:
            cnt += 1
    return cnt


@aoc.part(2)
def part2(items):
    cnt = 0
    for i in range(len(items) - 3):
        if items[i + 3] > items[i]:
            cnt += 1
    return cnt


if __name__ == "__main__":
    aoc.solve()
