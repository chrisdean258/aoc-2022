#!/usr/bin/env python3

ins = isinstance


def sign(i):
    return i if i == 0 else int(i / abs(i))


def cmp(i1, i2):
    if ins(i1, int) and ins(i2, int):
        return sign(i1 - i2)
    if ins(i1, int) and ins(i2, list):
        return cmp([i1], i2)
    if ins(i1, list) and ins(i2, int):
        return cmp(i1, [i2])
    if ins(i1, list) and ins(i2, list):
        for ii1, ii2 in zip(i1, i2):
            c = cmp(ii1, ii2)
            if c == -1:
                return -1
            if c == 1:
                return 1
        return sign(len(i1) - len(i2))


s = 0
with open(0) as f:
    run = True
    i = 1
    while run:
        l1 = eval(f.readline())
        l2 = eval(f.readline())
        if f.readline() == "":
            run = False
        val = cmp(l1, l2)
        # print("---", i, "---", val)
        if val == -1:
            # print(i)
            s += i
        i += 1
print(s)
