#!/usr/bin/env python3

grid = [['x', 'x',   1, 'x', 'x'],
        ['x',  2,    3,   4, 'x'],
        [  5,  6,    7,   8,   9],
        ['x', 'A', 'B', 'C', 'x'],
        ['x', 'x', 'D', 'x', 'x']]

XMAX = len(grid[0]) - 1
YMAX = len(grid) - 1
x, y = 0, 2
nums = []
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        for direction in line:
            nextx = x
            nexty = y
            if direction == 'U':
                nexty = max(y - 1, 0)
            elif direction == 'R':
                nextx = min(x + 1, XMAX)
            elif direction == 'D':
                nexty = min(y + 1, YMAX)
            elif direction == 'L':
                nextx = max(x - 1, 0)

            if grid[nexty][nextx] == 'x':
                continue

            x = nextx
            y = nexty

        nums.append(str(grid[y][x]))

print(''.join(nums))
