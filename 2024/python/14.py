import re
from collections import defaultdict
from math import prod

lines = open("../input/14").read().split("\n")


robots = []
for line in lines:
    x, y, dx, dy = map(int, re.findall(r"-?[0-9]+", line))
    robots.append((x, y, dx, dy))

Y = 103
X = 101
y_mid = Y // 2
x_mid = X // 2


def solve1():
    quadrants = [0, 0, 0, 0]
    for x, y, _dx, _dy in robots:
        if x < x_mid and y < y_mid:
            quadrants[0] += 1
        elif x > x_mid and y < y_mid:
            quadrants[1] += 1
        elif x < x_mid and y > y_mid:
            quadrants[2] += 1
        elif x > x_mid and y > y_mid:
            quadrants[3] += 1
    return prod(quadrants)


part1 = part2 = i = 0
while True:
    robot_set = defaultdict(int)
    skip = False
    for j in range(len(robots)):
        x, y, dx, dy = robots[j]
        nx = (x + dx) % X
        ny = (y + dy) % Y
        robots[j] = (nx, ny, dx, dy)
        robot_set[(x, y)] += 1
        if robot_set[(x, y)] > 1:
            skip = True
    if not skip:
        part2 = i
        break
    if i == 100 - 1:
        part1 = solve1()
    i += 1


print(part1)
print(part2)
