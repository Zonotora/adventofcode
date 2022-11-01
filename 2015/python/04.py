# flake8: noqa

from python import *
import hashlib

aoc = AdventOfCode("2021", "04", "", identity)


def find(items, n):
    i = 0
    check = "0" * n
    while True:
        s = f"{items}{i}"
        h = hashlib.md5(s.encode("utf-8")).hexdigest()
        if h[:n] == check:
            return i
        i += 1
    return 0


@aoc.part(1)
def part1(items):
    return find(items, 5)


@aoc.part(2)
def part2(items):
    return find(items, 6)


if __name__ == "__main__":
    aoc.solve()
