from collections import defaultdict, deque

lines = open("../input/22").read().strip().split("\n")

lines = list(map(int, lines))
part1 = 0
part2 = defaultdict(int)
for line in lines:
    secret = line
    last = secret % 10
    window = deque(maxlen=4)
    changes = {}
    for _ in range(2000):
        secret = ((secret * 64) ^ secret) % 16777216
        secret = ((secret // 32) ^ secret) % 16777216
        secret = ((secret * 2048) ^ secret) % 16777216
        price = secret % 10
        change = price - last
        last = price
        window.append(change)
        if len(window) == 4:
            key = tuple(window)
            if key not in changes:
                changes[key] = price
    part1 += secret
    for k, v in changes.items():
        part2[k] += v

print(part1)
print(max(part2.values()))
