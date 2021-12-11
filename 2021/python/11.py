# flake8: noqa

from python import *

aoc = AdventOfCode("2021", "11", "Dumbo Octopus", new)


@aoc.part(1)
def part1(items):
    items = [[int(c) for c in item] for item in items]
    flashes = 0

    for _ in range(100):
        for i in range(len(items)):
            for j in range(len(items[i])):
                items[i][j] += 1
        i, j = 0, 0
        seen = set()
        while i < len(items):
            j = 0
            while j < len(items[i]):
                if (i, j) not in seen and items[i][j] > 9:
                    seen.add((i, j))
                    ns = neighbours(items, i, j)
                    for x, y in ns:
                        items[y][x] += 1
                    i, j = 0, -1
                    flashes += 1
                j += 1
            i += 1

        for i, j in seen:
            items[i][j] = 0

    return flashes


@aoc.part(2)
def part2(items):
    items = [[int(c) for c in item] for item in items]
    k = 0
    while True:
        for i in range(len(items)):
            for j in range(len(items[i])):
                items[i][j] += 1
        i, j = 0, 0
        seen = set()
        while i < len(items):
            j = 0
            while j < len(items[i]):
                if (i, j) not in seen and items[i][j] > 9:
                    seen.add((i, j))
                    ns = neighbours(items, i, j)
                    for x, y in ns:
                        items[y][x] += 1
                    i, j = 0, -1
                j += 1
            i += 1

        for i, j in seen:
            items[i][j] = 0

        simul = True
        for i in range(len(items)):
            for j in range(len(items[i])):
                if items[i][j] != 0:
                    simul = False
                    break
            if not simul:
                break
        k += 1
        if simul:
            break

    return k


if __name__ == "__main__":
    aoc.solve()
