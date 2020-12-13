#!/usr/bin/env python3

from itertools import permutations

def scramble(pw, lines):
    pw = list(pw)
    for line in lines:
        splt = line.strip().split()
        if line.startswith("swap"):
            if splt[1] == "position":
                p1 = int(splt[2])
                p2 = int(splt[-1])
                tmp = pw[p2]
                pw[p2] = pw[p1]
                pw[p1] = tmp
            else:
                l1 = splt[2]
                l2 = splt[-1]
                p1 = pw.index(l1)
                p2 = pw.index(l2)
                tmp = pw[p2]
                pw[p2] = pw[p1]
                pw[p1] = tmp

        elif line.startswith("reverse"):
            p1 = int(splt[2])
            p2 = int(splt[-1])
            cpw = list(pw)
            for i in range(p2-p1+1):
                cpw[p2-i] = pw[p1+i]
            pw = cpw

        elif line.startswith("rotate"):
            if splt[1] in ["left", "right"]:
                steps = int(splt[-2]) % len(pw)
                if steps:
                    if splt[1] == "left":
                        pw = pw[-(len(pw)-steps):] + pw[:steps]
                    elif splt[1] == "right":
                        pw = pw[-steps:] + pw[:len(pw)-steps]
            else:
                l = splt[-1]
                i = pw.index(l)
                steps = (1 + i + (i >= 4)) % len(pw)
                if steps:
                    pw = pw[-steps:] + pw[:len(pw)-steps]

        elif line.startswith("move"):
            p1 = int(splt[2])
            p2 = int(splt[-1])
            l = pw.pop(p1)
            pw.insert(p2, l)

    return "".join(pw)

inp = "fbgdceah"

with open("input.txt") as f:
    lines = f.read().strip().split("\n")

for p in permutations("abcdefgh"):
    p = "".join(p)
    if scramble(p, lines) == inp:
        print(p)
        exit()
