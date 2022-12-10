#!/usr/bin/env python3

X = 1

cycle = 0
s = 0

with open(0) as f:
    for line in f:
        line = line.strip()
        cycle += 1
        if cycle % 40 == 20:
            s += cycle * X
        if line == "noop":
            continue
        cycle += 1
        if cycle % 40 == 20:
            s += cycle * X
        print(line)
        X += int(line.partition(" ")[2])
print(s)
