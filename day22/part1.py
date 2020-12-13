#!/usr/bin/env python3

from itertools import combinations

useds = {}
avails = {}
with open("input.txt") as f:
    for i, line in enumerate(f):
        if i < 2:
            continue
        splt = line.strip().split()

        useds[splt[0]] = int(splt[2][:-1])
        avails[splt[0]] = int(splt[3][:-1])

nodes = list(useds.keys())
valid = 0
for n1 in nodes:
    for n2 in nodes:
        if n1 == n2 or useds[n1] == 0:
            continue
        if useds[n1] == 0:
            continue
        if avails[n2] >= useds[n1]:
            valid += 1

print(valid)
