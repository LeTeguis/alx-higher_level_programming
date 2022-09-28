#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for e in sorted(a_dictionary):
        print(f"{e}: {a_dictionary[e]}")
