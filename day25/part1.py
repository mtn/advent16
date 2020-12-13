#!/usr/bin/env python3

regnames = "abcd"

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

ainit = 0
while True:
    reg = [0] * len(regnames)
    reg[0] = ainit

    outs = []
    max_steps = 10000000
    with open("input.txt") as f:
        lines = f.read().strip().split("\n")
        ind = 0
        step = 0
        while ind < len(lines):
            step += 1
            line = lines[ind]

            if ind == 1:
                reg[3] += 15 * 170
                reg[2] = 0
                reg[1] = 0
                ind = 8
                continue

            if len(outs) == 20:
                if all(outs[2*i] == 0 and outs[2*i+1] == 1 for i in range(10)):
                    print(ainit)
                    exit()
                break

            if step > max_steps:
                break

            splt = line.strip().split()
            if line.startswith("cpy"):
                val = getval(reg, splt[1])
                if isinstance(splt[2], str) and splt[2] in regnames:
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
            elif line.startswith("out"):
                val = getval(reg, splt[1])
                if outs and outs[-1] == val:
                    break
                outs.append(val)
                ind += 1

    ainit += 1
