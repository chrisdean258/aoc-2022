#!/usr/bin/env python3


hposx = 0
hposy = 0
tposx = 0
tposy = 0

poss = set([(tposx, tposy)])

with open(0) as f:
    for line in f:
        direction, _, num = line.strip().partition(" ")
        num = int(num)
        for i in range(num):
            if direction == "R":
                hposx += 1
                if hposx == tposx + 2:
                    tposx = hposx - 1
                    tposy = hposy
            elif direction == "L":
                hposx -= 1
                if hposx == tposx - 2:
                    tposx = hposx + 1
                    tposy = hposy
            elif direction == "U":
                hposy += 1
                if hposy == tposy + 2:
                    tposx = hposx
                    tposy = hposy - 1
            elif direction == "D":
                hposy -= 1
                if hposy == tposy - 2:
                    tposx = hposx
                    tposy = hposy + 1
            poss.add((tposx, tposy))

            print(tposx, tposy)

print(len(poss))
