# flake8: noqa

from python import *
import sys
import math
import numpy as np
from collections import defaultdict, deque
from sympy import symbols, solve
import re

aoc = AdventOfCode("2022", "21", "", new)


def find(id, maths, monkeys):
    if id == "humn":
        return None
    if id in monkeys:
        return monkeys[id]
    else:
        op1, op, op2 = maths[id]
        v1 = find(op1, maths, monkeys)
        v2 = find(op2, maths, monkeys)
        if v1 is None or v2 is None:
            return None
        monkeys[id] = eval(f"{v1} {op} {v2}")
        del maths[id]
        return monkeys[id]


def substitute(id, maths, monkeys):
    if id == "humn":
        return "humn"
    if id in maths:
        op1, op, op2 = maths[id]
        op1 = substitute(op1, maths, monkeys)
        op2 = substitute(op2, maths, monkeys)
        id = f"({op1}) {op} ({op2})"
    else:
        id = f"{monkeys[id]}"
    return id


def compute(id, maths, monkeys, value):
    op1, op, op2 = maths[id]

    op1 = substitute(op1, maths, monkeys)
    op2 = substitute(op2, maths, monkeys)
    expr = f"({op1}) {op} ({op2}) - {value}"
    sol = solve(expr)[0]
    return round(sol)


@aoc.part(1)
def part1(items):
    monkeys = {}
    q = deque()
    for line in items:
        id, operation = line.split(":")
        operation = operation.strip()
        if operation.isnumeric():
            monkeys[id] = operation
        else:

            op1, op, op2 = operation.split()
            if op1 in monkeys and op2 in monkeys:
                monkeys[id] = eval(f"{monkeys[op1]} {op} {monkeys[op2]}")
            else:
                q.append((id, op1, op, op2))
    while len(q) > 0:
        id, op1, op, op2 = q.popleft()
        if op1 in monkeys and op2 in monkeys:
            monkeys[id] = eval(f"{monkeys[op1]} {op} {monkeys[op2]}")
        else:
            q.append((id, op1, op, op2))
    return round(monkeys["root"])


@aoc.part(2)
def part2(items):
    monkeys = {}
    maths = {}
    for line in items:
        id, operation = line.split(":")
        operation = operation.strip()
        if operation.isnumeric():
            if id != "humn":
                monkeys[id] = operation
        else:
            op1, op, op2 = operation.split()
            maths[id] = (op1, op, op2)

    op1, op, op2 = maths["root"]
    v1 = find(op1, maths, monkeys)
    v2 = find(op2, maths, monkeys)

    if v1 is None:
        return compute(op1, maths, monkeys, v2)
    else:
        return compute(op2, maths, monkeys, v1)


if __name__ == "__main__":
    aoc.solve()
