#!/usr/bin/python3
"""
multipy by 2
"""


def multiply_by_2(a_dictionary):
    new_dict = dict(a_dictionary)
    for key in a_dictionary:
        new_dict[key] = new_dict[key] * 2
    return new_dict
