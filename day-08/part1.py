#!/usr/bin/env python3

grid = [a.strip() for a in open(0).readlines()]
visible = [[0] * len(grid[0]) for _ in grid]

for i in range(1, len(grid) - 1):
    m_l = grid[i][0]
    m_r = grid[i][-1]
    for j in range(1, len(grid[i]) - 1):
        if grid[i][j] > m_l:
            m_l = grid[i][j]
            visible[i][j] = 1
        if grid[i][-j - 1] > m_r:
            m_r = grid[i][-j - 1]
            visible[i][-j - 1] = 1

for i in range(1, len(grid[0]) - 1):
    m_t = grid[0][i]
    m_b = grid[-1][i]
    for j in range(1, len(grid) - 1):
        if grid[j][i] > m_t:
            m_t = grid[j][i]
            visible[j][i] = 1
        if grid[-j - 1][i] > m_b:
            m_b = grid[-j - 1][i]
            visible[-j - 1][i] = 1

visible[0] = [1] * len(grid[0])
visible[-1] = [1] * len(grid[0])

for row in visible:
    row[0] = 1
    row[-1] = 1

print("\n".join(str(g) for g in grid))
print("\n".join(str(v) for v in visible))

print(sum(sum(r) for r in visible))
