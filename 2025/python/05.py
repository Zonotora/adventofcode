parts = open("../input/05").read().strip().split("\n\n")

ranges = [list(map(int, p.split("-"))) for p in parts[0].split("\n")]
ingredients = list(map(int, parts[1].split("\n")))


ans1 = 0
for ing in ingredients:
  for [start, end] in ranges:
    if start <= ing <= end:
      ans1 += 1
      break
print(ans1)


intervals = []
for [start, end] in ranges:
  combined = False
  next_iter = []
  insert = (start, end)
  cont = False
  for s, e in intervals:
    if insert[0] <= s <= insert[1] and e > insert[1]:
      insert = (insert[0], e)
    elif insert[0] <= e <= insert[1] and s < insert[0]:
      insert = (s, insert[1])
    elif insert[0] <= s <= e <= insert[1]:
      pass
    elif s <= insert[0] <= insert[1] <= e:
      cont = True
      break
    else:
      next_iter.append((s, e))
  if cont:
    continue
  next_iter.append(insert)

  intervals = sorted(next_iter)

ans2 = 0
for s, e in intervals:
  ans2 += e - s + 1
print(ans2)
