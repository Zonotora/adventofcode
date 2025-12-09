from math import prod
import numpy as np

lines = open("../input/08").read().strip().split("\n")
positions = [[int(x) for x in line.split(",")] for line in lines]

pts = np.array(positions)
dist = np.pow(pts[np.newaxis, :, :] - pts[:, np.newaxis, :], 2).sum(axis=2)

flat = dist.flatten()
indices = np.argsort(flat)
n = len(positions)

circuits = []
seen = set()
count = 0
for k in range(len(indices)):
  index = indices[k]
  i = int(index // n)
  j = int(index % n)
  if i == j: continue
  if (i,j) in seen or (j,i) in seen:
    continue
  seen.add((i, j))
  added = set()
  for index in range(len(circuits)):
    c = circuits[index]
    if i in c or j in c:
      if added:
        added |= c
        circuits.pop(index)
        break
      else:
        c.add(i)
        c.add(j)
        added = c

  if not added:
    circuits.append(set([i, j]))
  count += 1

  if count == 1000:
    lengths = sorted([len(x) for x in circuits])
    ans1 = prod(lengths[-3:])
    print(ans1)

  if len(circuits) == 1 and len(circuits[0]) == 1000:
    ans2 = pts[i][0] * pts[j][0]
    print(ans2)
    break
exit()
