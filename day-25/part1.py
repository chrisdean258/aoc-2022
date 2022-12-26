#!/usr/bin/env python3

import fileinput


def decode(line):
    s = 0
    decode = {'0': 0, '1': 1, '2': 2, '-': -1, '=': -2}
    for ch in line:
        s *= 5
        s += decode[ch]
    return s


def encode(num):
    chars = []
    while num != 0:
        small_num = num % 5
        if small_num == 4:
            num += 1
            chars.append('-')
        if small_num == 3:
            num += 2
            chars.append('=')
        if small_num == 2:
            chars.append('2')
        if small_num == 1:
            chars.append('1')
        if small_num == 0:
            chars.append('0')
        num //= 5
    return "".join(reversed(chars))


print(encode(sum(decode(a.strip()) for a in fileinput.input())))
