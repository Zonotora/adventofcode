import heapq
import math
import re

lines = open("../input/18").read().split("\n")

N = 70
N_BYTES = 1024
INVALID = 99999999
corruptions = [tuple(map(int, reversed(re.findall(r"[0-9]+", line)))) for line in lines]


def h(i, j):
    return math.sqrt((N - i) ** 2 + (N - j) ** 2)


def solve(n):
    corrupted = set(corruptions[:n])

    def vhneighbours(i, j):
        pos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        return [
            (i + ii, j + jj)
            for ii, jj in pos
            if 0 <= i + ii <= N and 0 <= j + jj <= N and (i + ii, j + jj) not in corrupted
        ]

    si, sj = 0, 0
    queue = []
    heapq.heappush(queue, (0, si, sj))
    G = {(i, j): INVALID for i in range(N + 1) for j in range(N + 1)}
    G[(si, sj)] = 0

    while len(queue):
        cost, i, j = heapq.heappop(queue)

        if (i, j) == (N, N):
            break

        for ni, nj in vhneighbours(i, j):
            score = G[(i, j)] + 1
            if score < G[(ni, nj)]:
                G[(ni, nj)] = score
                node = score + h(ni, nj), ni, nj
                heapq.heappush(queue, node)
    return G


G = solve(N_BYTES)
print(G[(N, N)])
lo, hi = N_BYTES, len(corruptions)
while lo < hi:
    mid = (lo + hi) // 2
    G = solve(mid)
    if G[(N, N)] == INVALID:
        hi = mid
    else:
        lo = mid + 1
print(",".join(map(str, (reversed(corruptions[mid - 1])))))
