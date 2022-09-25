#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    list_result = []
    if len(my_list) > 0:
        for e in my_list:
            list_result.append(True if e % 2 == 0 else False)
    return list_result
