import re

from scipy.optimize import linprog

lines = open("../input/13").read().split("\n\n")

# minimize c @ z
# s.t.     z_1 (ax + ay) + z_2 (bx + by) = (X, Y)
# c = [3 1]
# A = [ax bx] [z_1]
#     [ay by] [z_2]
# b = [mx]
#     [my]
# floating errors with high offset..? no milp integrality=True
for offset in [0, 10000000000000]:
    s = 0
    i = 0
    for claw in lines:
        [ax, ay, bx, by, mx, my] = map(int, re.findall(r"[0-9]+", claw))
        c = [3, 1]
        A = [[ax, bx], [ay, by]]
        b = [mx, my]
        b = [x + offset for x in b]
        value = linprog(c=c, A_eq=A, b_eq=b)
        i += 1
        if value.x is None:
            continue
        a, b = value.x
        if abs(a - round(a)) > 1e-3:
            continue
        s += round(3 * a + b)
    print(s)
