#!/usr/bin/env python3

from collections import defaultdict
from collections import deque

stacks = defaultdict(deque)

with open(0) as f:
    for line in f:
        line = line.rstrip()
        if line == "":
            break
        if line[0:2] == " 1":
            continue
        for (i, ch) in enumerate(line[1::4]):
            if ch != " ":
                stacks[i+1].appendleft(ch)

    for i, v in stacks.items():
        stacks[i] = list(v)

    for line in f:
        num, fr, to = [int(a) for a in line.split()[1::2]]
        st = stacks[fr][-num:]
        stacks[fr] = stacks[fr][:-num]
        stacks[to] += st

for i in range(1, len(stacks) + 1):
    print(stacks[i].pop(), end="")
print()
