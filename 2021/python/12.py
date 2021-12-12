# flake8: noqa

from python import *
from collections import defaultdict, deque

aoc = AdventOfCode("2021", "12", "Passage Pathing", new)


def graph(items, is_twice):
    g = defaultdict(list)
    for f, t in [c.split("-") for c in items]:
        g[f].append(t)
        g[t].append(f)
    cnt = 0
    q = deque([("start", set(["start"]), None)])
    while q:
        v, path, twice = q.popleft()
        if v == "end":
            cnt += 1
            continue
        for n in g[v]:
            if n not in path:
                npath = set(path)
                if n.islower():
                    npath.add(n)
                q.append((n, npath, twice))
            elif is_twice and n != "start" and twice is None:
                q.append((n, path, n))

    return cnt


@aoc.part(1)
def part1(items):
    return graph(items, False)


@aoc.part(2)
def part2(items):
    return graph(items, True)


if __name__ == "__main__":
    aoc.solve()
