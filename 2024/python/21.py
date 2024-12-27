from collections import deque
from functools import cache
from itertools import product

lines = open("../input/21").read().strip().split("\n")
DIR_KEYPAD = [[" ", "^", "A"], ["<", "v", ">"]]
NUM_KEYPAD = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], [" ", "0", "A"]]


def vhneighbours(i, j, I, J):
    pos = [(i - 1, j, "^"), (i + 1, j, "v"), (i, j - 1, "<"), (i, j + 1, ">")]
    return [(ii, jj, move) for ii, jj, move in pos if 0 <= ii < I and 0 <= jj < J]


def compute(keypad):
    positions = {}
    inverse = {}
    I, J = len(keypad), len(keypad[0])
    for i in range(I):
        for j in range(J):
            key = keypad[i][j]
            if key != " ":
                positions[key] = (i, j)
                inverse[(i, j)] = key

    def bfs():
        possibilities = []
        si, sj = positions[t_from]
        q = deque([(si, sj, "")])
        optimal = float("inf")
        while q:
            i, j, moves = q.popleft()
            for ni, nj, move in vhneighbours(i, j, I, J):
                if (ni, nj) not in inverse:
                    continue
                if (ni, nj) == positions[t_to]:
                    if optimal < len(moves):
                        return possibilities
                    optimal = len(moves)
                    possibilities.append(moves + move + "A")
                else:
                    q.append((ni, nj, moves + move))
        return possibilities

    transitions = {}
    for t_from in positions:
        for t_to in positions:
            if t_from == t_to:
                transitions[(t_from, t_to)] = ["A"]
                continue
            transitions[(t_from, t_to)] = bfs()
    return transitions


num_transitions = compute(NUM_KEYPAD)
dir_transitions = compute(DIR_KEYPAD)


@cache
def recur(seq, depth):
    if depth == 0:
        return sum(len(dir_transitions[(t_from, t_to)][0]) for t_from, t_to in zip("A" + seq, seq))

    length = 0
    for t_from, t_to in zip("A" + seq, seq):
        min_length = float("inf")
        for sseq in dir_transitions[(t_from, t_to)]:
            min_length = min(min_length, recur(sseq, depth - 1))
        length += min_length
    return length


def solve(seq, depth):
    ways = product(*[num_transitions[(t_from, t_to)] for t_from, t_to in zip("A" + seq, seq)])
    s = float("inf")
    for way in ways:
        s = min(s, recur("".join(way), depth - 1))
    return s


part1 = part2 = 0
for line in lines:
    value = int(line[:-1])
    part1 += value * solve(line, 2)
    part2 += value * solve(line, 25)

print(part1)
print(part2)
