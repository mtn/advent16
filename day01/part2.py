#!/usr/bin/env python3

x, y = 0, 0
heading = 1
locs = set()
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
            dx = dy = 0
            steps = int(cmd[1:])
            if heading == 0:
                dx -= steps
            elif heading == 1:
                dy += steps
            elif heading == 2:
                dx += steps
            elif heading == 3:
                dy -= steps

            while dx != 0 or dy != 0:
                if dx > 0:
                    dx -= 1
                    x += 1
                elif dx < 0:
                    dx += 1
                    x -= 1
                elif dy > 0:
                    dy -= 1
                    y += 1
                elif dy < 0:
                    dy += 1
                    y -= 1

                if (x, y) in locs:
                    print(abs(x) + abs(y))
                    exit()

                locs.add((x, y))
