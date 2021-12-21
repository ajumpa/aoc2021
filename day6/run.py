#! /usr/bin/python3.8
from sre_constants import NOT_LITERAL_LOC_IGNORE
import numpy as np
import re

NDAYS = 256

def parse_input(f):
    f_input = re.split(',', f.readline())

    return np.array(f_input).astype(int)

def create_map(fish):
    map = np.zeros(shape=(9,),dtype=int)
    occur = np.bincount(fish)
    map[:np.size(occur)] = occur
    return map


# Just keep count of the fish
def calc_fish(fish_map):
    for t in range (NDAYS):
        day0 = fish_map[0]
        day1 = fish_map[1]
        day2 = fish_map[2]
        day3 = fish_map[3]
        day4 = fish_map[4]
        day5 = fish_map[5]
        day6 = fish_map[6]
        day7 = fish_map[7]
        day8 = fish_map[8]

        fish_map[0] = day1
        fish_map[1] = day2
        fish_map[2] = day3
        fish_map[3] = day4
        fish_map[4] = day5
        fish_map[5] = day6
        fish_map[6] = day0 + day7
        fish_map[7] = day8
        fish_map[8] = day0


    return np.sum(fish_map)

#380 TOO LOW
# 1079922 TOO HIGH
def part_one(f):
    fish = parse_input(f)
    fish_map = create_map(fish)
    n_fish = calc_fish(fish_map)
    return n_fish

f = open("input", 'r')

answer = part_one(f)
print(answer)