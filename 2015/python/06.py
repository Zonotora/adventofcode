# flake8: noqa

from python import *

aoc = AdventOfCode("2021", "06", "", new)


def set_light(grid, x1, x2, y1, y2, value, part):
    for i in range(y1, y2 + 1):
        for j in range(x1, x2 + 1):
            if part == 2:
                if value == 2:
                    # grid[i][j] = 1 - grid[i][j]
                    grid[i][j] += 2
                elif value == 1:
                    grid[i][j] += 1
                else:
                    grid[i][j] = max(grid[i][j] - 1, 0)
            else:
                if value == 2:
                    grid[i][j] = 1 - grid[i][j]
                else:
                    grid[i][j] = value


def parse(items, part):
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    for item in items:
        parts = item.split()
        if parts[0] == "toggle":
            [x1, y1] = list(map(int, parts[1].split(",")))
            [x2, y2] = list(map(int, parts[3].split(",")))
            set_light(grid, x1, x2, y1, y2, 2, part)
        elif parts[1] == "off":
            [x1, y1] = list(map(int, parts[2].split(",")))
            [x2, y2] = list(map(int, parts[4].split(",")))
            set_light(grid, x1, x2, y1, y2, 0, part)
        elif parts[1] == "on":
            [x1, y1] = list(map(int, parts[2].split(",")))
            [x2, y2] = list(map(int, parts[4].split(",")))
            set_light(grid, x1, x2, y1, y2, 1, part)

    s = 0
    for i in range(1000):
        for j in range(1000):
            s += grid[i][j]

    return s


@aoc.part(1)
def part1(items):
    return parse(items, 1)


@aoc.part(2)
def part2(items):
    return parse(items, 2)


if __name__ == "__main__":
    aoc.solve()
