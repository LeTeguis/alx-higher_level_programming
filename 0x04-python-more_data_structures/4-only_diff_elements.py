#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    mr = []
    for e in set_1:
        if e not in set_2:
            mr.append(e)
    for e in set_2:
        if e not in set_1:
            mr.append(e)
    return mr
