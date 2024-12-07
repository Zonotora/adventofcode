import numpy as np

lines = open("../input/07").read().split("\n")


def get_op(x):
    return {"0": "+", "1": "*", "2": "||"}[x]


def solve(part=1):
    s = 0
    base = part + 1
    for line in lines:
        result, values = line.split(":")
        values = [int(x) for x in values.split()]
        result = int(result)

        for i in range(base ** (len(values) - 1)):
            ternary = np.base_repr(i, base=base)
            ternary = "0" * (len(values) - 1 - len(ternary)) + ternary
            operators = [get_op(x) for x in ternary]
            acc = values[0]
            for j in range(len(operators)):
                if operators[j] == "+":
                    acc += values[j + 1]
                elif operators[j] == "*":
                    acc *= values[j + 1]
                else:
                    acc = int(str(acc) + str(values[j + 1]))
            if result == acc:
                s += result
                break
    return s


print(solve(part=1))
print(solve(part=2))
