#!/usr/bin/python3

def safe_print_integer(value):
    try:
        v = int(value)
        print("{:d}".format(v))
    except ValueError:
        return False
    return True
