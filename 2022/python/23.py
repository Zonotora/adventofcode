# flake8: noqa

from python import *
import sys
import numpy as np
from collections import defaultdict
import re

aoc = AdventOfCode("2022", "23", "", new)


def check(x, y, dx, dy, moves, elves, deletes):
    free = 0
    for i in range(-1, 2):
        if (x + i * dy + dx, y + i * dx + dy) not in elves:
            free += 1

    if free == 3:
        key = (x + dx, y + dy)
        if key not in moves:
            moves[key] = (x, y)
        else:
            deletes.add(key)
        return True
    return False


def print_elves(elves):
    min_x, max_x = min(elves, key=lambda e: e[0])[0], max(elves, key=lambda e: e[0])[0]
    min_y, max_y = min(elves, key=lambda e: e[1])[1], max(elves, key=lambda e: e[1])[1]
    print("-" * 40)
    for i in range(min_y, max_y + 1):
        s = ""
        for j in range(min_x, max_x + 1):
            if (j, i) in elves:
                s += "#"
            else:
                s += "."
        print(s)
    input()


def compute(items, part):
    elves = set()
    for i in range(len(items)):
        for j in range(len(items[i])):
            if items[i][j] == "#":
                elves.add((j, i))

    first = 0
    checks = [
        lambda x, y, elves, moves, deletes: check(x, y, 0, -1, moves, elves, deletes),
        lambda x, y, elves, moves, deletes: check(x, y, 0, 1, moves, elves, deletes),
        lambda x, y, elves, moves, deletes: check(x, y, -1, 0, moves, elves, deletes),
        lambda x, y, elves, moves, deletes: check(x, y, 1, 0, moves, elves, deletes),
    ]

    while True:
        # round 1
        moves = {}
        deletes = set()
        for x, y in elves:
            neighbours = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == j == 0:
                        continue

                    pos = (x + j, y + i)
                    if pos in elves:
                        neighbours += 1

            if neighbours == 0:
                continue

            i = first % 4
            cnt = 0
            while not checks[i](x, y, elves, moves, deletes) and cnt < 4:
                i = (i + 1) % 4
                cnt += 1

        for key in deletes:
            del moves[key]

        # round 2
        for key in moves:
            old = moves[key]
            assert old in elves
            elves.remove(old)
            elves.add(key)

        if len(moves) == 0:
            return first + 1

        if part == 1 and first == 9:
            break
        first += 1

    min_x, max_x = min(elves, key=lambda e: e[0])[0], max(elves, key=lambda e: e[0])[0]
    min_y, max_y = min(elves, key=lambda e: e[1])[1], max(elves, key=lambda e: e[1])[1]
    total = (max_y - min_y + 1) * (max_x - min_x + 1)
    return total - len(elves)


@aoc.part(1)
def part1(items):
    return compute(items, 1)


@aoc.part(2)
def part2(items):
    return compute(items, 2)


if __name__ == "__main__":
    aoc.solve()
