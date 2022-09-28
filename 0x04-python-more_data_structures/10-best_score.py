#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) <= 0:
        return None
    max_key = list(a_dictionary)[0]
    for k, v in a_dictionary.items():
        if a_dictionary[max_key] < v:
            max_key = k
    return max_key
