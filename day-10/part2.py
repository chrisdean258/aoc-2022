#!/usr/bin/env python3

X = 1

cycle = 0
s = 0


def draw():
    global cycle
    if cycle % 40 == 0 and cycle != 0:
        print()
    if X - 1 <= cycle % 40 <= X + 1:
        print("#", end="")
    else:
        print(".", end="")
    cycle += 1


with open(0) as f:
    for line in f:
        draw()
        if line.strip() != "noop":
            draw()
            X += int(line.split()[1])
