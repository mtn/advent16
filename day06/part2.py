#!/usr/bin/env python3

from collections import defaultdict

letter_freqs = [defaultdict(int) for _ in range(len("ciglthza"))]

with open("input.txt") as f:
    for line in f:
        word = line.strip()

        for i, c in enumerate(word):
            letter_freqs[i][c] += 1

print("".join(map(lambda x: min(x, key=x.get), letter_freqs)))
