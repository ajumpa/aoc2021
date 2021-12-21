#!/usr/bin/python3.8


f = open("input", 'r')

c = 0
n1 = f.readline()
while n2 := f.readline():
    if ( int(n2) > int(n1) ):
        c += 1
    n1 = n2

print(c)
