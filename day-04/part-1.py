#!/usr/bin/env python3
import re

s = 0
with open(0) as f:
    for line in f:
        s1, e1, s2, e2 = [int(a) for a in re.split(r"[,-]", line.strip())]
        s += (s1 <= s2 and e2 <= e1) or (e1 <= e2 and s2 <= s1)
print(s)

