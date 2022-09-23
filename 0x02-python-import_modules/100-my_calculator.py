#!/usr/bin/python3
if __name__ == "__main__":
    '''from calculator_1 import add, sub, mul, div'''
    import calculator_1 as cal
    from sys import argv

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        operator = {"+": cal.add, "-": cal.sub, "*": cal.mul, "/": cal.div}
        a = int(argv[1])
        b = int(argv[3])
        o = argv[2]
        if o in operator:
            print("{:d} {} {:d} = {:d}".format(a, o, b, operator[o](a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
