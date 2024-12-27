lines = open("../input/25").read().strip().split("\n\n")

locks = []
keys = []
for line in lines:
    schematic = line.split("\n")
    lock = schematic[0].startswith("#")
    grid = [list(x) for x in schematic]
    count = [0] * len(grid[0])
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            count[j] += grid[i][j] == "#"
    for j in range(len(count)):
        count[j] -= 1
    if lock:
        locks.append(count)
    else:
        keys.append(count)


s = 0
for lock in locks:
    for key in keys:
        overlap = False
        for j in range(len(key)):
            if lock[j] + key[j] >= 6:
                overlap = True
        if not overlap:
            s += 1
print(s)
