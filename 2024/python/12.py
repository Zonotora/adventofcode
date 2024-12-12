lines = open("../input/12").read().split("\n")

grid = [list(x) for x in lines]
I = len(grid)
J = len(grid[0])


def vhneighbours(i, j):
    pos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    return [(i + ii, j + jj) for ii, jj in pos]


groups = []
seen = set()
part1 = part2 = 0
for i in range(I):
    for j in range(J):
        if (i, j) in seen:
            continue
        lseen = set([(i, j)])
        stack = vhneighbours(i, j)
        group = set([(i, j)])
        perimeter = 0
        while len(stack):
            ii, jj = stack.pop(0)
            if (ii, jj) in lseen:
                continue
            if not (0 <= ii < I and 0 <= jj < J):
                perimeter += 1
            elif grid[i][j] == grid[ii][jj]:
                group.add((ii, jj))
                lseen.add((ii, jj))
                stack.extend(vhneighbours(ii, jj))
            else:
                perimeter += 1
        part1 += perimeter * len(group)
        seen = seen | lseen
        groups.append(group)


def solve2(min_i, max_i, min_j, max_j, di, dj):
    sides = 0
    for ii in range(min_i, max_i + 1):
        top = bottom = 0
        for jj in range(min_j, max_j + 1):
            # make sure we have the right index depending on
            # horizontal or vertical scan
            i, j = (ii, jj) if di else (jj, ii)

            if (i, j) in group:
                # if (i, j) in group we add side to top/left or bottom/right
                top += (i - di, j - dj) not in group
                bottom += (i + di, j + dj) not in group
                # if top/left is in group we have a break
                if (i - di, j - dj) in group:
                    sides += top != 0
                    top = 0
                # if bottom/right is in group we have a break
                if (i + di, j + dj) in group:
                    sides += bottom != 0
                    bottom = 0
            else:
                # if (i, j) not in group we add to side and reset
                sides += top != 0
                sides += bottom != 0
                top = bottom = 0

        # since the whole block may be in the group we add here as well
        sides += top != 0
        sides += bottom != 0
    return sides


for group in groups:
    min_i = min(group, key=lambda x: x[0])[0]
    max_i = max(group, key=lambda x: x[0])[0]
    min_j = min(group, key=lambda x: x[1])[1]
    max_j = max(group, key=lambda x: x[1])[1]
    # horizontally
    sides = solve2(min_i, max_i, min_j, max_j, 1, 0)
    # vertically
    sides += solve2(min_j, max_j, min_i, max_i, 0, 1)
    part2 += sides * len(group)

print(part1)
print(part2)
