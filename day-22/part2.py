#!/usr/bin/env python3

import fileinput
import re

*grid, _, path = fileinput.input()
pos, vel = complex(grid[0].index('.'), 0), 1
path = re.findall(r'\d+|[RL]', path)
grid = {complex(x, y): c for y, l in enumerate(grid)
        for x, c in enumerate(l) if c in '.#'}
slen = 50


def where(pos, vel):
    sq = int(3 * (pos.imag // slen) + pos.real // slen)
    val = m[sq][vel](pos)
    sq2 = int(3 * (val[0].imag // slen) + val[0].real // slen)
    print(f"{sq} {sq2} {pos} + {vel} -> {val[0]} + {val[1]}")
    return val


m = {
    1: {
        -1: lambda p: (complex(0, 3 * slen - 1 - p.imag % slen), 1),
        -1j: lambda p: (complex(0, 3 * slen + p.real % slen), 1),
    },
    2: {
        1: lambda p: (complex(2 * slen - 1, 3 * slen - 1 - p.imag % slen), -1),
        1j: lambda p: (complex(2 * slen - 1, slen + p.real % slen), -1),
        -1j: lambda p: (complex(p.real % slen, 4 * slen - 1), -1j),
    },
    4: {
        1: lambda p: (complex(2 * slen + p.imag % slen, slen - 1), -1j),
        -1: lambda p: (complex(p.imag % slen, 2 * slen), 1j),
    },
    6: {
        -1: lambda p: (complex(slen, slen - 1 - p.imag % slen), 1),
        -1j: lambda p: (complex(slen, slen + p.real % slen), 1),
    },
    7: {
        1: lambda p: (complex(3 * slen - 1, slen - 1 - p.imag % slen), -1),
        1j: lambda p: (complex(slen - 1, 3 * slen + p.real % slen), -1),
    },
    9: {
        -1: lambda p: (complex(slen + p.imag % slen, 0), 1j),
        1: lambda p: (complex(slen + p.imag % slen, 3 * slen - 1), -1j),
        1j: lambda p: (complex(2 * slen + p.real % slen, 0), 1j),
    }
}

for p in path:
    if p == "R":
        vel *= 1j
    elif p == "L":
        vel *= -1j
    else:
        for _ in range(int(p)):
            new_pos = pos + vel
            new_vel = vel
            if new_pos not in grid:
                new_pos, new_vel = where(pos, vel)
            if grid[new_pos] == '.':
                pos = new_pos
                vel = new_vel
            else:
                break


print(int(1000 * (pos.imag + 1) + 4 *  # noqa
      (pos.real + 1) + [1, 1j, -1, -1j].index(vel)))
