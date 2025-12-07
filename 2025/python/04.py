from copy import deepcopy
lines = open("../input/04").read().strip().split("\n")

grid = [[j for j in line] for line in lines]

def solve():
  global grid
  ans = 0
  grid_copy = deepcopy(grid)
  for ii in range(len(grid)):
    for jj in  range(len(grid[ii])):
      count = 0
      if grid[ii][jj] != "@":
        continue
      for i in range(-1, 2):
        for j in range(-1, 2):
          if i == 0 and j == 0:
            continue
          x = jj + j
          y = ii + i
          if 0 <= x < len(grid[ii]) and 0 <= y < len(grid) and grid[y][x] == "@":
            count += 1
      if count < 4:
        ans += 1
        grid_copy[ii][jj] = "."
  grid = grid_copy
  return ans

ans1 = ans2 = 0
while True:
  ans = solve()
  if ans == 0:
    break
  if ans1 == 0:
    ans1 = ans
  ans2 += ans

print(ans1)
print(ans2)


