#!/usr/bin/env python3

import re
import fileinput
import sys

beacons = set()
sensors = {}


def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


for line in fileinput.input():
    sx, sy, bx, by = map(int, re.findall(r"-?\d+", line))
    beacons.add((bx, by))
    d = abs(sx - bx) + abs(sy - by)
    sensors[(sx, sy)] = d

size = 4000000
for i in range(size + 1):
    j = 0
    while j <= size:
        can = True
        for s, d in sensors.items():
            if dist((i, j), s) <= d:
                if j < s[1]:
                    j += max(2 * abs(j - s[1]) - 1, 1)
                j += max(d - dist((i, j), s) - 1, 1)
                can = False
        if can and (i, j) not in beacons:
            print(i, j, i * 4000000 + j)
            sys.exit()
