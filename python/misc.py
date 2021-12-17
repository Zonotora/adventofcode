def each_cons(xs, n):
    return [xs[i : i + n] for i in range(len(xs) - n + 1)]


def vhneighbours(arr, i, j):
    pos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    return [
        (j + x, i + y)
        for x, y in pos
        if 0 <= i + y < len(arr) and 0 <= j + x < len(arr[i + y])
    ]


def neighbours(arr, i, j):
    pos = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
        (-1, -1),
        (-1, 1),
        (1, 1),
        (1, -1),
    ]
    return [
        (j + x, i + y)
        for x, y in pos
        if 0 <= i + y < len(arr) and 0 <= j + x < len(arr[i + y])
    ]


def pretty_print(items, pad=2):
    print(
        "\n".join(
            ["".join([f"{item:<{pad}}" for item in row]) for row in items]
        )
    )


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
