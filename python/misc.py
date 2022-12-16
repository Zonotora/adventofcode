def each_cons(xs, n):
    return [xs[i : i + n] for i in range(len(xs) - n + 1)]


def vhneighbours(arr, i, j):
    pos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    return [(j + x, i + y) for x, y in pos if 0 <= i + y < len(arr) and 0 <= j + x < len(arr[i + y])]


def neighbours(arr, i, j):
    pos = [
        (-1, -1),
        (0, -1),
        (1, -1),
        (-1, 0),
        (1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
    ]
    return [(j + x, i + y) for x, y in pos if 0 <= i + y < len(arr) and 0 <= j + x < len(arr[i + y])]


def pretty_print(items, pad=2):
    print("\n".join(["".join([f"{item:<{pad}}" for item in row]) for row in items]))


def sign(n):
    if n >= 0:
        return 1
    else:
        return -1


def prod(items):
    a = 1
    for item in items:
        a *= item
    return a


class Interval:
    def __init__(self) -> None:
        self.parts = []

    def __str__(self) -> str:
        return f"{self.parts}"

    def __repr__(self) -> str:
        return f"{self.parts}"

    def add(self, x1, x2):
        assert x1 <= x2
        interval = [x1, x2]
        parts = []

        for sx, ex in self.parts:
            if x1 <= sx <= ex <= x2:
                continue
            elif ex < x1 or sx > x2:
                parts.append([sx, ex])

            if sx < x1 <= ex:
                interval[0] = sx
            if sx <= x2 < ex:
                interval[1] = ex

        parts.append(interval)
        self.parts = sorted(parts, key=lambda x: x[0])

    def sum(self):
        s = 0
        for sx, ex in self.parts:
            s += ex - sx
        return s
