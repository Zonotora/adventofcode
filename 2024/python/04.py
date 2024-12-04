lines = open("../input/04").read().split("\n")


def get(lines, i, j, ii, jj, n):
    s = ""
    for _ in range(n):
        if 0 <= i < len(lines) and 0 <= j < len(lines[i]):
            s += lines[i][j]
        i += ii
        j += jj
    return s


part1 = part2 = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        horizontal = get(lines, i, j, 0, 1, 4)
        vertical = get(lines, i, j, 1, 0, 4)
        r_diagonal = get(lines, i, j, 1, 1, 4)
        l_diagonal = get(lines, i, j, 1, -1, 4)
        values = [horizontal, vertical, r_diagonal, l_diagonal]
        for value in values:
            part1 += value == "XMAS"
            part1 += "".join(reversed(value)) == "XMAS"

        if lines[i][j] == "A":
            r_diagonal = get(lines, i - 1, j - 1, 1, 1, 3)
            l_diagonal = get(lines, i - 1, j + 1, 1, -1, 3)

            if (r_diagonal == "MAS" or "".join(reversed(r_diagonal)) == "MAS") and (
                l_diagonal == "MAS" or "".join(reversed(l_diagonal)) == "MAS"
            ):
                part2 += 1


print(part1)
print(part2)
