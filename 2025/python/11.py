from functools import cache
lines = open("../input/11").read().strip().split("\n")

devices = {}
for line in lines:
  parts = line.split(":")
  key = parts[0]
  outputs = parts[1].strip().split()

  if key not in devices:
    devices[key] = []
  devices[key].extend(outputs)


stack = []
for o in devices["you"]: stack.append(o)

ans1 = ans2 = 0
while stack:
  e = stack.pop()
  if e == "out":
    ans1 += 1
  else:
    stack.extend(devices[e])

print(ans1)

@cache
def part2(x, fft, dac):
  if x == "out":
    return 1 if fft and dac else 0
  else:
    s = 0
    for y in devices[x]:
      s += part2(y, fft or x == "fft", dac or x == "dac")
    return s

ans2 = part2("svr", False, False)
print(ans2)
