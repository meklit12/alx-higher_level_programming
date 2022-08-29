#!/usr/bin/env python3
"""
removes all characters c and C from a string
"""


def no_c(my_string):
    new_str = ""
    for i in range(len(my_string)):
        if my_string[i] == 'C' or my_string[i] == 'c':
            pass
        else:
            new_str += my_string[i]
    return new_str
