#!/usr/bin/env python3

from collections import deque
from itertools import permutations

grid = []
with open("input.txt") as f:
    for line in f:
        grid.append(list(line.strip()))


visit_locs = set()
start_x = None
start_y = None
for y, row in enumerate(grid):
    for x, val in enumerate(row):
        if val.isdigit():
            if val == "0":
                start_x = x
                start_y = y
            else:
                visit_locs.add((x, y))

memo = set()
q = deque([([0], (start_x,start_y), 0)])
while q:
    reached, pt, steps = q.popleft()
    if (tuple(reached), pt) in memo:
        continue
    memo.add((tuple(reached), pt))

    if pt in visit_locs and pt not in reached:
        reached.append(pt)

    if len(reached) == len(visit_locs) + 1:
        print(steps)
        break

    x, y = pt
    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if grid[y+dy][x+dx] != "#":
            q.append((list(reached), (x+dx, y+dy), steps+1))
