# flake8: noqa

from python import *

aoc = AdventOfCode("2021", "08", "", new)


@aoc.part(1)
def part1(items):
    st_code = 0
    st_string = 0
    for line in items:
        i = 0
        s_code = 0
        while i < len(line) - 1:
            if line[i] == "\\" and line[i + 1] == "x":
                s_code += 1
                i += 3
            elif line[i] == "\\" and line[i + 1] == '"':
                s_code += 1
                i += 1
            elif line[i] == "\\" and line[i + 1] == "\\":
                s_code += 1
                i += 1
            elif line[i] != '"':
                s_code += 1

            i += 1

        st_string += len(line)
        st_code += s_code
    return st_string - st_code


@aoc.part(2)
def part2(items):
    s_original, s_new = 0, 0
    for line in items:
        s_original += len(line)
        line = line.replace("\\", "\\\\")
        line = line.replace('"', '\\"')
        line = '"' + line + '"'
        s_new += len(line)
    return s_new - s_original


if __name__ == "__main__":
    aoc.solve()
