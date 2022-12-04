#!/usr/bin/env python3

scores = {
    "A X": 3 + 0,
    "A Y": 1 + 3,
    "A Z": 2 + 6,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 2 + 0,
    "C Y": 3 + 3,
    "C Z": 1 + 6,
}


score = 0
with open(0) as f:
    for line in f:
        score += scores[line.strip()]

print(score)
