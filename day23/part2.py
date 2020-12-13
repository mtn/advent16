#!/usr/bin/env python3


regnames = "abcd"
reg = [0] * len(regnames)
reg[0] = 12

def isnum(s):
    try:
        int(s)
    except:
        return False
    return True

def getval(reg, s):
    if isnum(s):
        return int(s)
    return reg[regnames.find(s)]

def toggle(line):
    cmd = line.strip().split()[0]
    if cmd == "inc":
        return line.replace("inc", "dec")
    elif cmd in ["dec", "tgl"]:
        return line.replace(cmd, "inc")
    elif cmd == "jnz":
        return line.replace(cmd, "cpy")
    return line.replace(cmd, "jnz")

with open("input.txt") as f:
    lines = f.read().strip().split("\n")
    ind = 0
    while ind < len(lines):
        line = lines[ind]

        if ind == 4:
            reg[0] += reg[-1] * reg[1]
            reg[2] = 0
            reg[3] = 0
            ind += 6
            continue

        splt = line.strip().split()
        if line.startswith("cpy"):
            val = getval(reg, splt[1])
            if isinstance(splt[2], str) and splt[2] in regnames:
                tgt = regnames.find(splt[2])
                reg[tgt] = val
            else:
                print("invalid")
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
            x = getval(reg, splt[1])
            steps = getval(reg, splt[2])
            if x != 0:
                ind += steps
            else:
                ind += 1
        elif line.startswith("tgl"):
            tgl_ind = getval(reg, splt[1]) + ind
            if 0 <= tgl_ind < len(lines):
                lines[tgl_ind] = toggle(lines[tgl_ind])
            ind += 1

print(reg[0])





