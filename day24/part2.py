#!/usr/bin/env python3

from collections import deque, defaultdict
from itertools import permutations


grid = []
with open("input.txt") as f:
    for line in f:
        grid.append(list(line.strip()))

def dst(frm, to):
    q = deque([(frm, 0)])
    reached = set()
    while q:
        pt, steps = q.popleft()
        if pt == to:
            return steps

        if pt in reached:
            continue
        reached.add(pt)

        x, y = pt
        reached.add(pt)
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if grid[y+dy][x+dx] != "#":
                q.append(((x+dx,y+dy), steps+1))

    return None

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
start = (start_x, start_y)

dsts = defaultdict(lambda: defaultdict(int))
for node in visit_locs:
    dsts[start][node] = dst(start, node)
    dsts[node][start] = dst(start, node)

for n1 in visit_locs:
    for n2 in visit_locs:
        dsts[n1][n2] = dsts[n2][n1] = dst(n1, n2)

mindist = 1e8
visit_locs.add(start)
for p in permutations(visit_locs):
    path = list(p)
    d = 0
    for p1, p2 in zip(path, path[1:]):
        d += dsts[p1][p2]
    d += dsts[path[-1]][path[0]]
    mindist = min(mindist, d)

print(mindist)
