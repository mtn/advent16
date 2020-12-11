#!/usr/bin/env python3

from collections import deque

inp = 1364

def is_wall(x, y):
    val = x*x + 3*x + 2*x*y + y + y*y + inp
    one_bits = 0
    while val > 0:
        one_bits += val & 1
        val = val >> 1

    return one_bits % 2 == 1

def print_grid(xlim, ylim):
    for y in range(ylim+1):
        print("".join(["#" if is_wall(x, y) else "." for x in range(xlim+1)]))

q = deque([((1, 1), 0)])
visited = set()
while q:
    p, steps = q.popleft()
    if p == (31, 39):
        print(steps)
        break

    visited.add(p)

    x,y = p
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if (x+dx, y+dy) in visited:
            continue
        if x + dx < 0 or y + dy < 0:
            continue
        if not is_wall(x+dx, y+dy):
            q.append(((x+dx, y+dy), steps+1))




