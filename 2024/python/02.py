from copy import copy


def sign(n, current):
    if n == 0:
        return current
    elif n > 0:
        return 1
    else:
        return -1


lines = open("../input/02").read().split("\n")


def solve(levels):
    last = levels.pop(0)
    direction = sign(levels[1] - levels[0], 0)
    safe = True
    for level in levels:
        diff = level - last
        if not (1 <= abs(diff) <= 3) or direction != sign(diff, direction):
            safe = False
        last = level
    return safe


part1 = part2 = 0
for line in lines:
    levels = [int(x) for x in line.split()]
    safe = solve(copy(levels))
    part1 += safe
    part2 += safe
    if safe:
        continue

    for i in range(len(levels)):
        new_levels = copy(levels)
        new_levels.pop(i)
        safe = safe or solve(new_levels)

    part2 += safe

print(part1)
print(part2)
