from collections import Counter, defaultdict
from itertools import combinations

lines = open("../input/23").read().strip().split("\n")

nodes = defaultdict(set)

for line in lines:
    [fr, to] = line.split("-")
    nodes[fr].add(to)
    nodes[to].add(fr)

groups = set()
for node, connections in nodes.items():
    for fst, snd in combinations(connections, 2):
        cond1 = node in nodes[fst] and snd in nodes[fst]
        cond2 = node in nodes[snd] and fst in nodes[snd]
        has_t = any([c.startswith("t") for c in [node, fst, snd]])
        if cond1 and cond2 and has_t:
            key = tuple(sorted([node, fst, snd]))
            groups.add(key)

biggest = []
for node, connections in nodes.items():
    group = set([node]) | connections
    merges = []
    for c in connections:
        other = set([c]) | nodes[c]
        merges.append(group & other)
    freq = Counter([tuple(sorted(keys)) for keys in merges])
    for k, v in freq.items():
        if len(k) == v + 1 and len(biggest) < v + 1:
            biggest = k

print(len(groups))
print(",".join(biggest))
