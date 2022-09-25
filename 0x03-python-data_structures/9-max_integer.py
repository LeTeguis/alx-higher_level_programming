#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) > 0:
        max_ = my_list[0]
        for m in my_list:
            if m > max_:
                max_ = m
        return max_
    return None
