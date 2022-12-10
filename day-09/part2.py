#!/usr/bin/env python3

def update(headx, heady, tailx, taily):
    if abs(headx - tailx) > 1 and abs(heady - taily) > 1:
        tailx = (headx + tailx) // 2
        taily = (heady + taily) // 2
    elif abs(headx - tailx) > 1:
        taily = heady
        tailx = (headx + tailx) // 2
    elif abs(heady - taily) > 1:
        tailx = headx
        taily = (heady + taily) // 2
    return (tailx, taily)


poss = set()


rope = [[0, 0] for _ in range(10)]


with open(0) as f:
    for line in f:
        direction, _, num = line.strip().partition(" ")
        num = int(num)
        for i in range(num):
            if direction == "U":
                rope[0][1] += 1
            elif direction == "D":
                rope[0][1] -= 1
            elif direction == "L":
                rope[0][0] -= 1
            elif direction == "R":
                rope[0][0] += 1

            for i in range(1, len(rope)):
                rope[i] = update(*rope[i - 1], *rope[i])

            poss.add(rope[-1])

print(len(poss))
