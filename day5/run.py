#! /usr/bin/python3.8
import numpy as np
import re
from numpy.core.fromnumeric import diagonal

from numpy.core.numeric import indices
from numpy.lib.twodim_base import diag

def parse_input(f):
    coords = []
    x_max = 0

    while line := f.readline():
        coords_str = re.split(',| -> |\\n', line)
        x0 = int(coords_str[0].strip())
        y0 = int(coords_str[1].strip())
        x1 = int(coords_str[2].strip())
        y1 = int(coords_str[3].strip())

        x_max = x0 if x0 > x_max else x_max
        x_max = x1 if x1 > x_max else x_max
        x_max = y0 if y0 > x_max else x_max
        x_max = y1 if y1 > x_max else x_max
        coord = np.array([[x0,y0], [x1,y1]])
        coords.append(coord)

    return coords, x_max

def correct_angle(x0,x1,y0,y1):
    dx = max(x0,x1) - min(x0,x1)
    dy = max(y0,y1) - min(y0,y1)

    return dx == dy

def build_map(coords, dim):
    map = np.zeros((dim+1, dim+1))
    c_arr = np.array(coords)

    for c0, c1 in c_arr:
        x0 = c0[0]
        x1 = c1[0]
        y0 = c0[1]
        y1 = c1[1]

        #vertical, x0 = x1
        if x0 == x1:
            map[min(y0,y1):max(y0,y1)+1, x0] += 1
        #horizontal, y0 = y1
        elif y0 == y1:
            map[y0, min(x0,x1):max(x0,x1)+1] += 1
        elif correct_angle(x0,x1,y0,y1):
            sX = 0
            sY = 0
            eX = 0
            eY = 0

            if x0 < x1:
                sX = x0
                sY = y0
                eX = x1
                eY = y1
            else:
                sX = x1
                sY = y1
                eX = x0
                eY = y0

            dY = -1 if eY < sY else 1
            iy = sY
            for ix in range (sX, eX+1):
                map[iy, ix] += 1
                iy += dY
    return map

def part_two(f):
    coords, dim  = parse_input(f)
    map = build_map(coords, dim)
    print(map)
    return np.shape(np.where(map>1))[1]

f = open("input", 'r')

p2 = part_two(f)
print(p2)