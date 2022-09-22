#!/usr/bin/python3
from sys import argv

somme = 0

if len(argv) > 1:
    for i in range(1, len(argv)):
        somme += int(argv[i])
print("{}".format(somme))
