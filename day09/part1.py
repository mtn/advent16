#!/usr/bin/env python3

import re


with open("input.txt") as f:
    content = f.read().strip()

ans = ""
i = 0
while i < len(content):
    if content[i] == "(":
        end = content[i:].find(")") + i
        instr = content[i+1:end]
        chars, times = map(int, content[i+1:end].split("x"))
        to_copy = content[end+1:end+1+chars]
        ans += times * to_copy
        i = end + 1 + chars
    else:
        ans += content[i]
        i += 1
print(len(ans))
