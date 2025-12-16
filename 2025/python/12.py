from dataclasses import dataclass
from functools import cache
import re

parts = open("../input/12").read().strip().split("\n\n")

shapes = []
for p in parts[:-1]:
  lines = p.split("\n")[1:]
  shape = set()
  for i in range(3):
    for j in range(3):
      if lines[i][j] == "#":
        shape.add((i-1,j-1))
  shapes.append(shape)

def pprint(shape):
  for i in range(3):
    for j in range(3):
      if (i-1,j-1) in shape:
        print("#", end="")
      else:
        print(".", end="")
    print()


# rotate + flip = 16 combinations
# try solve for each

transforms = [[] for _ in range(len(shapes))]
for index, shape in enumerate(shapes):
  transforms[index].append(shape)
  for _ in range(3):
    rotated_shape = set()
    for i,j in shape:
      y = j
      x = -i
      rotated_shape.add((y,x))
    shape = rotated_shape
    transforms[index].append(rotated_shape)

  flips = []
  for shape in transforms[index]:
    flips.append(shape)
    for fx,fy in [(-1,-1),(-1,1),(1,-1)]:
      flipped_shape = set()
      for i,j in shape:
        x = j * fx
        y = i * fy
        flipped_shape.add((y,x))
      flips.append(flipped_shape)
  transforms[index].extend(flips)

# merge identical transforms
for i in range(len(transforms)):
  base = [transforms[i][0]]
  for t in transforms[i][1:]:
    add = True
    for b in base:
      if len(t & b) == len(b):
        add = False
        break
    if add:
      base.append(t)
  transforms[i] = base

@dataclass
class Box:
  dim: int
  shapes: list[int]

boxes = []
lines = parts[-1].split("\n")
for line in lines:
  m = re.search(r"([0-9]+)x([0-9]+)", line)
  assert m is not None
  dim = (int(m.group(1)), int(m.group(2)))
  s = [int(x) for x in line.split(":")[1].strip().split()]
  boxes.append(Box(dim, s))

ans = 0
for box in boxes:
  i,j = 0,0
  grid = [[0 for _ in range(box.dim[1])] for _ in range(box.dim[0])]
  while sum(box.shapes) and i < box.dim[0] - 2:
    best = (0, None, None)
    for k in range(len(shapes)):
      if box.shapes[k] > 0:
        for t in transforms[k]:
          count = 0
          taken = False
          for ii,jj in t:
            ii = i + (ii+1)
            jj = j + (jj+1)
            if grid[ii][jj] == 1:
              taken = True
              break
            else:
              count += 1
          if not taken:
            if count > best[0]:
              best = (count, t, k)
    if best[1] is not None:
      for ii,jj in best[1]:
        ii = i + (ii+1)
        jj = j + (jj+1)
        grid[ii][jj] = 1
      box.shapes[best[2]] -= 1
    j += 1
    if j >= box.dim[1] - 2:
      j = 0
      i += 1
  if sum(box.shapes) == 0:
    ans += 1
print(ans)


