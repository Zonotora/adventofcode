# flake8: noqa

from python import *

aoc = AdventOfCode("2021", "17", "", new)

def trajectory(items, p1):
    s = items[0].split("=")
    [xmin, xmax] = [int(v) for v in s[1].split(",")[0].split("..")]
    [ymin, ymax] = [int(v) for v in s[2].split("..")]
    d = 300
    answer = 0
    for i in range(0, d):
        for j in range(-d, d):
            cmax = 0
            x, y = 0, 0
            vx, vy = i, j
            while True:
                x += vx
                y += vy
                if vx != 0:
                    vx += -sign(vx)
                vy -= 1
                cmax = max(cmax, y)

                if xmin <= x <= xmax and ymin <= y <= ymax:
                    if p1:
                        answer = max(answer, cmax)
                    else:
                        answer += 1
                    break
                if y <= ymin:
                    break
    return answer


@aoc.part(1)
def part1(items):
    return trajectory(items, True)

@aoc.part(2)
def part2(items):
    return trajectory(items, False)



if __name__ == "__main__":
    aoc.solve()
