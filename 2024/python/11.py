from collections import Counter


def solve(part=1):
    stones = Counter(open("../input/11").read().split())
    for _ in range(25 if part == 1 else 75):
        blink = Counter()
        for key in stones:
            if key == "0":
                blink["1"] += stones[key]
            elif len(key) % 2 == 0:
                left = key[: len(key) // 2]
                right = str(int(key[len(key) // 2 :]))
                blink[left] += stones[key]
                blink[right] += stones[key]
            else:
                blink[str(int(key) * 2024)] += stones[key]
        stones = blink
    return sum(stones.values())


print(solve(part=1))
print(solve(part=2))
