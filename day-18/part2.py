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


def search(out, in_, fr):
    seen = set()
    q = deque([fr])
    while q:
        point = q.popleft()
        if point in out:
            out |= seen
            return True
        if point in in_:
            in_ |= seen
            return False
        for p in surrounding(*point):
            if p in lava:
                continue
            if p not in seen:
                q.append(p)
                seen.add(p)
    in_ |= seen
    return False


lava = set(tuple(int(a) for a in line.split(","))
           for line in fileinput.input())

outx = min(p[0] for p in lava) - 1
outy = min(p[0] for p in lava) - 1
outz = min(p[0] for p in lava) - 1
out = {(outx, outy, outz)}


air = set()
s = 0
for l in lava:
    for p in surrounding(*l):
        if p not in lava:
            air.add(p)

in_ = set()
trapped = set()
for p in air:
    if not search(out, in_, p):
        trapped.add(p)

for l in lava:
    for p in surrounding(*l):
        if p not in lava and p not in trapped:
            s += 1

print(s)
