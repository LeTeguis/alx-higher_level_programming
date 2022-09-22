#!/usr/bin/python3
from sys import argv

s_argv = len(argv)

if s_argv > 1:
    if s_argv > 2:
        print("{} arguments:".format(s_argv - 1))
    else:
        print("{} argument:".format(s_argv - 1))

    for i in range(1, s_argv):
        print("{}: {}".format(i, argv[i]))
else:
    print("{} arguments.".format(s_argv - 1))
