#!/usr/bin/python3

for i in range(26):
    print("{}".format(
        chr(25 - i + ord("a")) if (26 - i) % 2 == 0 else
        chr(25 - i + ord("A"))), end="")
