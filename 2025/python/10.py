import re
from pulp import *
import sys

lines = open("../input/10").read().strip().split("\n")

ans1 = ans2 = 0
k = 0
for line in lines:

  parts = line.split()
  onoff = [0] * (len(parts[0]) - 2)
  i = 0
  for c in parts[0]:
    if c in ["[", "]"]:
      continue
    onoff[i] = c == "#"
    i += 1
  buttons = [list(map(int, re.findall("[0-9]+", e))) for e in parts[1:-1]]
  joltage = list(map(int, re.findall(r"[0-9]+", parts[-1])))

  # onoff = x1 * btn1 + x2 * btn2 ... xn * btnn
  # min x1 + x2 ... xn
  ans1_model = LpProblem(name="ans1", sense=LpMinimize)
  ans2_model = LpProblem(name="ans2", sense=LpMinimize)
  decisions = []
  for i in range(len(buttons)):
    x = LpVariable(name=f"x{i}", lowBound=0, cat="Integer")
    decisions.append(x)

  parity = []
  slack = []
  for i in range(len(onoff)):
    p = LpVariable(f"parity{i}", cat="Binary")
    t = LpVariable(f"slack_t{i}", lowBound=0, cat="Integer")
    parity.append(p)
    slack.append(t)
  ans1_model += lpSum(decisions)
  ans2_model += lpSum(decisions)

  lights = {}
  for i in range(len(buttons)):
    b = buttons[i]
    for key in b:
      if key not in lights:
        lights[key] = []
      lights[key].append(i)

  assert len(lights) == len(onoff)
  for key in lights:
    s = lpSum([decisions[i] for i in lights[key]])

    ans1_model += s == 2 * slack[key] + parity[key]
    ans1_model += parity[key] == onoff[key]
    ans2_model += s == joltage[key]

  status = ans1_model.solve(PULP_CBC_CMD(msg=0))
  assert status == 1
  ans1 += int(value(ans1_model.objective))

  status = ans2_model.solve(PULP_CBC_CMD(msg=0))
  assert status == 1
  ans2 += int(value(ans2_model.objective))
  k += 1

print(ans1)
print(ans2)
