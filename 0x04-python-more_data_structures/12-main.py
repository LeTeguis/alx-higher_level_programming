#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int
int_to_roman = __import__('12-roman_to_int').int_to_roman

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = int_to_roman(3999)
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

for i in range(4000):
    r = int_to_roman(i)
    if i != roman_to_int(r):
        print(f"erreur_{i}: {r} : {roman_to_int(r)}")
