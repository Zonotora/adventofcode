from collections import defaultdict

lines = open("../input/07").read().strip().split("\n")


grid = [[c for c in line] for line in lines]

ans1 = 0
memo = defaultdict(int)

for j in range(len(grid[0])):
  if grid[0][j] == "S":
    memo[(0,j)] += 1

for i in range(len(grid)):
  for j in range(len(grid[i])):
    should_create = grid[i][j] == "S" or grid[i][j] == "|" and i + 1 < len(grid)
    should_split = i + 1 < len(grid) and grid[i+1][j] == "^"
    if should_create: 
      if should_split:
        if j - 1 >= 0:
          grid[i+1][j-1] = "|"
          memo[(i+1,j-1)] += memo[(i,j)]
        if j + 1 < len(grid[i+1]):
          grid[i+1][j+1] = "|"
          memo[(i+1,j+1)] += memo[(i,j)]
        ans1 += 1
      else:
          grid[i+1][j] = "|"
          memo[(i+1,j)] += memo[(i,j)]

print(ans1)
ans2 = 0
for j in range(len(grid)):
  key = (len(grid) - 1, j)
  if key in memo:
    ans2 += memo[key]
print(ans2)
