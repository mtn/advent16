#!/usr/bin/env python3

from itertools import combinations

count = 0
with open('input.txt') as f:
    for line in f:
        line = list(map(int, line.strip().split()))
        total = sum(line)

        for (p1, p2) in combinations(line, 2):
            if p1 + p2 <= total - (p1 + p2):
                break
        else:
            count += 1

print(count)
