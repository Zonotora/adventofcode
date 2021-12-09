# flake8: noqa

from python import *
from functools import reduce
import operator

aoc = AdventOfCode("2021", "09", "Smoke Basin", new)


def check_neighbour(arr, i, j):
    ns = vhneighbours(arr, i, j)
    return all([int(arr[i][j]) < int(arr[y][x]) for x, y in ns])


def get_basin(arr, i, j, seen):
    seen.add((j, i))
    cnt = 0
    ns = vhneighbours(arr, i, j)
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
