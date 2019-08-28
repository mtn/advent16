#!/usr/bin/env python3

from itertools import combinations

count = 0
with open('input.txt') as f:
    for line1 in f:
        line2 = f.next()
        line3 = f.next()

        line1 = list(map(int, line1.strip().split()))
        line2 = list(map(int, line2.strip().split()))
        line3 = list(map(int, line3.strip().split()))

        for i, _ in enumerate(line1):
            triangle = [line1[i], line2[i], line3[i]]
            total = sum(triangle)

            for (p1, p2) in combinations(triangle, 2):
                if p1 + p2 <= total - (p1 + p2):
                    break
            else:
                count += 1

print(count)
