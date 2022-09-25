#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list == None or my_list == []:
        print()
        return
    for e in my_list[::-1]:
        print("{:d}".format(e))
