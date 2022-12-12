#!/usr/bin/env python3
import sys


def find_starts():
    posx, posy = None, None
    for i, v in enumerate(m):
        for j, v2 in enumerate(v):
            if v2 in (ord("S"), ord('a')):
                print(i, j)
                yield i, j


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
things = [10000000000]
for line in open(0):
    m.append([ord(a) for a in line.strip()])

for posx, posy in find_starts():
    done = False
    posses = {(posx, posy): None}
    seen = {}

    for i in range(min(things)):
        seen = {**seen, **posses}
        new_posses = {}
        for (posx, posy) in posses:
            v = m[posx][posy]
            if v == ord("E"):
                things.append(i)
                done = True
                break
            for x, y, vv in ffff(posx, posy, v):
                new_posses[(x, y)] = None
        posses = new_posses
        if done:
            break

print(min(things))
