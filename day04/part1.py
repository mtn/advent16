#!/usr/bin/env python3

from itertools import combinations


real_sum = 0
with open('input.txt') as f:
    for line in f:
        checksum = line[line.find('[')+1:line.find(']')]
        line = line.strip().split('-')
        number = int(line[-1][:line[-1].find('[')])

        fullstr = ''.join(line[:-1])
        expected_checksum = ''.join(map(lambda x: x[1], sorted(list(map(lambda x: (-fullstr.count(x), x), set(fullstr))))))[:5]

        if checksum == expected_checksum:
            real_sum += number

print(real_sum)
