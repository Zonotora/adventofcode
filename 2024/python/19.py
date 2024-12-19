import re
from functools import cache

patterns, designs = open("../input/19").read().strip().split("\n\n")
patterns = re.findall(r"[a-z]+", patterns)


@cache
def solve(design):
    ans = len(design) == 0
    for p in patterns:
        if design.startswith(p):
            ans += solve(design[len(p) :])
    return ans


part1 = part2 = 0
for d in designs.split("\n"):
    ways = solve(d)
    part1 += ways > 0
    part2 += ways
print(part1)
print(part2)
