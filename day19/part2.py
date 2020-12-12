#!/usr/bin/env python3

from collections import deque


inp = 3005290

l = deque()
r = deque()
for i in range(1, inp+1):
    if i <= inp // 2:
        l.append(i)
    else:
        r.appendleft(i)
while l and r:
    if len(l) > len(r):
        l.pop()
    else:
        r.pop()

    r.appendleft(l.popleft())
    l.append(r.pop())

print(l[0])
