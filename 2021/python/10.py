# flake8: noqa

from python import *

aoc = AdventOfCode("2021", "10", "", new)

scores1 = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

matching = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}


@aoc.part(1)
def part1(items):
    score = 0
    for item in items:
        queue = []
        for c in item:
            if c in [">", ")", "]", "}"]:
                left = queue.pop()
                if left != matching[c]:
                    score += scores1[c]
                    break
                continue

            queue.append(c)

    return score


scores2 = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}


@aoc.part(2)
def part2(items):
    scores = []
    for item in items:
        score = 0
        queue = []
        faulty = False
        for c in item:
            if c in [">", ")", "]", "}"]:
                left = queue.pop()
                if left != matching[c]:
                    faulty = True
                    break
                continue

            queue.append(c)
        if not faulty:
            while len(queue) > 0:
                c = queue.pop()
                score = score * 5 + scores2[c]

            scores.append(score)
    return sorted(scores)[len(scores) // 2]


if __name__ == "__main__":
    aoc.solve()
