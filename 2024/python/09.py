lines = open("../input/09").read()
fs = list(lines)
files = [int(x) for x in fs[::2]]
free = [int(x) for x in fs[1::2]]
file_info = {}
free_info = []

new = []
index = 0
for i, file in enumerate(files):
    new.extend([i] * file)
    file_info[i] = (index, file)
    index += file
    if free:
        e = free.pop(0)
        free_info.append((index, e))
        new.extend([-1] * e)
        index += e


def checksum(new):
    c = 0
    for i, file in enumerate(new):
        if file != -1:
            c += i * file
    return c


def part1(new):
    i = 0
    new = new[::]
    while i < len(new):
        last = new.pop()
        if last != -1:
            while i < len(new) and new[i] != -1:
                i += 1
            if i >= len(new):
                new.append(last)
                break
            new[i] = last
            i += 1
    return new


def part2(new):
    for id, (start, size) in reversed(file_info.items()):
        remove = -1
        for j in range(len(free_info)):
            fstart, fsize = free_info[j]
            if fstart > start:
                break

            if size <= fsize:
                for i in range(fstart, fstart + size):
                    new[i] = id
                for i in range(start, start + size):
                    new[i] = -1
                free_info[j] = (fstart + size, fsize - size)
                if fsize - size == 0:
                    remove = j
                break
        if remove != -1:
            free_info.pop(remove)
    return new


print(checksum(part1(new)))
print(checksum(part2(new)))
