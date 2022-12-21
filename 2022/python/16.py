# flake8: noqa

from python import *
import sys
import numpy as np
from collections import deque
import re

aoc = AdventOfCode("2022", "16", "", new)


class Valve:
    def __init__(self, id, rate, exits) -> None:
        self.id = id
        self.rate = rate
        self.exits = exits

    def __str__(self) -> str:
        return f"{self.id} {self.rate} {self.exits}"


def parse(items):
    valves = {}
    for i, line in enumerate(items):
        valve, *exits = re.findall("[A-Z][A-Z]", line)
        # exits = list(zip(exits, [1 for _ in range(len(exits))]))
        rate = int(re.findall(r"\d+", line)[0])
        valves[valve] = Valve(i, rate, exits)

    keys = sorted(valves)
    indices = [i for i, k in enumerate(keys) if valves[k].rate > 0 or k == "AA"]
    n = len(keys)
    dist = np.zeros((n, n))

    for i, k in enumerate(keys):
        q = deque([(k, 0)])
        seen = set()
        while q:
            e, value = q.popleft()
            j = keys.index(e)
            if e not in seen:
                if k == e:
                    value = 0
                dist[i, j] = value
                seen.add(e)

            for ee in valves[e].exits:
                if ee not in seen:
                    q.append((ee, value + 1))

    mask = np.ix_(indices, indices)
    filtered_keys = [keys[i] for i in indices]
    return valves, filtered_keys, dist[mask]


def compute(cache, t, valves, i, seen, keys, dist):
    key = (t, seen, i)
    if key in cache:
        return cache[key]

    max_value = 0
    for j in range(1, len(keys)):
        if dist[i][j] == 0:
            continue

        e = valves[keys[j]]

        mask = 1 << j
        # print(f"{j} {mask:b} {seen:b} {mask & seen}")
        # input()
        if mask & seen:
            continue

        remaining_time = t - dist[i][j] - 1
        if remaining_time <= 0:
            continue

        nxt_value = remaining_time * e.rate
        nxt = compute(cache, remaining_time, valves, j, mask | seen, keys, dist) + nxt_value
        max_value = max(max_value, nxt)

    cache[key] = max_value

    return max_value


@aoc.part(1)
def part1(items):
    valves, keys, dist = parse(items)
    return int(compute({}, 30, valves, 0, 1, keys, dist))


@aoc.part(2)
def part2(items):
    valves, keys, dist = parse(items)

    b = (1 << len(keys)) - 1
    max_value = 0
    cache = {}
    for i in range((b + 1) // 2):
        fst = int(compute(cache, 26, valves, 0, i, keys, dist))
        snd = int(compute(cache, 26, valves, 0, b ^ i, keys, dist))
        max_value = max(max_value, fst + snd)

    return max_value


if __name__ == "__main__":
    aoc.solve()
