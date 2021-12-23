#! /usr/bin/python3.8
import numpy as np
import re

def parse_input(f):
    f_input = re.split(',', f.readline())

    return np.array(f_input).astype(int)

def calc_distances(map):
    n = np.shape(map)[0]
    for ix in range(1,n):
        map[ix,1:] = np.absolute(map[0,1:] - map[ix,0])
    return map

def create_map(input):
    n = np.size(input)
    map = np.zeros((n+1,n+1),dtype=int)
    map[1::,0] = input
    map[0,1::] = input
    return calc_distances(map)

def trace_map(map):
    n = np.shape(map)[0]-1
    iy = 1
    min_sum = np.inf
    min_x = 1
    for row in map[1:,:]:
        sum = np.sum(row[1:])
        if sum < min_sum:
            min_sum = sum
            min_x = row[0]
    print(min_x)
            
    
def part_one(input):
    map = create_map(input)
    print(map)
    trace_map(map)

f = open("input2", 'r')

#331 TOO LOW
#1650 TOO LOW
input = parse_input(f)
input = np.sort(input)
part_one(input)