#!/usr/bin/env python3

from itertools import combinations


with open('input.txt') as f:
    for line in f:
        line = line.strip().split('-')
        number = int(line[-1][:line[-1].find('[')])

        newstr = ' '.join(map(lambda word: ''.join(map(lambda x: chr((ord(x) - ord('a') + number) % 26 + ord('a')), word)), line[:-1]))

        if 'north' in newstr:
            print(number)
            exit()
