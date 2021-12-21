#!/usr/bin/python3.8

def parsemove(move):
    if len(move) == 10:
        return int(move[8]), 0
    if len(move) == 7:
        return 0, int(move[5])
    else:
        return 0, -int(move[3])


f = open("input", 'r')

x = 0
y = 0

while move := f.readline():
    dx,dy = parsemove(move)
    x += dx
    y += dy

print(x*y)

