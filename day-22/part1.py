#!/usr/bin/env python3

import fileinput
import re

*grid, _, path = fileinput.input()
pos, vel = grid[0].index('.'), 1
path = re.findall(r'\d+|[RL]', path)
grid = {complex(x, y): c for y, l in enumerate(grid)
        for x, c in enumerate(l) if c in '.#'}

for p in path:
    if p == "R":
        vel *= 1j
    elif p == "L":
        vel *= -1j
    else:
        for _ in range(int(p)):
            new = pos + vel
            if new in grid:
                if grid[new] == '.':
                    pos = new
            else:
                new = pos
                while new - vel in grid:
                    new -= vel
                if grid[new] == '.':
                    pos = new


print(int(1000 * (pos.imag + 1) + 4 * (pos.real + 1) + [1, 1j, -1, -1j].index(vel)))
