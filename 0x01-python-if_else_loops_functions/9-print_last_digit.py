#!/usr/bin/python3

def print_last_digit(number):
    num = number
    if num < 0:
        num = -num
    print("{}".format(num % 10), end="")
    return num % 10
