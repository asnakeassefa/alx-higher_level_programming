#!/usr/bin/python3
def safe_print_integer(value):
    try:
        "{:d}".format(value)
        return isinstance(value)
    except:
        return isinstance(value,int)
