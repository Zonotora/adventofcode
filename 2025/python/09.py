import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

lines = open("../input/09").read().strip().split("\n")

coords = []
for line in lines:
  [x,y] = [int(x) for x in line.split(",")]
  coords.append((x, y))

pts = np.array(coords)
dist = (np.abs(pts[np.newaxis, :, :] - pts[:, np.newaxis, :]) + 1).prod(axis=2)
ans1 = np.max(dist)
print(ans1)




prev = coords[-1]
max_length = [0, 0]
points = [(), ()]
for x,y in coords:
  length = abs(x - prev[0])
  if length > max_length[0]:
    max_length[1] = max_length[0]
    max_length[0] = length
    points[1] = points[0]
    points[0] = (max(x, prev[0]), max(y,prev[1]))
  elif length > max_length[1]:
    max_length[1] = length
    points[1] = (max(x, prev[0]), max(y,prev[1]))
  prev = (x,y)


if points[0][1] > points[1][1]:
  upper = points[0]
  lower = points[1]
else:  
  lower = points[0]
  upper = points[1]


ans2 = 0
ms = []
max_rect = ()

for p1 in coords:
  for p2 in coords:
    if p1[0] == p2[0] or p1[1] == p2[1]: continue
    min_x = min(p1[0],p2[0])
    min_y = min(p1[1],p2[1])
    max_x = max(p1[0],p2[0])
    max_y = max(p1[1],p2[1])
    valid = True
    for pt in coords:
      if min_x < pt[0] < max_x and min_y < pt[1] < max_y:
        valid = False
        break
    if min_y < upper[1] and max_y > upper[1]:
      valid = False
    if min_y < lower[1] and max_y > lower[1]:
      valid = False

    if valid:
      new_area = (max_x - min_x + 1) * (max_y - min_y + 1)
      ans2 = max(ans2, new_area)
print(ans2)
