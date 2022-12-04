#!/usr/bin/env python3

s = 0
elves = []
for line in open(0):
    line = line.strip()
    if line == "":
        elves.append(s)
        s = 0
    else:
        s += int(line)

print(sum(sorted(elves)[-3:]))
