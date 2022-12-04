#!/usr/bin/env python3

import string

s = 0
with open(0) as f:
    for e1, e2, e3 in zip(f, f, f):
        ch = (set(e1.strip()) & set(e2.strip()) & set(e3.strip())).pop()
        print(ch)
        s += string.ascii_letters.index(ch) + 1
print(s)
