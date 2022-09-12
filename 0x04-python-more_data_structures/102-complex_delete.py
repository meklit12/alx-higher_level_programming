#!/usr/bin/python3
"""
complex delete
"""


def complex_delete(my_dict, value):
    keys_to_del = []
    for key in my_dict:
        if my_dict[key] == value:
            keys_to_del.append(key)
    for key in keys_to_del:
        del my_dict[key]
    return my_dict
