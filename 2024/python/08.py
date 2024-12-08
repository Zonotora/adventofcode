from collections import defaultdict
from itertools import combinations

lines = open("../input/08").read().split("\n")

grid = [list(line) for line in lines]
I = len(grid)
J = len(grid[0])

antennas = defaultdict(list)
vantennas = {}
for i in range(I):
    for j in range(J):
        if grid[i][j] != ".":
            antennas[grid[i][j]].append((i, j))
            vantennas[(i, j)] = grid[i][j]

part1 = set()
part2 = set()
for a in antennas:
    c = combinations(antennas[a], 2)
    for (i1, j1), (i2, j2) in c:
        di = i2 - i1
        dj = j2 - j1
        n1 = (i1 - di, j1 - dj)
        n2 = (i2 + di, j2 + dj)
        # part 1
        for ni, nj in [n1, n2]:
            if 0 <= ni < I and 0 <= nj < J:
                part1.add((ni, nj))

        # part 2
        ni = i1 - di
        nj = j1 - dj
        while 0 <= ni < I and 0 <= nj < J:
            ni, nj = ni - di, nj - dj

        ni, nj = ni + di, nj + dj
        while 0 <= ni < I and 0 <= nj < J:
            part2.add((ni, nj))
            ni, nj = ni + di, nj + dj
print(len(part1))
print(len(part2))
