#!/usr/bin/env python3

import string

s = 0
with open(0) as f:
    for line in f:
        s1 = set(line[:len(line) // 2])
        s2 = set(line[len(line) // 2:])
        ch = (s1 & s2).pop()
        s += string.ascii_letters.index(ch) + 1
print(s)
