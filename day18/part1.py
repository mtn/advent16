#!/usr/bin/env python3

with open("input.txt") as f:
    c = f.read().strip()

c = "." + c + "."
safe_tiles = c.count(".") - 2

for i in range(39):
    cc = ["."]
    for j in range(len(c) - 2):
        s = c[j:j+3]
        if s in ["^^.", ".^^", "^..", "..^"]:
            cc.append("^")
        else:
            cc.append(".")
    cc.append(".")
    c = "".join(cc)
    safe_tiles += c.count(".") - 2
print(safe_tiles)
