ids = [x.split("-") for x in open("../input/02").read().split(",")]

ans1 = ans2 = 0
for [first, last] in ids:
  for i in range(int(first), int(last) + 1):
    s = str(i)
    n = len(s) // 2
    if s[:n] == s[n:]:
      ans1 += i
      ans2 += i
    else:
      for k in range(1, n + 1):
        if len(s) % k == 0:
          prev = None
          equal = True
          for j in range(0, len(s), k):
            if prev is None:
              prev = s[j:j+k]
            elif s[j:j+k] != prev:
              equal = False
          if equal:
            ans2 += i
            break

print(ans1)
print(ans2)



