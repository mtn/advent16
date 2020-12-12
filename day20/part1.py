#!/usr/bin/env python3

rngs = []
with open("input.txt") as f:
    for line in f:
        l,h = map(int, line.strip().split("-"))
        rngs.append((l,h))

rngs.sort()
lowest = 0
for l, h in rngs:
    if lowest in range(l, h):
        lowest = h+1


print(lowest)
