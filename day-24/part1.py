#!/usr/bin/env python3

import fileinput

grid = [a.strip() for a in fileinput.input()]
up = set()
down = set()
left = set()
right = set()
walls = {(-1, 1)}


def adj(i, j):
    yield i, j
    yield i + 1, j
    yield i - 1, j
    yield i, j + 1
    yield i, j - 1


for i, line in enumerate(grid):
    for j, ch in enumerate(line):
        if ch == "<":
            left.add((i, j))
        elif ch == ">":
            right.add((i, j))
        elif ch == "^":
            up.add((i, j))
        elif ch == "v":
            down.add((i, j))
        elif ch == "#":
            walls.add((i, j))


def print_grid():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            invalid = up | down | left | right | walls
            print("#" if (i, j) in invalid else ".", end="")
        print()
    print()


def advance():
    global up, right, left, down
    newup = set()
    for i, j in up:
        if i == 1:
            newup.add((len(grid) - 2, j))
        else:
            newup.add((i - 1, j))
    up = newup
    newdown = set()
    for i, j in down:
        if i == len(grid) - 2:
            newdown.add((1, j))
        else:
            newdown.add((i + 1, j))
    down = newdown
    newleft = set()
    for i, j in left:
        if j == 1:
            newleft.add((i, len(grid[i]) - 2))
        else:
            newleft.add((i, j - 1))
    left = newleft
    newright = set()
    for i, j in right:
        if j == len(grid[i]) - 2:
            newright.add((i, 1))
        else:
            newright.add((i, j + 1))
    right = newright
    # print_grid()


pos = {(0, 1)}
next_pos = set()
time = 1
advance()
target = (len(grid) - 1, len(grid[0]) - 2)
while True:
    looking = pos.pop()
    if looking == target:
        pos = {looking}
        next_pos = set()
        print(time)
        break
    for p in adj(*looking):
        next_pos.add(p)
    if not pos:
        advance()
        invalid = up | down | left | right | walls
        pos = next_pos - invalid
        next_pos = set()
        time += 1
