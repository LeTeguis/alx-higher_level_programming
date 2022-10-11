#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    nbr = 0
    while True:
        try:
            print("{:d}".format(my_list[i]), end="")
            nbr += 1
            if nbr >= x:
                print()
                return nbr
        except (ValueError, TypeError):
            pass
        i += 1
