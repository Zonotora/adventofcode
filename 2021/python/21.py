# flake8: noqa

from python import *
from cachetools import cached

aoc = AdventOfCode("2021", "21", "Dirac Dice", new)

def roll(die):
    s = 0
    for _ in range(3):
        s += die
        die = (die % 100) + 1
    return s, die 


@aoc.part(1)
def part1(items):
    [p1, p2] = [list(map(int, item.split(": ")[1]))[0] for item in items]
    score1, score2 = 0, 0
    die = 1
    times = 0
    while True:
        s, d = roll(die)
        times += 3
        p1 += s
        while p1 > 10:
            p1 -= 10
        score1 += p1
        die = d
        if score1 >= 1000:
            return score2 * times
        s, d = roll(die)
        times += 3
        p2 += s
        while p2 > 10:
            p2 -= 10
        score2 += p2
        die = d
        if score2 >= 1000:
            return score1 * times


@cached(cache={})
def quantum_roll(p1, p2, s1, s2):
    if s1 >= 21:
        return (1,0) 
    if s2 >= 21:
        return (0,1)
    die = [1, 2, 3]
    score = (0,0)
    for d1 in die:
        for d2 in die:
            for d3 in die:
                new_p1 = (p1+d1+d2+d3)
                while new_p1 > 10:
                    new_p1 -= 10
                new_s1 = s1 + new_p1
                x1, x2 = quantum_roll(p2, new_p1, s2, new_s1)
                score = (score[0]+x2,score[1]+x1)
    return score


@aoc.part(2)
def part2(items):
    [p1, p2] = [list(map(int, item.split(": ")[1]))[0] for item in items]
    return max(quantum_roll(p1, p2, 0, 0))


if __name__ == "__main__":
    aoc.solve()
