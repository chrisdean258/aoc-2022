#!/usr/bin/env python3

t = open(0).read()

ls = [t[i:] for i in range(14)]

for i, cs in enumerate(zip(*ls)):
    if len(set(cs)) == len(ls):
        print(i + len(ls))
        break
