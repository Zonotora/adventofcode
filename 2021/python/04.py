# flake8: noqa

from python import *

aoc = AdventOfCode("2021", "04", "", newnew)


def check_bingo(board, num):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == num:
                board[i][j] = -1

            if check_item(board[i]) or check_item(
                [board[k][j] for k in range(len(board))]
            ):
                return board


def check_item(items):
    return all([item == -1 for item in items])


def winner(numbers, boards):
    for num in numbers:
        for board in boards:
            b = check_bingo(board, num)
            if b is not None:
                return b, num


def calc_sum(board):
    s = 0
    for row in board:
        for col in row:
            s += col if col != -1 else 0
    return s


@aoc.part(1)
def part1(items):
    numbers = [int(n) for n in items[0].split(",")]

    boards = []
    for b in items[1:]:
        boards.append(
            [[int(c) for c in r.strip().split()] for r in b.split("\n")]
        )

    w, n = winner(numbers, boards)
    s = calc_sum(w)

    return s * n


@aoc.part(2)
def part2(items):
    numbers = [int(n) for n in items[0].split(",")]

    boards = []
    for b in items[1:]:
        boards.append(
            [[int(c) for c in r.strip().split()] for r in b.split("\n")]
        )

    for num in numbers:
        if len(boards) != 1:
            boards = [
                board for board in boards if check_bingo(board, num) is None
            ]
        else:
            b = check_bingo(boards[0], num)
            if b is not None:
                s = calc_sum(boards[0])
                return s * num


if __name__ == "__main__":
    aoc.solve()
