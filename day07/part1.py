#!/usr/bin/env python3


supports_tls = 0

with open("input.txt") as f:
    for line in f:
        in_brackets = False
        is_ip = False

        for i, ch in enumerate(line.strip()[:-3]):
            if ch == "[":
                in_brackets = True
            elif ch == "]":
                in_brackets = False
            elif ch == line[i + 3] and line[i + 1] == line[i + 2] and ch != line[i + 1]:
                if in_brackets:
                    is_ip = False
                    break
                else:
                    is_ip = True

        if is_ip:
            supports_tls += 1

print(supports_tls)
