#!/usr/bin/python3

def no_c(my_string):
    new_string = ""
    for e in my_string:
        if e != 'c' and e != 'C':
            new_string += e
    return (new_string)
