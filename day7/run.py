#! /usr/bin/python3.8
import numpy as np
import re

def parse_input(f):
    f_input = re.split(',', f.readline())

    return np.array(f_input).astype(int)

def calc_distances(map):
    print(map)

def create_map(input):
    n = np.size(input)
    map = np.zeros((n+1,n+1),dtype=int)
    map[1::,0] = input
    map[0,1::] = input
    return calc_distances(map)

def part_one(input):
    map = create_map(input)

f = open("input2", 'r')

#331 too low

input = parse_input(f)
input = np.sort(input)
part_one(input)