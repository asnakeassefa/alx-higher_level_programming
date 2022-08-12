#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for i in range(0,x):
        try:
            print(my_list[i], end="")
        except IndexError:
            print(end="\n")
            return i
    print(end="\n")
    return i+1