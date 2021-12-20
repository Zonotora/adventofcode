# flake8: noqa

from python import *

aoc = AdventOfCode("2021", "20", "Trench Map", newnew)


def show(image, xmin, xmax, ymin, ymax):
    for i in range(ymin, ymax):
        line = ""
        for j in range(xmin, xmax):
            line += "#" if image[(i, j)] else "."
        print(line)


def enhance(items, n):
    [rule, image] = items
    assert len(rule) == 512
    lights = {}
    for i, j, c in [
        (i, j, c == "#")
        for i, line in enumerate(new(image))
        for j, c in enumerate(line)
    ]:
        lights[(i, j)] = c

    for k in range(n):
        xmin = min(lights, key=lambda x: x[0])[0] - 2
        xmax = max(lights, key=lambda x: x[0])[0] + 3
        ymin = min(lights, key=lambda x: x[1])[1] - 2
        ymax = max(lights, key=lambda x: x[1])[1] + 3
        image = dict(lights)

        for i in range(ymin, ymax):
            for j in range(xmin, xmax):
                index = ""
                for y in range(-1, 2):
                    for x in range(-1, 2):
                        key = (i + y, j + x)

                        if key in lights:
                            index += "1" if lights[key] else "0"
                        else:
                            index += (
                                "0" if rule[0] != "#" or k % 2 == 0 else "1"
                            )

                index = int(index, 2)
                image[(i, j)] = rule[index] == "#"
        lights = image
    return sum([image[key] for key in image])


@aoc.part(1)
def part1(items):
    return enhance(items, 2)


@aoc.part(2)
def part2(items):
    return enhance(items, 50)


if __name__ == "__main__":
    aoc.solve()
