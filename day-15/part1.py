#!/usr/bin/env python3

import re
import fileinput

row_test = 2000000

cannot = set()
beacons = set()
for line in fileinput.input():
    sx, sy, bx, by = map(int, re.findall("-?\d+", line))
    beacons.add((bx, by))
    d = abs(sx - bx) + abs(sy - by)
    px = sx
    while True:
        if abs(px - sx) + abs(row_test - sy) <= d:
            cannot.add((px, row_test))
        else:
            break
        px += 1
    px = sx
    while True:
        if abs(px - sx) + abs(row_test - sy) <= d:
            cannot.add((px, row_test))
        else:
            break
        px -= 1

print(len(cannot - beacons))
