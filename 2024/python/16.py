import heapq
from collections import defaultdict, deque

lines = open("../input/16").read().split("\n")
grid = [list(x) for x in lines]
I = len(grid)
J = len(grid[0])
INVALID = float("inf")

for i in range(I):
    for j in range(J):
        if grid[i][j] == "S":
            si, sj = i, j

pq = [(0, si, sj, 0, 1)]
G = {(i, j, di, dj): INVALID for i in range(I) for j in range(J) for (di, dj) in [(0, 1), (0, -1), (1, 0), (-1, 0)]}
G[(si, sj, 0, 1)] = 0
best_cost = INVALID
end = set()
backtrack = defaultdict(set)

while pq:
    cost, i, j, di, dj = heapq.heappop(pq)

    if grid[i][j] == "E":
        if cost > best_cost:
            break
        best_cost = cost
        end.add((i, j, di, dj))

    neighbours = [(1, i + di, j + dj, di, dj), (1000, i, j, dj, -di), (1000, i, j, -dj, di)]
    for penalty, ni, nj, ndi, ndj in neighbours:
        if grid[ni][nj] == "#":
            continue
        lowest = G.get((ni, nj, ndi, ndj))
        score = cost + penalty
        if score > lowest:
            continue
        if score < lowest:
            G[(ni, nj, ndi, ndj)] = score
            backtrack[(ni, nj, ndi, ndj)] = set()
        backtrack[(ni, nj, ndi, ndj)].add((i, j, di, dj))
        heapq.heappush(pq, (score, ni, nj, ndi, ndj))

path = deque(end)
seen = set(end)

while path:
    key = path.popleft()

    for last in backtrack.get(key, []):
        if last in seen:
            continue
        seen.add(last)
        path.append(last)

print(best_cost)
print(len({(i, j) for i, j, _, _ in seen}))
