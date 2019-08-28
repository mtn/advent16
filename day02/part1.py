#!/usr/bin/env python3

x, y = 1, 1
nums = []
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        for direction in line:
            if direction == 'U':
                y -= 1
            elif direction == 'R':
                x += 1
            elif direction == 'D':
                y += 1
            elif direction == 'L':
                x -= 1

            y = min(y, 2)
            x = min(x, 2)
            y = max(y, 0)
            x = max(x, 0)

        nums.append(str(3 * y + x + 1))

print(''.join(nums))
