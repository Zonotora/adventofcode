# flake8: noqa

from python import *

aoc = AdventOfCode("2021", "03", "Binary Diagnostic", new)


@aoc.part(1)
def part1(items):
    n = len(items[0])
    bits = n * [0]

    for line in items:
        for i in range(len(line)):
            if line[i] == "1":
                bits[i] += 1
    string1 = "".join(["1" if b > len(items) / 2 else "0" for b in bits])
    string2 = "".join(["0" if b > len(items) / 2 else "1" for b in bits])
    return int(string1, 2) * int(string2, 2)


def co2(items, inverse=False):
    n = len(items[0])
    for k in range(n):
        bit = 0
        for line in items:
            if line[k] == "1":
                bit += 1
        j = 0
        if inverse:
            keep = "0" if bit >= len(items) / 2 else "1"
        else:
            keep = "1" if bit >= len(items) / 2 else "0"
        while j < len(items):
            if items[j][k] != keep:
                items.pop(j)
                j -= 1
            j += 1
        if len(items) == 1:
            break
    return items[0]


@aoc.part(2)
def part2(items):

    generating = items[:]
    scrubber = items[:]
    val1 = co2(generating)
    val2 = co2(scrubber, inverse=True)
    return int(val1, 2) * int(val2, 2)


if __name__ == "__main__":
    aoc.solve()
