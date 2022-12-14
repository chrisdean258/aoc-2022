#!/usr/bin/env python3
import fileinput
import re

i = [list(map(int, re.findall(r"-?\d+", l)))
     for l in fileinput.input()]
sand = set()

for l in i:
    for p in range(0, len(l) - 2, 2):
        x1, y1, x2, y2 = l[p: p + 4]
        dx = (x2 > x1) - (x2 < x1)
        dy = (y2 > y1) - (y2 < y1)
        while (x1, y1) != (x2, y2):
            sand.add((x1, y1))
            x1, y1 = x1 + dx, y1 + dy
        sand.add((x1, y1))
abyss = max(y for x, y in sand)
print(list(sorted(sand)))
for x in range(-10000, 10000):
    sand.add((x, abyss + 2))

num = 0
while (500, 0) not in sand:
    x, y = 500, 0
    while True:
        if (x, y + 1) not in sand:
            y += 1
        elif (x - 1, y + 1) not in sand:
            x, y = x - 1, y + 1
        elif (x + 1, y + 1) not in sand:
            x, y = x + 1, y + 1
        else:
            sand.add((x, y))
            if y - 1 == abyss:
                print(num)
                abyss = None
            num += 1
            break
print(num)
