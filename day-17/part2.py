#!/usr/bin/env python3

import fileinput
from itertools import cycle


for line in fileinput.input():
    plen = len(line.strip())
    pattern = cycle(line.strip())
    break


def can_be_here(offx, offy, piece, board):
    if offx < 0 or offy < 0:
        return False
    for i, line in enumerate(piece):
        if board[offy + i] & piece[i] << offx != 0:
            return False
    return True


pieces = [
    [0b1111],
    [0b010, 0b111, 0b010],
    [0b111, 0b100, 0b100],
    [1, 1, 1, 1],
    [0b11, 0b11],
]

no_pieces = 1000000000000
top = 0
num_taken = 0
board = []
cache = []
tops = []
last_seen = {}
cycle = None


for i in range(no_pieces):
    tops.append(top)
    if i % 5 == 0:
        key = num_taken % plen
        if key in last_seen:
            diff, pos = last_seen[key]
            if i - pos == diff:
                cycle = diff
                break
            last_seen[key] = (i - pos, i)
        else:
            last_seen[key] = (0, i)

    piece = pieces[i % len(pieces)]
    while len(board) < top + 3 + len(piece):
        board.append(0b100000001)
    offsety = top + 3
    offsetx = 3
    while True:
        move = next(pattern)
        num_taken += 1
        if move == "<":
            if can_be_here(offsetx - 1, offsety, piece, board):
                offsetx -= 1
        elif move == ">":
            if can_be_here(offsetx + 1, offsety, piece, board):
                offsetx += 1
        if can_be_here(offsetx, offsety - 1, piece, board):
            offsety -= 1
        else:
            for i, line in enumerate(piece):
                board[offsety + i] |= piece[i] << offsetx
            while board[top] != 0b100000001:
                top += 1
            break

cycle_diff = tops[-1] - tops[-cycle - 1]
print(no_pieces // cycle * cycle_diff + tops[no_pieces % cycle])
