#!/usr/bin/env python3

import fileinput
from itertools import cycle

for line in fileinput.input():
    pattern = cycle(line.strip())
    break


def can_be_here(offx, offy, piece, board):
    if offx < 0 or offy < 0:
        return False
    # print("Testing")
    # b2 = board[:]
    # for i, line in enumerate(piece):
        # b2[offy + i] |= piece[i] << offx
    # for line in b2:
        # print(f"{line:b}")
    for i, line in enumerate(piece):
        if board[offy + i] & piece[i] << offx != 0:
            # print("No\n")
            return False
    # print("yes\n")
    return True


pieces = [
    [0b1111],
    [0b010, 0b111, 0b010],
    [0b111, 0b100, 0b100],
    [1, 1, 1, 1],
    [0b11, 0b11],
]

top = 0

board = []

for i in range(2022):
    # for line in board:
        # print(f"{line:b}")
    # print()
    piece = pieces[i % len(pieces)]
    while len(board) < top + 3 + len(piece):
        board.append(0b100000001)
    offsety = top + 3
    offsetx = 3
    while True:
        move = next(pattern)
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
print(top)
