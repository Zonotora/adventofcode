import re

line = open("../input/03").read()
operators = re.findall(r"(mul\(([0-9]+),([0-9]+)\)|do\(\)|don't\(\))", line)


def solve(part=1):
    s = 0
    enabled = True
    for op, a, b in operators:
        if op == "do()":
            enabled = True
        elif op == "don't()":
            enabled = False
        elif enabled or part == 1:
            s += int(a) * int(b)
    return s


print(solve(1))
print(solve(2))
