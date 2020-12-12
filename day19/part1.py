#!/usr/bin/env python3

# https://www.youtube.com/watch?v=uCsD3ZGzMgE

inp = 3005290

p2 = 2
while p2 < inp:
    p2 *= 2
p2 //= 2
print((inp - p2) * 2 + 1)

# presents = {i: 1 for i in range(inp)}
# nxt = {i:(i+1)%inp for i in range(inp)}

# i = 0
# steps = 0
# while True:
#     nx = nxt[i]
#     if presents[i]:
#         presents[i] += presents[nx]
#         del presents[nx]
#         nxt[i] = nxt[nx]
#         del nxt[nx]

#     i = nxt[i]

#     if presents[i] == inp:
#         print(i+1)
#         break

