from itertools import count

values, wires = open("../input/24").read().strip().split("\n\n")

signals = {}
conditions = []
gates = {}
for s in values.split("\n"):
    k, v = s.replace(":", "").split()
    signals[k] = v == "1"

for c in wires.split("\n"):
    left, op, right, res = c.replace(" -> ", " ").split()
    gates[res] = (op, left, right)
    conditions.append((left, op, right, res))


def operation(op, left, right):
    left, right = signals[left], signals[right]
    if op == "AND":
        return left and right
    elif op == "OR":
        return left or right
    elif op == "XOR":
        return left ^ right


def part1():
    while len(conditions):
        [left, op, right, res] = conditions.pop(0)
        if left in signals and right in signals:
            signals[res] = operation(op, left, right)
        else:
            conditions.append([left, op, right, res])
    z = []
    for key in sorted(signals, reverse=True):
        if key.startswith("z"):
            z.append(1 if signals[key] else 0)
    return int("".join(map(str, z)), 2)


def make(c, i):
    return c + str(i).rjust(2, "0")


def pp(key):
    op, left, right = gates[key]
    if not left[1:].isdigit():
        left = pp(left)
    if not right[1:].isdigit():
        right = pp(right)
    left, right = sorted([left, right])
    return f"({left} {op} {right})"


def carry(a, b, c):
    if c is None:
        return f"({a} AND {b})"
    else:
        return f"(({c} AND ({a} XOR {b})) OR ({a} AND {b}))"


def check():
    c = None
    for i in count():
        if make("z", i) not in gates:
            break
        x = make("x", i)
        y = make("y", i)
        z = make("z", i)
        s = f"({x} XOR {y})"
        try:
            v = pp(z)
        except:
            return 0
        if c is None and v != s:
            return i
        elif c is not None and v != f"({c} XOR {s})":
            return i
        c = carry(x, y, c)


best = check()
pairs = []
for _ in range(4):
    for a in gates:
        for b in gates:
            gates[a], gates[b] = gates[b], gates[a]
            c = check()
            if best < c:
                best = c
                pairs.extend([a, b])
                break
            gates[a], gates[b] = gates[b], gates[a]
        else:
            continue
        break

print(part1())
print(",".join(sorted(pairs)))
