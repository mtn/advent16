#!/usr/bin/env python3

st = []
with open("input.txt") as f:
    for line in f:
        splt = line.strip().split()
        npos = int(splt[3])
        ipos = int(splt[-1][:-1])
        st.append((ipos, npos))
st.append((0, 11))

t = 0
while True:
    valid = True
    for dt, s in enumerate(st):
        ipos, npos = s
        pos = (ipos + t + dt + 1) % npos
        if pos != 0:
            valid = False
            break
    if valid:
        print(t)
        break

    t += 1
