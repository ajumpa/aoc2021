#!/usr/bin/python3.8
f = open("input", 'r')

cnt = 0

a = f.readline()
b = f.readline()
c = f.readline()
while d := f.readline():

    sum1 = int(a) + int(b) + int(c)
    sum2 = int(b) + int(c) + int(d)

    if sum2 > sum1:
        cnt += 1

    a = b
    b = c
    c = d

print(cnt)

