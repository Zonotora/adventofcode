lines = open("../input/03").read().strip().split("\n")

def solve(N):
  battery = [0] * N
  bank = [int(x) for x in line]
  bank.extend(battery)
  L = len(line)
  for i in range(L):
    b = int(line[i])
    for j in range(N):
      if i + (N - 1 - j) < L and b > battery[j]:
        battery[j] = b
        for k in range(j + 1, N):
          battery[k] = 0
        break
  return int("".join([str(b) for b in battery]))

ans1 = ans2 = 0
for line in lines:
  ans1 += solve(2)
  ans2 += solve(12)
print(ans1)
print(ans2)
    







