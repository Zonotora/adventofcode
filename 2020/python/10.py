from itertools import tee, groupby
from functools import reduce

nums = sorted(list(map(int, open("../input/10").read().splitlines())))
nums.insert(0, 0)
nums.append(nums[-1] + 3)

# part 1
a, b = tee(nums)
next(b, None)
part1 = list(map(lambda x: x[1]-x[0], zip(a,b)))
print(part1.count(1) * part1.count(3))

# part 2
trib = { 1: 1, 2: 1, 3: 2, 4: 4, 5: 7}
a, b = tee([list(j) for i, j in groupby(part1)])
next(b, None)
head, *part2 = list(zip(a,b))
part2 = list(filter(lambda x: x[0][0] == 3, part2))
part2 = list(map(lambda x: trib.get(len(x[1]) + 1), part2))
print(trib.get(len(head[0])))
part2 = reduce(lambda x, y: x*y, part2) * trib.get(len(head[0])) * 2
print(part2)
