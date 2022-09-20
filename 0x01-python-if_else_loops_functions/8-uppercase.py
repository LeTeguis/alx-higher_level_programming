#!/usr/bin/python3

def uppercase(str):
    for c in str:
        C = c
        if ord(c) >= ord("a") and ord(c) <= ord("z"):
            C = chr(ord(c) - ord("a") + ord("A"))
        print("{}".format(C), end="")
    print("")
