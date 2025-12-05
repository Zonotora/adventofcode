lines = open("../input/01").read().strip().split("\n")
dial = 50

ans1 = ans2 = 0
for line in lines:
  amount = int(line[1:])
  times = 0
  if line[0] == "R":
    dial += amount
    times = dial // 100
    ans2 += times
  else:
    prev = dial
    dial -= amount
    if dial == 0: times = 1
    if dial < 0:
      times = -dial // 100 + 1
      if prev == 0:
        times -= 1
    ans2 += times

  dial %= 100

  if dial == 0:
    ans1 += 1

print(ans1)
print(ans2)
