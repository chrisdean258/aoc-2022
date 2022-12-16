#!/usr/bin/env python3

import fileinput

nodes = {}
res = 0
tot_rate = 0
procs = False
cache = {}

for line in fileinput.input():
    parts = line.split()
    _, valve, _, _, rate, _, _, _, _, *leads_to = parts
    rate = int(rate[5:-1])
    tot_rate += rate
    nodes[valve] = [rate, [a.rstrip(",") for a in leads_to], False]


def search(node, potential_flow, total, remaining, max_seen, mask):
    global res
    global procs
    a = cache.get(node,
    if total + potential_flow * remaining < max_seen:
        return 0
    if remaining <= 0:
        if total > res:
            print(res)
            return total
        return res
    rate, leads_to, is_open = nodes[node]
    if not is_open and rate != 0:
        nodes[node][2] = True
        remaining -= 1
        new_tot = total + rate * remaining
        for newnode in leads_to:
            if nodes[newnode][1] == 0:
                continue
            search(newnode, potential_flow - rate, new_tot, remaining - 1)
        remaining += 1
        nodes[node][2] = False
    else:
        for newnode in leads_to:
            search(newnode, potential_flow, total, remaining - 1)


search("AA", tot_rate, 0, 30, 0)

print(res)
