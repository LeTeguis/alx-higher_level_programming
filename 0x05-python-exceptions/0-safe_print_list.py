#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        size = int(x)
        i = 0
        for e in my_list:
            if size < 0 or i >= size:
                break
            print(f"{e}", end="")
            i += 1
    except ValueError:
        return 0
    print()
    return i
