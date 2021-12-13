# flake8: noqa

from python import *

aoc = AdventOfCode("2021", "13", "", newnew)


def fold(items, p1):
    coords = [
        [int(x) for x in c.strip().split(",")] for c in items[0].split("\n")
    ]
    for cmd in items[1].split("\n"):
        c, v = cmd.split("=")
        if "y" in c:
            y = int(v)
            for i in range(len(coords)):
                xx, yy = coords[i]
                if yy > y:
                    coords[i] = [xx, max(0, y - (yy - y))]
        else:
            x = int(v)
            for i in range(len(coords)):
                xx, yy = coords[i]
                if xx > x:
                    coords[i] = [max(0, x - (xx - x)), yy]
        if p1:
            break
    return coords


@aoc.part(1)
def part1(items):
    coords = fold(items, True)
    return len(set(map(tuple, coords)))


@aoc.part(2)
def part2(items):
    coords = fold(items, False)
    xmax = max([x for x, y in coords]) + 1
    ymax = max([y for x, y in coords]) + 1
    arr = [["."] * xmax for _ in range(ymax)]
    for x, y in coords:
        arr[y][x] = "#"
    pretty_print(arr, pad=2)
    return 0


if __name__ == "__main__":
    aoc.solve()
