#!/usr/bin/python3

def uniq_add(my_list=[]):
    ml = []
    somme = 0
    for e in my_list:
        if e not in ml:
            ml.append(e)
            somme += e
    return somme
