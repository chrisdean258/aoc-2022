#!/usr/bin/env python3

import fileinput
from collections import defaultdict

elves = set()
for i, l in enumerate(fileinput.input()):
    for j, c in enumerate(l):
        if c == "#":
            elves.add((i, j))


def test_north(i, j):
    if not (set((i - 1, j + k) for k in (-1, 0, 1)) & elves):
        proposals[(i - 1, j)].append((i, j))
        return True
    return False


def test_south(i, j):
    if not (set((i + 1, j + k) for k in (-1, 0, 1)) & elves):
        proposals[(i + 1, j)].append((i, j))
        return True
    return False


def test_west(i, j):
    if not (set((i + k, j - 1) for k in (-1, 0, 1)) & elves):
        proposals[(i, j - 1)].append((i, j))
        return True
    return False


def test_east(i, j):
    if not (set((i + k, j + 1) for k in (-1, 0, 1)) & elves):
        proposals[(i, j + 1)].append((i, j))
        return True
    return False

def no_neightbors(i, j):
    for ii in range(-1, 2):
        for jj in range(-1 ,2):
            if ii == jj == 0:
                continue
            if (i + ii, j + jj) in elves:
                return False
    return True


tests = [
    test_north,
    test_south,
    test_west,
    test_east,
]

for _ in range(10):
    proposals = defaultdict(list)
    for i, j in elves:
        if no_neightbors(i, j):
            continue
        for test in tests:
            if test(i, j):
                break
    for to, fr in proposals.items():
        if len(fr) > 1:
            continue
        elves.remove(fr[0])
        elves.add(to)
    tests.append(tests.pop(0))
    # for i in range(12):
        # for j in range(12):
            # print("#" if (i, j) in elves else '.', end="")
        # print()
    # print()


mini, minj = elves.pop()
maxi, maxj = mini, minj
for i, j in elves:
    maxj = max(maxj, j)
    minj = min(minj, j)
    maxi = max(maxi, i)
    mini = min(mini, i)

print((maxj - minj + 1) * (maxi - mini + 1) - len(elves) - 1)
