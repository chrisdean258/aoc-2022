#!/usr/bin/env python3

import fileinput
import sympy


cmds = {}

for line in fileinput.input():
    mon, _, cmd = line.strip().partition(": ")
    try:
        cmds[mon] = int(cmd)
    except Exception:
        cmds[mon] = cmd

x = sympy.Symbol("humn")


def derive(cmds, name):
    if name == "humn":
        return x
    val = cmds[name]
    if isinstance(val, int):
        return int(val)
    l, op, r = val.split()
    l = derive(cmds, l)
    r = derive(cmds, r)
    if name == "root":
        return int(sympy.solve(l - r, x)[0])
    if op == "*":
        return l * r
    if op == "+":
        return l + r
    if op == "-":
        return l - r
    if op == "/":
        return l / r


v = derive(cmds, "root")

print(v)
