#!/usr/bin/env python3
import sys


def find_start():
    posx, posy = None, None
    for i, v in enumerate(m):
        for j, v2 in enumerate(v):
            if v2 == ord("S"):
                return i, j


def adj(x, y):
    if x > 0:
        yield x - 1, y
    if x < len(m) - 1:
        yield x + 1, y
    if y > 0:
        yield x, y - 1
    if y < len(m[x]) - 1:
        yield x, y + 1


def ffff(x, y, v):
    for nx, ny in adj(x, y):
        if (nx, ny) in seen:
            continue
        if v == ord("S"):
            yield nx, ny, m[nx][ny]
        elif v + 1 >= m[nx][ny] and m[nx][ny] != ord('E'):
            yield nx, ny, m[nx][ny]
        elif m[nx][ny] == ord("E") and v + 1 >= ord('z'):
            yield nx, ny, m[nx][ny]


m = []
for line in open(0):
    m.append([ord(a) for a in line.strip()])

posx, posy = find_start()
posses = {(posx, posy): [(posx, posy)]}
seen = {}

for i in range(100000):
    seen = {**seen, **posses}
    new_posses = {}
    for (posx, posy), way in posses.items():
        v = m[posx][posy]
        if v == ord("E"):
            print(i)
            sys.exit()
        for x, y, vv in ffff(posx, posy, v):
            ww = way[:]
            ww.append((x, y))
            new_posses[(x, y)] = ww
    posses = new_posses
