from collections import defaultdict

lines = open("../input/20").read().strip().split("\n")
grid = [list(x) for x in lines]
I = len(grid)
J = len(grid[0])

obstacles = set()
valid = set()
for i in range(I):
    for j in range(J):
        if grid[i][j] == "#":
            obstacles.add((i, j))
        elif grid[i][j] == "S":
            si, sj = i, j
        elif grid[i][j] == "E":
            valid.add((i, j))
            ei, ej = i, j
        elif grid[i][j] == ".":
            valid.add((i, j))


def vhneighbours(i, j, n=1):
    pos = [(-1 * n, 0), (1 * n, 0), (0, -1 * n), (0, 1 * n)]
    return [
        (i + ii, j + jj) for ii, jj in pos if 0 <= i + ii < I and 0 <= j + jj < J and (i + ii, j + jj) not in obstacles
    ]


path = []
ci, cj = si, sj
while (ci, cj) != (ei, ej):
    path.append((ci, cj))
    for ni, nj in vhneighbours(ci, cj):
        if len(path) >= 2 and (ni, nj) == path[-2]:
            continue
        ci, cj = ni, nj
path.append((ei, ej))


def solve(n):
    reachable = set()
    for i in range(-n + 1, n):
        for j in range(-n + abs(i) + 1, n - abs(i)):
            reachable.add((i, j))

    saves = defaultdict(int)
    for i in range(len(path)):
        ci, cj = path[i]
        points = set(map(lambda x: (ci + x[0], cj + x[1]), reachable)) & valid
        time = len(path) - i
        for ni, nj in points:
            manhattan = abs(ci - ni) + abs(cj - nj)
            cheat_time = len(path) - path.index((ni, nj)) + manhattan
            if time - cheat_time <= 0:
                continue
            saves[time - cheat_time] += 1

    s = 0
    for save in saves:
        if save >= 100:
            s += saves[save]
    return s


print(solve(3))
print(solve(21))
