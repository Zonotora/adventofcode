lines = open("../input/15").read().split("\n\n")

grid, instructions = lines
grid = [list(x) for x in grid.split("\n")]
I = len(grid)
J = len(grid[0])

obstacles = set()
movables = set()

pair_movables = {}
wide_obstacles = set()


for i in range(I):
    for j in range(J):
        if grid[i][j] == "O":
            movables.add((i, j))
            pair_movables[(i, j * 2)] = (i, j * 2 + 1)
            pair_movables[(i, j * 2 + 1)] = (i, j * 2)
        elif grid[i][j] == "#":
            obstacles.add((i, j))
            wide_obstacles.add((i, j * 2))
            wide_obstacles.add((i, j * 2 + 1))
        elif grid[i][j] == "@":
            si, sj = i, j
            wi, wj = i, j * 2


for i in instructions:
    di, dj = 0, 0
    if i == "<":
        dj = -1
    elif i == ">":
        dj = 1
    elif i == "^":
        di = -1
    elif i == "v":
        di = 1
    ni, nj = si + di, sj + dj

    if (ni, nj) in obstacles:
        continue

    if (ni, nj) in movables:
        ti, tj = ni, nj
        while (ti, tj) in movables:
            ti, tj = ti + di, tj + dj

        if (ti, tj) in obstacles:
            continue
        else:
            movables.add((ti, tj))
            movables.remove((ni, nj))

    si, sj = ni, nj


for i in instructions:
    di, dj = 0, 0
    if i == "<":
        dj = -1
    elif i == ">":
        dj = 1
    elif i == "^":
        di = -1
    elif i == "v":
        di = 1
    ni, nj = wi + di, wj + dj

    if (ni, nj) in wide_obstacles:
        continue

    if (ni, nj) in pair_movables:
        other = pair_movables[(ni, nj)]
        check = [(ni, nj), other]
        moves = set()
        cont = False
        while len(check):
            ci, cj = check.pop(0)
            moves.add((ci, cj))
            cii, cjj = ci + di, cj + dj
            if (cii, cjj) in wide_obstacles:
                cont = True
                break
            elif (cii, cjj) in pair_movables and (cii, cjj) not in moves:
                check.append((cii, cjj))
                check.append(pair_movables[(cii, cjj)])
        if cont:
            continue

        tmp = {}
        for key in moves:
            tmp[key] = pair_movables[key]
            del pair_movables[key]

        for mi, mj in moves:
            oi, oj = tmp[(mi, mj)]
            pair_movables[(mi + di, mj + dj)] = (oi + di, oj + dj)

    wi, wj = ni, nj


part1 = part2 = 0
for i, j in movables:
    part1 += i * 100 + j
seen = set()

s = 0
closest = set()
for i, j in pair_movables:
    oi, oj = pair_movables[(i, j)]

    if (i, j) in seen:
        continue
    seen.add((i, j))
    seen.add((oi, oj))
    right = oj if oj > j else j
    left = oj if oj < j else j
    part2 += i * 100 + left

print(part1)
print(part2)
