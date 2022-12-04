#!/usr/bin/env python3
import re

s = 0
with open(0) as f:
    for line in f:
        s1, e1, s2, e2 = [int(a) for a in re.split(r"[,-]", line.strip())]
        # range 2 starts in range 1 or range 1 starts in range 2
        s += (s1 <= s2 <= e1) or (s2 <= s1 <= e2)
print(s)
