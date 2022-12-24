# flake8: noqa

from python import *
import sys
import numpy as np
import math
from collections import defaultdict, deque
import re

aoc = AdventOfCode("2022", "24", "", new)

directions = {(1, 0): ">", (-1, 0): "<", (0, 1): "v", (0, -1): "^"}
inverse_directions = {">": (1, 0), "<": (-1, 0), "v": (0, 1), "^": (0, -1)}


def parse(grid):
    blizzards = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            p = (j, i)
            key = grid[i][j]
            if key in "><v^":
                blizzards[p] = [inverse_directions[key]]

    nx = len(grid[0]) - 2
    ny = len(grid) - 2
    s = (1, 0)
    e = (nx, ny + 1)
    lcm = math.lcm(nx, ny)
    return blizzards, nx, ny, s, e, lcm


def print_grid(blizzards, nx, ny, player=None):
    for i in range(ny + 2):
        s = ""
        for j in range(nx + 2):
            if player and player == (j, i):
                s += "E"
            elif i == 0 or i == ny + 1 or j == 0 or j == nx + 1:
                s += "#"
            elif (j, i) in blizzards:
                b = blizzards[(j, i)]
                if len(b) == 1:
                    s += directions[b[0]]
                else:
                    s += str(len(b))
            else:
                s += "."
        print(s)
    input()


def move(blizzards, nx, ny):
    next_blizzards = {}
    for (x, y) in blizzards:
        bs = blizzards[(x, y)]
        for (dx, dy) in bs:
            px = (x + dx - 1) % nx + 1
            py = (y + dy - 1) % ny + 1
            if (px, py) not in next_blizzards:
                next_blizzards[(px, py)] = [(dx, dy)]
            else:
                next_blizzards[(px, py)].append((dx, dy))

    return next_blizzards


def compute(blizzards, nx, ny, s, e, lcm):
    next_valid = [(1, 0), (-1, 0), (0, 1), (0, -1), (0, 0)]
    start = (*s, 0)
    q = deque([start])
    seen = set()
    old_ticks = -1
    while q:
        x, y, ticks = q.popleft()

        if (x, y) == e:
            return ticks, blizzards

        if old_ticks != ticks:
            blizzards = move(blizzards, nx, ny)
            old_ticks = ticks

        for (dx, dy) in next_valid:
            px = x + dx
            py = y + dy

            if (px, py) != s and (px, py) != e and not (1 <= px <= nx and 1 <= py <= ny):
                continue

            next_state = (px, py, (ticks + 1) % lcm)
            if next_state in seen:
                continue
            seen.add(next_state)

            if (px, py) not in blizzards:
                q.append((px, py, ticks + 1))


@aoc.part(1)
def part1(grid):
    ans, _ = compute(*parse(grid))
    return ans


@aoc.part(2)
def part2(grid):
    blizzards, nx, ny, s, e, lcm = parse(grid)
    time1, blizzards = compute(blizzards, nx, ny, s, e, lcm)
    time2, blizzards = compute(blizzards, nx, ny, e, s, lcm)
    time3, blizzards = compute(blizzards, nx, ny, s, e, lcm)
    return time1 + (time2 + 1) + (time3 + 1)


if __name__ == "__main__":
    aoc.solve()
