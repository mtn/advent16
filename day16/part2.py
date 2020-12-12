#!/usr/bin/env python3

inp = "01111010110010011"
dlen = 35651584

while len(inp) < dlen:
    a = inp
    b = str(a)[::-1].replace("0", "2").replace("1", "0").replace("2", "1")
    inp = a + "0" + b

inp = inp[:dlen]
while True:
    cs = []
    for i in range(len(inp)//2):
        if inp[2*i] == inp[2*i+1]:
            cs.append(1)
        else:
            cs.append(0)
    inp = "".join(map(str, cs))

    if len(inp) % 2 == 1:
        break

print(inp)

