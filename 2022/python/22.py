# flake8: noqa

from python import *
import sys
import numpy as np
from collections import defaultdict
import re

aoc = AdventOfCode("2022", "22", "", newnew)

debug = True


def parse(items):
    instructions = []
    buffer = []
    for i in items:
        if i.isdigit():
            buffer.append(i)
        else:
            if buffer:
                instructions.append(int("".join(buffer)))
                buffer = []
            instructions.append(i)
    if buffer:
        instructions.append(int("".join(buffer)))
    return instructions


def print_grid(grid, position, direction):
    global debug
    if not debug:
        return
    directions = {(1, 0): ">", (-1, 0): "<", (0, 1): "^", (0, -1): "v"}
    for i in range(len(grid)):
        s = ""
        for j in range(len(grid[i])):
            if i == position[1] and j == position[0]:
                s += directions[direction]
            else:
                s += grid[i][j]
        print(s)
    input()


@aoc.part(1)
def part1(items):
    grid = items[0].split("\n")
    instructions = parse(items[1])
    position = (0, 0)
    for i in range(len(grid[0])):
        if grid[0][i] == ".":
            position = (i, 0)
            break

    direction = (1, 0)

    for insn in instructions:
        x, y = direction
        if insn == "R":
            direction = (y, -x)
        elif insn == "L":
            direction = (-y, x)
        else:
            dir_x, dir_y = direction
            for _ in range(insn):
                x, y = position
                ny = (y - dir_y) % len(grid)
                nx = x
                while x >= len(grid[ny]):
                    ny = (ny - dir_y) % len(grid)
                nx = (x + dir_x) % len(grid[ny])

                while grid[ny][nx] == " ":
                    ny = (ny - dir_y) % len(grid)
                    nx = (nx + dir_x) % len(grid[ny])

                if grid[ny][nx] == "#":
                    break
                position = (nx, ny)

    directions = {(1, 0): 0, (-1, 0): 2, (0, 1): 3, (0, -1): 1}
    x, y = position
    ans = 1000 * (y + 1) + 4 * (x + 1) + directions[direction]
    return ans


def make_cube_test(grid):
    n = len(grid) // 3
    sides = [(2 * n, 0), (0, n), (n, n), (2 * n, n), (2 * n, 2 * n), (3 * n, 2 * n)]
    cube = []
    for x, y in sides:
        side = []
        for i in range(y, y + n):
            row = []
            for j in range(x, x + n):
                row.append(grid[i][j])
            side.append(row)
        cube.append(side)
    return n, cube


def walk_off_test(n, current_side, position, direction):
    x, y = position
    match current_side:
        case 1:
            if y >= n:
                return 4, (x, 0), (0, -1)
            elif y < 0:
                return 2, (n - x - 1, 0), (0, -1)
            elif x >= n:
                return 6, (n - 1, n - y - 1), (-1, 0)
            elif x < 0:
                return 3, (y, 0), (0, -1)
        case 2:
            if y >= n:
                return 5, (n - x - 1, n - 1), (0, 1)
            elif y < 0:
                return 1, (n - x - 1, 0), (0, -1)
            elif x >= n:
                return 3, (0, y), (1, 0)
            elif x < 0:
                return 6, (n - y - 1, n - 1), (0, 1)
        case 3:
            if y >= n:
                return 5, (0, n - x - 1), (1, 0)
            elif y < 0:
                return 1, (0, x), (1, 0)
            elif x >= n:
                return 4, (0, y), (1, 0)
            elif x < 0:
                return 2, (n - 1, y), (-1, 0)
        case 4:
            if y >= n:
                return 5, (x, 0), (0, -1)
            elif y < 0:
                return 1, (x, n - 1), (0, 1)
            elif x >= n:
                return 6, (n - y - 1, 0), (0, -1)
            elif x < 0:
                return 3, (n - 1, y), (0, -1)
        case 5:
            if y >= n:
                return 2, (n - x - 1, n - 1), (0, 1)
            elif y < 0:
                return 4, (x, n - 1), (0, 1)
            elif x >= n:
                return 6, (0, y), (1, 0)
            elif x < 0:
                return 3, (n - y - 1, n - 1), (0, 1)
        case 6:
            if y >= n:
                return 2, (0, n - x - 1), (1, 0)
            elif y < 0:
                return 4, (n - 1, n - x - 1), (-1, 0)
            elif x >= n:
                return 1, (n - 1, n - y - 1), (-1, 0)
            elif x < 0:
                return 5, (n - 1, y), (-1, 0)
    return current_side, position, direction


def make_cube(grid):
    # . 1 2
    # . 3 .
    # 4 5 .
    # 6 . .
    n = len(grid) // 4
    sides = [(n, 0), (2 * n, 0), (n, n), (0, 2 * n), (n, 2 * n), (0, 3 * n)]
    cube = []
    for x, y in sides:
        side = []
        for i in range(y, y + n):
            row = []
            for j in range(x, x + n):
                row.append(grid[i][j])
            side.append(row)
        cube.append(side)
    return n, cube


def walk_off(n, current_side, position, direction):
    # . 1 2
    # . 3 .
    # 4 5 .
    # 6 . .

    x, y = position
    match current_side:
        case 1:
            if y >= n:
                return 3, (x, 0), (0, -1)
            elif y < 0:
                return 6, (0, x), (1, 0)
            elif x >= n:
                return 2, (0, y), (1, 0)
            elif x < 0:
                return 4, (0, n - y - 1), (1, 0)
        case 2:
            if y >= n:
                return 3, (n - 1, x), (-1, 0)
            elif y < 0:
                return 6, (x, n - 1), (0, 1)
            elif x >= n:
                return 5, (n - 1, n - y - 1), (-1, 0)
            elif x < 0:
                return 1, (n - 1, y), (-1, 0)
        case 3:
            if y >= n:
                return 5, (x, 0), (0, -1)
            elif y < 0:
                return 1, (x, n - 1), (0, 1)
            elif x >= n:
                return 2, (y, n - 1), (0, 1)
            elif x < 0:
                return 4, (y, 0), (0, -1)
        case 4:
            if y >= n:
                return 6, (x, 0), (0, -1)
            elif y < 0:
                return 3, (0, x), (1, 0)
            elif x >= n:
                return 5, (0, y), (1, 0)
            elif x < 0:
                return 1, (0, n - y - 1), (1, 0)
        case 5:
            if y >= n:
                return 6, (n - 1, x), (-1, 0)
            elif y < 0:
                return 3, (x, n - 1), (0, 1)
            elif x >= n:
                return 2, (n - 1, n - y - 1), (-1, 0)
            elif x < 0:
                return 4, (n - 1, y), (-1, 0)
        case 6:
            if y >= n:
                return 2, (x, 0), (0, -1)
            elif y < 0:
                return 4, (x, n - 1), (0, 1)
            elif x >= n:
                return 5, (y, n - 1), (0, 1)
            elif x < 0:
                return 1, (y, 0), (0, -1)
    return current_side, position, direction


@aoc.part(2)
def part2(items):
    grid = items[0].split("\n")
    instructions = parse(items[1])
    n, cube = make_cube(grid)
    position = (0, 0)
    current_side = 1
    direction = (1, 0)

    for insn in instructions:
        x, y = direction
        if insn == "R":
            direction = (y, -x)
            grid = cube[current_side - 1]
            # print_grid(grid, position, direction)
        elif insn == "L":
            direction = (-y, x)
            grid = cube[current_side - 1]
            # print_grid(grid, position, direction)
        else:
            dir_x, dir_y = direction
            for _ in range(insn):
                x, y = position
                ny = y - dir_y
                nx = x + dir_x
                next_side, (nx, ny), (dx, dy) = walk_off(n, current_side, (nx, ny), direction)

                grid = cube[next_side - 1]
                if grid[ny][nx] == "#":
                    break

                position = (nx, ny)
                direction = (dx, dy)
                dir_x, dir_y = direction
                current_side = next_side
                # print_grid(grid, position, direction)

    sides = [(n, 0), (2 * n, 0), (n, n), (0, 2 * n), (n, 2 * n), (0, 3 * n)]
    x, y = sides[current_side - 1]
    dx, dy = position
    directions = {(1, 0): 0, (-1, 0): 2, (0, 1): 3, (0, -1): 1}
    ans = 1000 * (y + dy + 1) + 4 * (x + dx + 1) + directions[direction]
    return ans


if __name__ == "__main__":
    aoc.solve()
