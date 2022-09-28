#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list is None or len(my_list) <= 0:
        return 0
    n, x = 0, 0
    for t in my_list:
        if len(t) != 2:
            return 0
        x += (t[0] * t[1])
        n += t[1]
    return x / n
