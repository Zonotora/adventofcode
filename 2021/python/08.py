# flake8: noqa

from python import *

aoc = AdventOfCode("2021", "08", "Seven Segment Search", new)


@aoc.part(1)
def part1(items):
    cnt = 0
    for line in items:
        out = line.split("|")[1].split()
        for w in out:
            n = len(w)
            if n == 2 or n == 4 or n == 7 or n == 3:
                cnt += 1

    return cnt


@aoc.part(2)
def part2(items):
    cnt = 0
    for line in items:
        pattern = {}
        uniq, out = line.split(" | ")

        for a in uniq.split():
            p = "".join(sorted(a))
            n = len(p)
            if n == 2:
                pattern[1] = p
            elif n == 4:
                pattern[4] = p
        b = 1000
        v = 0
        for a in out.split():
            p = "".join(sorted(a))
            n = len(p)
            if n == 2:
                v += b * 1
            elif n == 3:
                v += b * 7
            elif n == 4:
                v += b * 4
            elif n == 7:
                v += b * 8
            elif all([c in p for c in pattern[1]]):
                # 0, 3, 9
                if n == 5:
                    v += b * 3
                elif sum([1 if c in p else 0 for c in pattern[4]]) == 3:
                    v += b * 0
                else:
                    v += b * 9
            elif n == 6:
                v += b * 6
            elif sum([1 if c in p else 0 for c in pattern[4]]) == 3:
                v += b * 5
            else:
                v += b * 2

            b /= 10
        cnt += v

    return int(cnt)


if __name__ == "__main__":
    aoc.solve()
