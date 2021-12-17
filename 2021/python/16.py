# flake8: noqa

from python import *

aoc = AdventOfCode("2021", "16", "Packet Decoder", new)


def receive(b, p):
    version = 0
    literal = 0
    while p < len(b) - 6:
        v = b[p+0:p+3]
        version += int(v, 2)
        t = int(b[p+3:p+6], 2)
        p += 6
        if t == 4:
            groups = []
            while b[p] == "1":
                groups.append(b[p+1:p+5])
                p += 5
            groups.append(b[p+1:p+5])
            p += 5
            literal = "".join(groups)
            literal = int(literal, 2)
            return [version, p, literal]
        else:
            i = b[p]
            literals = []
            p += 1
            if i == "1": #length id
                nsub = b[p:p+11]
                p += 11
                for _ in range(int(nsub, 2)):
                    [nv, np, nl] = receive(b, p)
                    version += nv 
                    p = np
                    literals.append(nl)
            else:
                length = int(b[p:p+15], 2)
                p += 15
                while length > 0:
                    [nv, np, nl] = receive(b, p)
                    version += nv 
                    length -= np - p
                    p = np
                    literals.append(nl)
            if t == 0:
                return [version, p, sum(literals)]
            elif t == 1:
                a = 1
                for l in literals:
                    a *= l
                return [version, p, a]
            elif t == 2:
                return [version, p, min(literals)]
            elif t == 3:
                return [version, p, max(literals)]
            elif t == 5:
                return [version, p, 1 if literals[0] > literals[1] else 0]
            elif t == 6:
                return [version, p, 1 if literals[0] < literals[1] else 0]
            elif t == 7:
                return [version, p, 1 if literals[0] == literals[1] else 0]


    return [version, p, literal]
                


@aoc.part(1)
def part1(items):
    s = items[0]
    b = bin(int(s, 16))[2:]
    while len(b) < 4*len(s):
        b = '0'+b
    [version, _, _] = receive(b, 0)
    return version


@aoc.part(2)
def part2(items):
    s = items[0]
    b = bin(int(s, 16))[2:]
    while len(b) < 4*len(s):
        b = '0'+b
    [_, _, literal] = receive(b, 0)
    return literal


if __name__ == "__main__":
    aoc.solve()
