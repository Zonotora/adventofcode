# flake8: noqa

from python import *
from collections import defaultdict

aoc = AdventOfCode("2021", "07", "", new)


class Instruction:
    def __init__(self, op, operands) -> None:
        self.op = op
        self.operands = operands

    def __repr__(self) -> str:
        return self.op + " " + " ".join(self.operands)


def parse(v, insns, values):
    if v in values:
        return values[v]

    insn = insns[v]
    value = 0
    if insn.op == "NOT":
        key = insn.operands[0]
        x = int(key) if key.isnumeric() else parse(key, insns, values)
        value = (~x) & 0xFFFF
    elif insn.op == "ASSIGN":
        key = insn.operands[0]
        value = int(key) if key.isnumeric() else parse(key, insns, values)
    else:
        key = insn.operands[0]
        x = int(key) if key.isnumeric() else parse(key, insns, values)
        key = insn.operands[1]
        y = int(key) if key.isnumeric() else parse(key, insns, values)

        if insn.op == "RSHIFT":
            value = x >> y
        elif insn.op == "LSHIFT":
            value = x << y
        elif insn.op == "OR":
            value = x | y
        elif insn.op == "AND":
            value = x & y
    values[v] = value
    return value


@aoc.part(1)
def part1(items):
    insns = defaultdict(int)
    for item in items:
        parts = item.split()
        if parts[0] == "NOT":
            insns[parts[3]] = Instruction(parts[0], [parts[1]])
        elif parts[1] == "->":
            insns[parts[2]] = Instruction("ASSIGN", [parts[0]])
        else:
            insns[parts[4]] = Instruction(parts[1], [parts[0], parts[2]])

    return parse("a", insns, dict())


@aoc.part(2)
def part2(items):
    insns = defaultdict(int)
    for item in items:
        parts = item.split()
        if parts[0] == "NOT":
            insns[parts[3]] = Instruction(parts[0], [parts[1]])
        elif parts[1] == "->":
            insns[parts[2]] = Instruction("ASSIGN", [parts[0]])
        else:
            insns[parts[4]] = Instruction(parts[1], [parts[0], parts[2]])
    values = {}
    a = part1(items)
    for key in insns:
        if insns[key].op == "ASSIGN" and insns[key].operands[0].isnumeric():
            values[key] = 0
        if key == "b":
            values[key] = a
    return parse("a", insns, values)


if __name__ == "__main__":
    aoc.solve()
