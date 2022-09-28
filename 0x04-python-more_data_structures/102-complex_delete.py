#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    new_dic = {k: v for k, v in a_dictionary.items()}
    for k in new_dic:
        if a_dictionary[k] is value:
            del a_dictionary[k]
    return a_dictionary
