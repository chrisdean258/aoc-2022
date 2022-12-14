#!/usr/bin/env python3
from functools import cmp_to_key
ins = isinstance


def sign(i):
    return i if i == 0 else int(i / abs(i))


def cmp(i1, i2):
    if ins(i1, int) and ins(i2, int):
        return sign(i1 - i2)
    if ins(i1, int) and ins(i2, list):
        return cmp([i1], i2)
    if ins(i1, list) and ins(i2, int):
        return cmp(i1, [i2])
    if ins(i1, list) and ins(i2, list):
        for ii1, ii2 in zip(i1, i2):
            c = cmp(ii1, ii2)
            if c == -1:
                return -1
            if c == 1:
                return 1
        return sign(len(i1) - len(i2))


packets = [
    [[2]],
    [[6]],
]

s = 0
with open(0) as f:
    for line in f:
        if line.strip():
            packets.append(eval(line))

packets.sort(key=cmp_to_key(cmp))
ind1 = packets.index([[2]]) + 1
ind2 = packets.index([[6]]) + 1
print(ind1 * ind2)
