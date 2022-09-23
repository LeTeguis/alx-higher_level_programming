#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        operator = {"+": add, "-": sub, "*": mul, "/": div}
        a = int(argv[1])
        b = int(argv[3])
        o = argv[2]
        if o in operator:
            print("{:d} {} {:d} = {:d}".format(a, o, b, operator[o](a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
