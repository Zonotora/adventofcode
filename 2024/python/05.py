from collections import defaultdict

lines = open("../input/05").read().split("\n\n")

orders, updates = lines

order = [[int(y) for y in x.split("|")] for x in orders.split("\n")]

mapping = defaultdict(list)
for order in orders.split("\n"):
    left, right = [int(x) for x in order.split("|")]
    mapping[left].append(right)


def update(pages):
    valid = []
    while len(pages):
        page = pages.pop(0)
        wrong = False
        for other in pages:
            if page in mapping[other]:
                pages.append(page)
                wrong = True
                break
        if not wrong:
            valid.append(page)
    return valid


updates = [[int(x) for x in page.split(",")] for page in updates.split("\n")]
part1 = part2 = 0
for pages in updates:
    seen = set()
    wrong = False
    for page in pages:
        for x in mapping[page]:
            if x in seen:
                wrong = True
                pages = update(pages)
                break
        seen.add(page)
    if wrong:
        part2 += pages[len(pages) // 2]
    else:
        part1 += pages[len(pages) // 2]

print(part1)
print(part2)
