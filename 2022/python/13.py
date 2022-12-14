# flake8: noqa

from python import *
import sys
import numpy as np
from collections import defaultdict
import re
from copy import deepcopy

aoc = AdventOfCode("2022", "13", "", newnew)


def compare(l1, l2):
    ok = empty(l1, l2, 0)
    if len(l1) == 0 and len(l2) == 0 or ok != 0:
        return l1, l2, ok

    item1 = l1.pop(0)
    item2 = l2.pop(0)
    # print(item1, item2)
    ok = 0

    if isinstance(item1, list) or isinstance(item2, list):
        if isinstance(item1, list) and isinstance(item2, list):
            item1, item2, ok = compare(item1, item2)
        elif isinstance(item1, list):
            item1, item2, ok = compare(item1, [item2])
        elif isinstance(item2, list):
            item1, item2, ok = compare([item1], item2)

        if ok != 0:
            return [], [], ok

        while len(item1) > 0 and len(item2) > 0 and ok == 0:
            item1, item2, ok = compare(item1, item2)

        if ok != 0:
            return [], [], ok

        ok = empty(item1, item2, ok)
    else:
        if item1 > item2:
            ok = 2
        elif item1 < item2:
            ok = 1

    return l1, l2, ok


def empty(l1, l2, ok):
    if len(l1) == 0 and len(l2) == 0:
        return 0
    elif len(l1) == 0 and len(l2) > 0:
        return 1
    elif len(l2) == 0 and len(l1) > 0:
        return 2
    return ok


@aoc.part(1)
def part1(items):
    indices = []
    for k, packet in enumerate(items):
        p1, p2 = packet.split("\n")
        l1 = eval(p1)
        l2 = eval(p2)

        _, _, ok = compare([l1], [l2])

        if ok == 1:
            indices.append(k)

    return sum(map(lambda x: x + 1, indices))


@aoc.part(2)
def part2(items):
    packets = []
    items.extend(["[[2]]\n[[6]]"])
    for packet in items:
        p1, p2 = packet.split("\n")
        l1 = eval(p1)
        l2 = eval(p2)

        for l in [l1, l2]:
            has_inserted = False
            for i in range(len(packets)):
                p = packets[i]
                _, _, ok = compare(deepcopy([l]), deepcopy([p]))
                if ok == 0 or ok == 1:
                    packets.insert(i, l)
                    has_inserted = True
                    break
            if not has_inserted:
                packets.append(l)
    s = 1
    for i, p in enumerate(packets):
        if str(p) == "[[2]]" or str(p) == "[[6]]":
            s *= i + 1

    return s


if __name__ == "__main__":
    aoc.solve()
