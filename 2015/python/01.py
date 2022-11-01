# flake8: noqa

from python import *

aoc = AdventOfCode("2015", "01", "", identity)


@aoc.part(1)
def part1(items):
    left = items.count("(")
    right = items.count(")")
    return left-right


@aoc.part(2)
def part2(items):
    cnt = 0
    for i, c in enumerate(items):
        if c == "(":
            cnt += 1
        elif c == ")":
            cnt -= 1
        if cnt == -1:
            break
    return i+1


if __name__ == "__main__":
    aoc.solve()
