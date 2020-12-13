#!/usr/bin/env python3

from itertools import combinations
import re

useds = {}
avails = {}
sizes = {}
maxx, maxy = 0, 0
with open("input.txt") as f:
    for i, line in enumerate(f):
        if i < 2:
            continue
        splt = line.strip().split()

        x, y = map(int, re.findall(r"(\d+)", splt[0]))

        sizes[(x, y)] = int(splt[1][:-1])
        useds[(x, y)] = int(splt[2][:-1])
        avails[(x, y)] = int(splt[3][:-1])

        maxx = max(maxx, x)
        maxy = max(maxy, y)

def print_grid(useds, maxx, maxy):
    def get_sym(x, y):
        if x == maxx and y == 0:
            return "G"
        elif useds[(x,y)] == 0:
            return "_"
        elif sizes[(x,y)] > 500:
            return "#"
        return "."

    print("".join(str(x).zfill(2) for x in range(maxx+2)))
    for y in range(maxy+1):
        print(str(y).zfill(2) + " ".join(get_sym(x, y) for x in range(maxx+1)))

# print_grid(useds, maxx, maxy)
print(244) # count
