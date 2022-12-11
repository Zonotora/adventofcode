# flake8: noqa

from python import *
import sys
import numpy as np
from collections import defaultdict
import re

aoc = AdventOfCode("2022", "11", "", newnew)

class Monkey:
    def __init__(self, id, items, new, div, true, false):
        self.id = int(id)
        self.items = list(map(int, items))
        self.new = new
        self.div = int(div)
        self.true = int(true)
        self.false = int(false)

    def update(self, value):
        fst, op, snd = self.new
        fst = value if fst == "old" else int(fst)
        snd = value if snd == "old" else int(snd)
        match op:
            case "+": return fst + snd
            case "*": return fst * snd


    def __str__(self):
        return f"{self.id}: {self.items}"

def get_monkeys(items):
    monkeys = []
    for m in items:
        lines = m.split("\n")
        id = re.findall("\d+", lines[0])[0]
        s_items = re.findall("\d+", lines[1])
        new = lines[2].split("=")[1].split()
        div = re.findall("\d+", lines[3])[0]
        true = re.findall("\d+", lines[4])[0]
        false = re.findall("\d+", lines[5])[0]
        monkey = Monkey(id, s_items, new, div, true, false)
        monkeys.append(monkey)
    return monkeys

@aoc.part(1)
def part1(items):
    monkeys = get_monkeys(items)
    cnt = [0] * len(monkeys)
    for r in range(20):
        items = [[] for _ in range(len(monkeys))]
        for i, m in enumerate(monkeys):
            n = len(m.items)
            for k in range(n):
                item = m.items.pop(0)
                cnt[i] += 1
                item = m.update(item)
                item //= 3
                if item % m.div == 0:
                    nid = m.true
                else:
                    nid = m.false
                monkeys[nid].items.append(item)

    return  prod(sorted(cnt)[-2:])


@aoc.part(2)
def part2(items):
    monkeys = get_monkeys(items)
    cnt = [0] * len(monkeys)
    p = prod([m.div for m in monkeys])
    for r in range(10000):
        items = [[] for _ in range(len(monkeys))]
        for i, m in enumerate(monkeys):
            n = len(m.items)
            for k in range(n):
                item = m.items.pop(0)
                cnt[i] += 1
                item = m.update(item)
                if item % m.div == 0:
                    nid = m.true
                else:
                    nid = m.false
                monkeys[nid].items.append(item)


        for m in monkeys:
            for i in range(len(m.items)):
                m.items[i] %= p

    return  prod(sorted(cnt)[-2:])


if __name__ == "__main__":
    aoc.solve()