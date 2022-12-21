#!/usr/bin/env python3

import fileinput

cmds = {}

for line in fileinput.input():
    mon, _, cmd = line.strip().partition(": ")
    try:
        cmds[mon] = int(cmd)
    except Exception:
        cmds[mon] = cmd

print(cmds)

def derive(cmds, name):
    val = cmds[name]
    if isinstance(val, int):
        return int(val)
    l, op, r = val.split()
    l = derive(cmds, l)
    r = derive(cmds, r)
    if op == "*":
        rv = l * r
    if op == "+":
        rv = l + r
    if op == "-":
        rv = l - r
    if op == "/":
        rv = l // r
    cmds[name] = rv
    return rv

v = derive(cmds, "root")
print("\n".join(str(i) for i in cmds.items()))

print(v)
