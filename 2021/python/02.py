# flake8: noqa

from python import *

aoc = AdventOfCode("2021", "02", "Dive!", new)


@aoc.part(1)
def part1(items):
    pos = [0, 0]
    for item in items:
        [cmd, val] = item.split(" ")
        if cmd == "forward":
            pos[0] += int(val)
        elif cmd == "up":
            pos[1] -= int(val)
        elif cmd == "down":
            pos[1] += int(val)
    return pos[1] * pos[0]


@aoc.part(2)
def part2(items):
    pos = [0, 0]
    aim = 0
    for item in items:
        [cmd, val] = item.split(" ")
        if cmd == "forward":
            pos[0] += int(val)
            pos[1] += aim * int(val)
        elif cmd == "up":
            aim -= int(val)
        elif cmd == "down":
            aim += int(val)
    return pos[1] * pos[0]


if __name__ == "__main__":
    aoc.solve()
