#!/usr/bin/env python3

import re


with open("input.txt") as f:
    content = f.read().strip()

def ulen(content):
    ans = 0
    i = 0
    while i < len(content):
        if content[i] == "(":
            end = content[i:].find(")") + i
            instr = content[i+1:end]
            chars, times = map(int, content[i+1:end].split("x"))
            to_copy = content[end+1:end+1+chars]
            to_copy_len = ulen(to_copy)
            ans += times * to_copy_len
            i = end + 1 + chars
        else:
            ans += 1
            i += 1

    return ans

print(ulen(content))
