#!/usr/bin/env python3

import fileinput

nums = []
for line in fileinput.input():
    nums.append(int(line.strip()))


def mix(l):
    idxs = list(range(len(l)))
    for i in range(len(l)):
        c = idxs.index(i)
        idxs.pop(c)
        idxs.insert((c + l[i]) % len(idxs), i)
    return [l[i] for i in idxs]


nums = mix(nums)
z = nums.index(0)
s = 0
for i in range(1, 4):
    s += nums[(z + i * 1000) % len(nums)]
print(s)
