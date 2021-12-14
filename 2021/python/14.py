# flake8: noqa

from python import *
from collections import defaultdict

aoc = AdventOfCode("2021", "14", "Extended Polymerization", newnew)


def polymerization(items, n):
    main = items[0]
    cmds = [c.split(" -> ") for c in items[1].split("\n")]
    pairs = defaultdict(list)
    for a, b in cmds:
        pairs[a].append(a[0] + b)
        pairs[a].append(b + a[1])
    c = defaultdict(int)
    for i in range(len(main) - 1):
        c[main[i : i + 2]] += 1
    for i in range(n):
        old = dict(c)
        for k, v in old.items():
            [p1, p2] = pairs[k]
            c[p1] += v
            c[p2] += v
            c[k] -= v
    l = defaultdict(int)
    for k, v in c.items():
        l[k[0]] += v
    l[main[-1]] += 1
    c = sorted(l.items(), key=lambda x: x[1])
    return c[-1][1] - c[0][1]


@aoc.part(1)
def part1(items):
    return polymerization(items, 10)


@aoc.part(2)
def part2(items):
    return polymerization(items, 40)


if __name__ == "__main__":
    aoc.solve()
