#!/usr/bin/env python3

def no_c(my_string):
    new_str = ""
    for e in my_string:
        if e != 'c' and e != 'C':
            new_str += e
    return (new_str)
