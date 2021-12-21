#!/usr/bin/python3.8

def parsemove(move, aim):
    if len(move) == 10:
        return int(move[8]), int(move[8])*aim, 0
    if len(move) == 7:
        return 0, 0, int(move[5])
    else:
        return 0, 0, -int(move[3])


f = open("input", 'r')

aim = 0
x = 0
y = 0

while move := f.readline():
    dx ,dy, d_aim = parsemove(move, aim)
    x += dx
    y += dy
    aim += d_aim

print(x*y)

