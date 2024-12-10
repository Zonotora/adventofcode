from collections import defaultdict

lines = open("../input/10").read().split("\n")
grid = [[int(y) if y != "." else y for y in x] for x in lines]
I = len(grid)
J = len(grid[0])
nodes = defaultdict(list)
start_nodes = []


def vhneighbours(i, j):
    pos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    return [(i + ii, j + jj) for ii, jj in pos if 0 <= i + ii < I and 0 <= j + jj < J]


for i in range(I):
    for j in range(J):
        if grid[i][j] == ".":
            continue
        if grid[i][j] == 0:
            start_nodes.append((i, j))

        neighbours = vhneighbours(i, j)

        for ii, jj in neighbours:
            if grid[ii][jj] == ".":
                continue

            if grid[i][j] + 1 == grid[ii][jj]:
                nodes[(i, j)].append((ii, jj))


part1 = part2 = 0
for key in start_nodes:
    unique = set()
    link = nodes[key]
    stack = nodes[key][::]
    while len(stack):
        i, j = stack.pop(0)
        if grid[i][j] == 9:
            unique.add((i, j))
            part2 += 1
        stack.extend(nodes[(i, j)])
    part1 += len(unique)

print(part1)
print(part2)
