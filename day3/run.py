#!/usr/bin/python3.8
import numpy as np

def binary_conv(n):
    accum = 0
    i = 0
    for x in reversed(n):
        accum += x * (2 ** i)
        i += 1
    return accum

def construct(cnts):
    mcb = [0 for i in range(len(cnts))]
    lcb = [0 for i in range(len(cnts))]

    i = 0
    for tup in (cnts):
        mcb[i] = 1 if tup[1] >= tup[0] else 0
        lcb[i] = 0 if tup[0] <= tup[1] else 1
        i += 1

    return mcb, lcb



f = open("input", 'r')
w_size = len(f.readline().strip())
f.seek(0)

cnts = np.zeros((w_size,2))
line = 0
data_arr = np.zeros((1,w_size))

f.seek(0)
while n := f.readline().strip():
    for i in range(len(n)):
        data_arr[line][i] = n[i]
        cnts[i][int(n[i])] += 1

    line += 1
    data_arr = np.append(data_arr, np.zeros((1,w_size)), axis=0)

data_arr = data_arr[:len(data_arr)-1].astype(int)

mcb, lcb = construct(cnts)

print(str(binary_conv(mcb))
        + " x "
        + str(binary_conv(lcb))
        + " = "
        + str(binary_conv(mcb)*binary_conv(lcb)))
f.seek(0)


# part 2
"""answer greater than 2572440"""

num_w = np.shape(data_arr)[0]

o2_list = np.array(data_arr, copy=True)
co2_list = np.array(data_arr, copy=True)

for i in range(w_size):
    o2_cnt = np.bincount(o2_list[::,i])
    co2_cnt = np.bincount(co2_list[::,i])

    if len(o2_cnt) > 1:
        if o2_cnt[1] >= o2_cnt[0] and len(o2_list) > 1:
            o2_list = o2_list[np.where(o2_list[::,i] == 1)]
        else:
            o2_list = o2_list[np.where(o2_list[::,i] == 0)]

    if len(co2_cnt) > 1 and (len(co2_list) > 1):
        if co2_cnt[0] <= co2_cnt[1]:
            co2_list = co2_list[np.where(co2_list[::,i] == 0)]
        else:
            co2_list = co2_list[np.where(co2_list[::,i] == 1)]

print(binary_conv(o2_list[len(o2_list)-1]))
print(binary_conv(co2_list[len(co2_list)-1]))
print(binary_conv(o2_list[len(o2_list)-1]) * binary_conv(co2_list[len(co2_list)-1]))