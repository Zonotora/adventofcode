from math import prod
lines = open("../input/06").read().strip().split("\n")

values = [[int(x) for x in line.split()] for line in lines[:-1]]
operators = lines[-1].split()

res = values[0]
for v in values[1:]:
  for j in range(len(operators)):
    if operators[j] == "+":
      res[j] += v[j]
    elif operators[j] == "*":
      res[j] *= v[j]

print(sum(res))


numbers = [[] for _ in range(len(lines[0]))]
for i in range(len(lines) - 1):
  for j in range(len(lines[i])):
    c = lines[i][j]
    numbers[j].append(c)

col = 0
buf = []
ans2 = 0
for num in numbers:
  value = "".join(num).strip()
  if not value.isnumeric():
    if operators[col] == "+":
      ans2 += sum(buf)
    elif operators[col] == "*":
      ans2 += prod(buf)
    buf.clear()
    col += 1
    continue
  buf.append(int(value))

if operators[col] == "+":
  ans2 += sum(buf)
elif operators[col] == "*":
  ans2 += prod(buf)
print(ans2)
