#!/usr/bin/env python3

def dist(val, l):
    for i, v in enumerate(l):
        if v >= val:
            return i + 1
    return len(l)


grid = [list(a.strip()) for a in open(0).readlines()]

m = 0
for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[1]) - 1):
        val = grid[i][j]
        right = grid[i][j + 1:]
        left = list(reversed(grid[i][:j]))
        up = [grid[k][j] for k in range(i - 1, -1, -1)]
        down = [grid[k][j] for k in range(i + 1, len(grid))]

        s1 = dist(val, right)
        s2 = dist(val, left)
        s3 = dist(val, up)
        s4 = dist(val, down)

        score = s1 * s2 * s3 * s4

        # print(i, j, val, up, s3, down, s4, left, s2, right, s1, score)
        m = max(score, m)

print(m)
