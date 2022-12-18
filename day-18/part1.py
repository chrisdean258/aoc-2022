#!/usr/bin/env python3

import fileinput
from collections import deque


def surrounding(x, y, z):
    yield x + 1, y, z
    yield x - 1, y, z
    yield x, y + 1, z
    yield x, y - 1, z
    yield x, y, z + 1
    yield x, y, z - 1



lava = set(tuple(int(a) for a in line.split(","))
           for line in fileinput.input())

s = 0
for l in lava:
    for p in surrounding(*l):
        if p not in lava:
            s += 1

print(s)
