lines = open("../input/06").read().split("\n")

grid = [list(line) for line in lines]
obstacles = set()
ni = len(grid)
nj = len(grid[0])

for i in range(ni):
    for j in range(nj):
        if grid[i][j] == "^":
            si, sj = i, j
        elif grid[i][j] == "#":
            obstacles.add((i, j))


def in_bounds(i, j):
    return 0 <= i < ni and 0 <= j < nj


def step(i, j, di, dj):
    ii, jj = i + di, j + dj
    if (ii, jj) in obstacles:
        return (i, j, dj, -di)
    return (ii, jj, di, dj)


def simulate(i, j, di, dj):
    loop = set()
    while in_bounds(i, j):
        if (i, j, di, dj) in loop:
            return True
        loop.add((i, j, di, dj))
        i, j, di, dj = step(i, j, di, dj)
    return False


di, dj = -1, 0
i, j = si, sj
seen = set()
while in_bounds(i, j):
    seen.add((i, j))
    i, j, di, dj = step(i, j, di, dj)

points = set()
for oi, oj in seen - {(si, sj)}:
    has = (oi, oj) in obstacles
    obstacles.add((oi, oj))
    if simulate(si, sj, -1, 0):
        points.add((oi, oj))
    if not has:
        obstacles.remove((oi, oj))

print(len(seen))
print(len(points))
