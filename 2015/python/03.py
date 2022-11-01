# flake8: noqa

from python import *

aoc = AdventOfCode("2021", "03", "", identity)


def parse(c, p):
    if c == ">":
        p += Point.EAST
    elif c == "<":
        p += Point.WEST
    elif c == "v":
        p += Point.SOUTH
    elif c == "^":
        p += Point.NORTH
    return p


@aoc.part(1)
def part1(items):
    points = set()
    p = Point(0, 0)
    points.add((p.x, p.y))
    for c in items:
        p = parse(c, p)
        points.add((p.x, p.y))

    return len(points)


@aoc.part(2)
def part2(items):
    points = set()
    p1 = Point(0, 0)
    p2 = Point(0, 0)
    points.add((p1.x, p1.y))
    points.add((p2.x, p2.y))
    for c in items[0::2]:
        p1 = parse(c, p1)
        points.add((p1.x, p1.y))

    for c in items[1::2]:
        p2 = parse(c, p2)
        points.add((p2.x, p2.y))
    return len(points)


if __name__ == "__main__":
    aoc.solve()
