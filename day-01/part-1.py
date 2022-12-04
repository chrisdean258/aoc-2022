#!/usr/bin/env python3

m = -1
s = 0
for line in open(0):
    line = line.strip()
    if line == "":
        m = max(s, m)
        s = 0
    else:
        s += int(line)

print(m)


