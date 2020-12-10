#!/usr/bin/env python3

from copy import deepcopy


height = 6
width = 50

def print_grid(grid):
    for y in range(height):
        print("".join("#" if grid[y][x] else "." for x in range(width)))
    print("")

grid = [deepcopy([False] * width) for _ in range(height)]
with open("input.txt") as f:
    for line in f:
        if line.startswith("rect"):
            _, ab = line.strip().split()
            a, b = map(int, ab.split("x"))
            for aa in range(a):
                for bb in range(b):
                    grid[bb][aa] = True
        elif line.startswith("rotate column"):
            splt = line.strip().split()
            col_ind = int(splt[2][2:])
            by = int(splt[-1])
            tmp = None
            col = []
            for row in range(height):
                col.append(grid[row][col_ind])
            col =  col[-by:] + col[:-by]
            for row in range(height):
                grid[row][col_ind] = col[row]
        elif line.startswith("rotate row"):
            splt = line.strip().split()
            row_ind = int(splt[2][2:])
            by = int(splt[-1])
            grid[row_ind] = grid[row_ind][-by:] + grid[row_ind][:-by]


tot = 0
for row in grid:
    tot += sum(row)
print(tot)





