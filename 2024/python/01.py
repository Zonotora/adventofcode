from collections import Counter

text = [int(x) for x in open("../input/01").read().split()]
left = text[::2]
right = text[1::2]
left.sort()
right.sort()
part1 = sum([abs(left[i] - right[i]) for i in range(len(left))])
print(part1)
c = Counter(right)
part2 = sum([left[i] * c[left[i]] for i in range(len(left))])
print(part2)
