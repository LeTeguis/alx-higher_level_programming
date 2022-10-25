#!/usr/bin/python3

"""
    Module: 0-lookup
    modulue to print objet information
"""


def lookup(obj):
    """
    lookup: print variable and method

    Arg:
        obj: object

    :return: list of methode and variable
    """
    return dir(obj)
