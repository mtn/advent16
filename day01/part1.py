#!/usr/bin/env python3

x, y = 0, 0
heading = 1
with open('input.txt') as f:
    for line in f:
        cmds = line.split(', ')
        for cmd in cmds:
            cmd = cmd.strip('\n,')

            if cmd[0] == 'L':
                heading -= 1
            elif cmd[0] == 'R':
                heading += 1

            heading %= 4

            steps = int(cmd[1:])
            if heading == 0:
                x -= steps
            elif heading == 1:
                y += steps
            elif heading == 2:
                x += steps
            elif heading == 3:
                y -= steps

print(abs(x) + abs(y))
