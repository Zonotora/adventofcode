# flake8: noqa

from python import *
from functools import reduce
import operator

aoc = AdventOfCode("2021", "09", "Smoke Basin", new)


def get_neighbours(arr, i, j):
    pos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    return [
        (j + x, i + y)
        for x, y in pos
        if 0 <= i + y < len(arr) and 0 <= j + x < len(arr[i])
    ]


def check_neighbour(arr, i, j):
    ns = get_neighbours(arr, i, j)
    return all([int(arr[i][j]) < int(arr[y][x]) for x, y in ns])


def get_basin(arr, i, j, seen):
    seen.add((j, i))
    cnt = 0
    ns = get_neighbours(arr, i, j)
    for x, y in ns:
        if (x, y) in seen or int(arr[y][x]) == 9:
            continue
        cnt += 1
        cnt += get_basin(arr, y, x, seen)
    return cnt


@aoc.part(1)
def part1(items):
    min_points = []
    for i in range(len(items)):
        for j in range(len(items[i])):
            if check_neighbour(items, i, j):
                min_points.append(int(items[i][j]))

    return sum(min_points) + len(min_points)


@aoc.part(2)
def part2(items):
    min_points = []
    for i in range(len(items)):
        for j in range(len(items[i])):
            if check_neighbour(items, i, j):
                min_points.append((i, j))
    basins = []
    for i, j in min_points:
        cnt = get_basin(items, i, j, set()) + 1
        basins.append(cnt)
    bs = sorted(basins)
    return reduce(operator.mul, bs[-3:], 1)


if __name__ == "__main__":
    aoc.solve()
