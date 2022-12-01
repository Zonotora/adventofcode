def identity(s):
    return s


def space(s):
    return [v.strip() for v in s.strip().split(" ")]


def spaceint(s):
    return [int(v.strip()) for v in s.strip().split(" ")]


def comma(s):
    return [v.strip() for v in s.strip().split(",")]


def commaint(s):
    return [int(v.strip()) for v in s.strip().split(",")]


def new(s):
    return [line.strip() for line in s.strip().split("\n")]


def newint(s):
    return [int(line.strip()) for line in s.strip().split("\n")]


def newnew(s):
    return [line.strip() for line in s.strip().split("\n\n")]


def newnewint(s):
    return [list(map(int, line.split("\n"))) for line in s.strip().split("\n\n")]


def newchar(s):
    return [[c for c in line] for line in s.strip().split("\n")]


def newcharint(s):
    return [[int(c) for c in line] for line in s.strip().split("\n")]
