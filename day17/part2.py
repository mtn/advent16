#!/usr/bin/env python3

from hashlib import md5
from collections import deque


inp = "pslxynzg"
dirs = "UDLR"
unlocked = "bcdef"
q = deque([("", (0,0))])
d_xy = [(0,-1), (0,1), (-1,0), (1,0)]
longest = 0
while q:
    p, (x, y) = q.popleft()
    if x == 3 and y == 3:
        longest = max(longest, len(p))
        continue

    hsh = md5(str.encode(inp+p)).hexdigest()[:4]
    for u, d, (dx, dy) in zip(hsh, dirs, d_xy):
        if u in unlocked and x + dx >= 0 and x + dx < 4 and y + dy >= 0 and y + dy < 4:
            q.append((p+d, (x+dx, y+dy)))

print(longest)

