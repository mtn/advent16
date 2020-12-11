#!/usr/bin/env python3

regnames = "abcd"
reg = [0] * len(regnames)
with open("input.txt") as f:
    lines = f.read().strip().split("\n")
    ind = 0
    while ind < len(lines):
        line = lines[ind]
        splt = line.strip().split()
        if line.startswith("cpy"):
            if splt[1].isdigit():
                val = int(splt[1])
            else:
                val = reg[regnames.find(splt[1])]
            tgt = regnames.find(splt[2])
            reg[tgt] = val
            ind += 1
        elif line.startswith("inc"):
            tgt = regnames.find(splt[1])
            reg[tgt] += 1
            ind += 1
        elif line.startswith("dec"):
            tgt = regnames.find(splt[1])
            reg[tgt] -= 1
            ind += 1
        elif line.startswith("jnz"):
            regval = reg[regnames.find(splt[1])]
            if regval != 0:
                steps = int(splt[2])
                ind += steps
            else:
                ind += 1

print(reg[0])





