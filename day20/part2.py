#!/usr/bin/env python3

max_ip = 4294967295
rngs = []
with open("input.txt") as f:
    for line in f:
        l,h = map(int, line.strip().split("-"))
        rngs.append((l,h))

rngs.sort()
ans = 0
i = 0
while i < len(rngs):
    l1, h1 = rngs[i]
    i += 1
    while i < len(rngs) and rngs[i][1] <= h1:
        i += 1
    if i != len(rngs):
        l2, h2 = rngs[i]
        ans += max(l2 - h1 - 1, 0)

ans += max_ip - h2

print(ans)
