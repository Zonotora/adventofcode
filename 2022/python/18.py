# flake8: noqa

from python import *
import sys
import numpy as np
from collections import defaultdict, deque
import re

aoc = AdventOfCode("2022", "18", "", new)


class Face:
    def __init__(self, vertices) -> None:
        self.vertices = vertices

    def __getitem__(self, i):
        return self.vertices[i]

    def __eq__(self, o: object) -> bool:
        h1 = hash(tuple([item for v in self.vertices for item in v]))
        h2 = hash(tuple([item for v in o.vertices for item in v]))
        return h1 == h2

    def __hash__(self) -> int:
        return hash(tuple([item for v in self.vertices for item in v]))

    def __str__(self) -> str:
        return " ".join([str(v) for v in self.vertices])


def parse(x, y, z):
    vertices = []
    for i in range(2):
        for j in range(2):
            for k in range(2):
                dx = 0.5 if j == 0 else -0.5
                dy = 0.5 if i == 0 else -0.5
                dz = 0.5 if k == 0 else -0.5
                vertices.append((x + dx, y + dy, z + dz))
    sides = [
        Face(vertices[:4]),
        Face(vertices[4:]),
        Face(vertices[:2] + vertices[4:6]),
        Face(vertices[2:4] + vertices[6:]),
        Face(vertices[1::2]),
        Face(vertices[::2]),
    ]

    return sides


def compute(items):
    faces = set()
    blocked = set()
    for line in items:
        x, y, z = list(map(int, line.split(",")))
        sides = parse(x, y, z)
        for side in sides:
            if side in faces and side not in blocked:
                blocked.add(side)
            faces.add(side)
    return faces - blocked


def walk(cubes, position, index, dir, min_bound, max_bound):
    position = list(position)
    while min_bound < position[index] < max_bound:
        position[index] += dir
        if tuple(position) in cubes:
            return True
    return False


def check(cubes, position, min_x, max_x, min_y, max_y, min_z, max_z):
    directions = [
        walk(cubes, position, 0, 1, min_x, max_x),
        walk(cubes, position, 0, -1, min_x, max_x),
        walk(cubes, position, 1, 1, min_y, max_y),
        walk(cubes, position, 1, -1, min_y, max_y),
        walk(cubes, position, 2, 1, min_z, max_z),
        walk(cubes, position, 2, -1, min_z, max_z),
    ]
    return all(directions)


@aoc.part(1)
def part1(items):
    surface = compute(items)
    return len(surface)


@aoc.part(2)
def part2(items):
    surface = compute(items)
    cubes = set()
    interior = set()
    max_x, min_x = -sys.maxsize, sys.maxsize
    max_y, min_y = -sys.maxsize, sys.maxsize
    max_z, min_z = -sys.maxsize, sys.maxsize

    for line in items:
        x, y, z = list(map(int, line.split(",")))
        cubes.add((x, y, z))
        max_x, min_x = max(max_x, x), min(min_x, x)
        max_y, min_y = max(max_y, y), min(min_y, y)
        max_z, min_z = max(max_z, z), min(min_z, z)

    for xx in range(min_x, max_x + 1):
        for yy in range(min_y, max_y + 1):
            for zz in range(min_z, max_z + 1):
                position = (xx, yy, zz)
                if position in cubes:
                    continue
                if check(cubes, position, min_x, max_x, min_y, max_y, min_z, max_z):
                    interior.add(position)

    blocked = set()
    for x, y, z in interior:
        sides = parse(x, y, z)
        for s in sides:
            if s in surface:
                blocked.add(s)

    surface = surface - blocked

    return len(surface)


if __name__ == "__main__":
    aoc.solve()
