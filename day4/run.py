#! /usr/bin/python3.8
from os import read
import numpy as np

B_SZ = 25
R_SZ = 5

def parse_input(file):

    numbers_rand = np.fromstring(file.readline().strip(), dtype=int, sep=',')
    data = np.zeros((1,5,5))
    b_ix = 0
    r_ix = 0
    while line := file.readline():
        line = line.strip()
        if len(line) > 0:
            row = np.fromstring(line, dtype=int, sep=' ')
            data[b_ix,r_ix,:] = row
            r_ix += 1
        else:
            data = np.append(data, np.zeros((1,R_SZ,R_SZ)), axis=0)
            b_ix += 1
            r_ix = 0

    return numbers_rand, data.astype(int)[1:]


def calc_score(score, board, n):
    return np.sum(board[np.where(score != 1)]) * n

def b_check(score, r, c):
    return score[r,:].all() == 1 or score[:,c].all() == 1

def part_one(numbers_rand, boards):
    scores = np.zeros((len(boards),R_SZ,R_SZ),dtype=int)

    for n in numbers_rand:
        for i in range(len(boards)):
            pos = np.argwhere(boards[i]==n)
            if len(pos) > 0:
                r = pos[0][0]
                c = pos[0][1]
                scores[i,r,c] = 1
                if b_check(scores[i], r,c):
                    return calc_score(scores[i], boards[i], n)

def part_two(numbers_rand, boards):
    scores = np.zeros((len(boards),R_SZ,R_SZ),dtype=int)
    winners = []
    for n in numbers_rand:
        for i in range(len(boards)):
            pos = np.argwhere(boards[i]==n)
            if len(pos) > 0:
                r = pos[0][0]
                c = pos[0][1]
                scores[i,r,c] = 1
                if b_check(scores[i], r,c): 
                    print("Board " + str(i) + " has bingo")
                    if i not in winners:
                        winners.append(i)
                    print(winners)
                    if len(winners) == len(boards):
                        return calc_score(scores[i], boards[i], n)

f = open("input", 'r')

numbers_rand, boards = parse_input(f)

p1 = part_one(numbers_rand, boards)
p2 = part_two(numbers_rand, boards)

print(p2)